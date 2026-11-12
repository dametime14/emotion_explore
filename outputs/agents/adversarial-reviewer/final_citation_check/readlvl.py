import re,random,json,glob,os
R='/home/user/emotion_explore/outputs/'
exec(open('draw.py').read().split('top={')[0])
authors={'RQ01':'geometry-info','RQ03':'geometry-info','RQ08':'llm-semantics','RQ10':'encoding-foundation','RQ14':'llm-semantics','RQ15':'frontier-ai','RQ32':'systems-neuro','RQ33':'multimodal-dynamics','RQ44':'emotion-theory','RQ60':'multimodal-dynamics'}
pop=[]
for f in sorted(glob.glob(R+'rq_cards/*.md')):
    k=os.path.basename(f)[:4]
    L=open(f).read().split('\n')
    s=[i for i,l in enumerate(L) if l.startswith('## 4.')][0]
    e=[i for i,l in enumerate(L) if l.startswith('## 5.')][0]
    for i in range(s,e):
        l=L[i]
        if not l.startswith('|') or not ids_in(l): continue
        cells=[c.strip() for c in l.split('|')]
        # find reading-level cell
        lvl=[c for c in cells if re.search(r'본문',c) and len(c)<60]
        if lvl and not re.search(r'DB|db|다른 에이전트',lvl[0]):
            pop.append((k,i+1,ids_in(l)[0],lvl[0]))
print(len(pop))
rng=random.Random(20261112+5)
pick=rng.sample(pop,3)
for p in pick: print(p)
# lookup
for k,ln,i,lvl in pick:
    ag=authors[k]
    for jf in glob.glob(R+f'agents/{ag}/literature*.jsonl'):
        for line in open(jf):
            try: r=json.loads(line)
            except: continue
            blob=(str(r.get('id',''))+' '+str(r.get('url',''))).lower()
            key=i.split(':',1)[1].lower()
            if key in blob:
                print('  ->',ag,os.path.basename(jf),'discussion_read=',r.get('discussion_read'),'| fds:',[ (fd.get('section') if isinstance(fd,dict) else fd) for fd in (r.get('future_directions') or [])][:3])
