import re,json,csv,glob,os,unicodedata
R='/home/user/emotion_explore/outputs/'
files=sorted(glob.glob(R+'rq_cards/*.md'))+[R+'final_synthesis.md',R+'pilots.md']
rows=list(csv.DictReader(open(R+'literature/literature_db.csv')))
def n(s):
    s=unicodedata.normalize('NFKD',s); s=''.join(c for c in s if not unicodedata.combining(c)); return s.lower()
# pattern: Surname (optional particle) [et al.| & Surname | and Surname]? [,]? year
PAT=re.compile(r"((?:(?:van der|van de|van|de la|de|la|dupré la|st\.?-|d')\s?)?[A-Z][A-Za-zÀ-ÿ'\-]+(?:\s(?:et al\.?|외|&|and)\s?(?:[A-Z][A-Za-zÀ-ÿ'\-]+)?)?(?:\s&\s[A-Z][A-Za-zÀ-ÿ'\-]+)?),?\s\(?((?:19|20)\d{2})[a-z]?\)?")
STOP=set('Stage Round Table Figure Fig Section CVPR NeurIPS ICLR ICML ECCV ICCV AAAI ACL EMNLP Nature Science PNAS Discussion Results Methods Limitations Supplementary Appendix November January February March April May June July August September October December RQ Axis Version GPT Qwen Claude Gemini Llama LLaVA Phase Pilot Deliverable The A An In On At Of Wave Step Card Matrix Top Sample'.split())
mentions={}
for f in files:
    L=open(f).read().split('\n')
    for ln,line in enumerate(L,1):
        for m in PAT.finditer(line):
            auth=m.group(1).strip(); yr=m.group(2)
            first=re.split(r'\s(?:et al|외|&|and)',auth)[0].strip()
            if first in STOP or first.isupper() and len(first)>1 and first not in ('LeDoux',): 
                if first in STOP: continue
            key=(first,yr)
            has_id=bool(re.search(r'(10\.\d{4,9}/|arxiv[:\s]*\d{4}\.\d{4,5}|PMID)',line,re.I))
            mentions.setdefault(key,[]).append((os.path.basename(f),ln,has_id))
# map to DB
def dbmatch(first,yr):
    out=[]
    fn=n(first).replace(' ','')
    for r in rows:
        c=n(r['citation'])
        # first author surname = start of citation
        lead=re.split(r'[,(]',c)[0].replace(' ','')
        yrs=re.findall(r'(?:19|20)\d{2}',r['citation']+' '+r['year'])
        if (fn in lead or lead.startswith(fn[:6])) and (yr in yrs):
            out.append((r['uid'],r['verified'],r['citation'][:100]))
    return out
res=[]
for (first,yr),ms in sorted(mentions.items()):
    dm=dbmatch(first,yr)
    res.append(dict(author=first,year=yr,n=len(ms),n_noid=sum(1 for m in ms if not m[2]),where=sorted(set(f"{m[0]}:{m[1]}" for m in ms))[:12],db=dm))
json.dump(res,open('authyear.json','w'),ensure_ascii=False,indent=1)
for r in res:
    tag='DBV' if any(d[1]=='True' for d in r['db']) else ('DBU' if r['db'] else 'NONE')
    print(tag, r['author'], r['year'], 'n=',r['n'],'noid=',r['n_noid'], '|', (r['db'][0][2][:70] if r['db'] else ''), '| ndb=',len(r['db']))
