import csv, re, sys, json, glob, os
ROOT='/home/user/emotion_explore'
rows=list(csv.DictReader(open(f'{ROOT}/outputs/literature/literature_db.csv')))
DOI_RE=re.compile(r'10\.\d{4,9}/[^\s"<>|`\]\)\(,;，、]+', re.I)
ARX_RE=re.compile(r'(?:arxiv[:/\s]*|abs/|pdf/)(\d{4}\.\d{4,5})(?:v\d+)?', re.I)
PMID_RE=re.compile(r'PMID[:\s]*(\d{6,9})', re.I)
def norm_doi(d):
    d=d.strip().rstrip('.,;:)*_').lower()
    return d
# build index
idx={}
for r in rows:
    ids=set()
    for tok in re.split(r'[;\s|]+', r['all_ids']+' '+r['doi']+' '+r['arxiv']+' '+r['uid']+' '+r['url']):
        tok=tok.strip()
        if not tok: continue
        for m in DOI_RE.finditer(tok):
            d=norm_doi(m.group(0))
            m2=re.match(r'10\.48550/arxiv\.(\d{4}\.\d{4,5})',d)
            if m2: ids.add('arxiv:'+m2.group(1))
            else: ids.add('doi:'+d)
        for m in ARX_RE.finditer(tok): ids.add('arxiv:'+m.group(1))
        m=re.match(r'^(\d{4}\.\d{4,5})(v\d+)?$',tok)
        if m: ids.add('arxiv:'+m.group(1))
    for m in PMID_RE.finditer(r['verified_by']+' '+r['all_ids']+' '+r['citation']+' '+r['url']):
        ids.add('pmid:'+m.group(1))
    for m in re.finditer(r'pubmed\.ncbi\.nlm\.nih\.gov/(\d+)', r['url']+' '+r['all_ids']):
        ids.add('pmid:'+m.group(1))
    for i in ids: idx.setdefault(i,[]).append(r)
REPO_PREFIX={'10.6084':'figshare','10.18112':'OpenNeuro','10.5281':'Zenodo','10.17605':'OSF','10.5061':'Dryad','10.25740':'Columbia/academic commons','10.12751':'G-Node','10.15387':'NIMH Data Archive','10.7910':'Harvard Dataverse','10.35092':'?','10.17632':'Mendeley Data','10.24433':'CRCNS?','10.60864':'?'}
files=sorted(glob.glob(f'{ROOT}/outputs/rq_cards/*.md'))+[f'{ROOT}/outputs/final_synthesis.md',f'{ROOT}/outputs/pilots.md']
out={}
for f in files:
    txt=open(f).read()
    lines=txt.split('\n')
    found={}
    for ln,line in enumerate(lines,1):
        for m in DOI_RE.finditer(line):
            d=norm_doi(m.group(0))
            m2=re.match(r'10\.48550/arxiv\.(\d{4}\.\d{4,5})',d)
            key=('arxiv:'+m2.group(1)) if m2 else 'doi:'+d
            found.setdefault(key,[]).append(ln)
        for m in ARX_RE.finditer(line):
            found.setdefault('arxiv:'+m.group(1),[]).append(ln)
        for m in PMID_RE.finditer(line):
            found.setdefault('pmid:'+m.group(1),[]).append(ln)
    res=[]
    for k,lns in sorted(found.items()):
        hits=idx.get(k,[])
        pre=k[4:].split('/')[0] if k.startswith('doi:') else ''
        repo=REPO_PREFIX.get(pre)
        status='repo:'+repo if repo else ('db_verified' if any(h['verified']=='True' for h in hits) else ('db_unverified' if hits else 'not_in_db'))
        res.append(dict(id=k,lines=sorted(set(lns)),status=status,cit=(hits[0]['citation'][:90] if hits else '')))
    out[os.path.basename(f)]=res
json.dump(out,open(sys.argv[1],'w'),ensure_ascii=False,indent=1)
for f,res in out.items():
    from collections import Counter
    c=Counter(r['status'] for r in res)
    print(f, len(res), dict(c))
    for r in res:
        if r['status']!='db_verified': print('   ',r['status'],r['id'],r['lines'][:6])
