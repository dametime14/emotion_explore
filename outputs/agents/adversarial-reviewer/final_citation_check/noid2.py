import json,re,glob,os,csv
R='/home/user/emotion_explore/outputs/'
src=open('authyear.py').read().split('res=[]')[0]
exec(src)
uid2ids={}
for r in rows:
    ids=set(x.strip().lower().replace('doi:','').replace('arxiv:','') for x in re.split(r'[;|\s]+',r['all_ids']+' '+r['doi']+' '+r['arxiv']) if x.strip())
    uid2ids[r['uid']]=ids
texts={os.path.basename(f):open(f).read().lower() for f in files}
out=[]
for (first,yr),ms in sorted(mentions.items()):
    cands=dbmatch(first,yr)
    byf={}
    for f,ln,has in ms: byf.setdefault(f,[]).append(ln)
    for f,lns in byf.items():
        t=texts[f]
        present=[c for c in cands if any(i and i in t for i in uid2ids[c[0]])]
        if cands and len(present)>=1 and (len(cands)==1 or len(present)==1):
            continue  # resolvable within file
        out.append(dict(file=f,author=first,year=yr,lines=sorted(set(lns)),cands=[(c[0],c[1],c[2][:80]) for c in cands],present=[c[0] for c in present]))
json.dump(out,open('noid2.json','w'),ensure_ascii=False,indent=1)
for o in out:
    print(o['file'][:20],o['author'],o['year'],o['lines'][:6],'| cands:',[(c[0]) for c in o['cands']],'| present:',o['present'])
