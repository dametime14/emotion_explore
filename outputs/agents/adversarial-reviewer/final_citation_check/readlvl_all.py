import re,json,glob,os,csv
R='/home/user/emotion_explore/outputs/'
exec(open('draw.py').read().split('top={')[0])
authors={'RQ01':'geometry-info','RQ03':'geometry-info','RQ08':'llm-semantics','RQ10':'encoding-foundation','RQ14':'llm-semantics','RQ15':'frontier-ai','RQ32':'systems-neuro','RQ33':'multimodal-dynamics','RQ44':'emotion-theory','RQ60':'multimodal-dynamics'}
db=list(csv.DictReader(open(R+'literature/literature_db.csv')))
def dbrow(key):
    for r in db:
        if key in (r['all_ids']+' '+r['doi']+' '+r['arxiv']).lower(): return r
def agrec(ag,key):
    out=[]
    for jf in glob.glob(R+f'agents/{ag}/literature*.jsonl'):
        for line in open(jf):
            try: r=json.loads(line)
            except: continue
            if key in (str(r.get('id',''))+' '+str(r.get('url',''))).lower(): out.append(r.get('discussion_read'))
    return out
for f in sorted(glob.glob(R+'rq_cards/*.md')):
    k=os.path.basename(f)[:4]
    L=open(f).read().split('\n')
    s=[i for i,l in enumerate(L) if l.startswith('## 4.')][0]
    e=[i for i,l in enumerate(L) if l.startswith('## 5.')][0]
    for i in range(s,e):
        l=L[i]
        if not l.startswith('|') or not ids_in(l): continue
        cells=[c.strip() for c in l.split('|')]
        lvl=[c for c in cells if re.search(r'본문|초록|미열람|서지|DB|db',c) and len(c)<70]
        if not lvl: continue
        lv=lvl[0]
        key=ids_in(l)[0].split(':',1)[1].lower()
        a=agrec(authors[k],key); d=dbrow(key)
        dd=d['discussion_read'] if d else None
        claims_full='본문' in lv
        own_ok = any(x=='full_text' for x in a)
        flag=''
        if claims_full and not re.search(r'DB|db|다른 에이전트',lv) and not own_ok: flag='OWN_MISMATCH'
        if claims_full and re.search(r'DB|db|다른 에이전트',lv) and dd!='full_text': flag='DB_MISMATCH'
        if flag: print(flag,k,i+1,key,'| card:',lv,'| own:',a,'| db:',dd)
