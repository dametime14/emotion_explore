import re,random,json
R='/home/user/emotion_explore/outputs/'
SEED=20261112
DOI_RE=re.compile(r'10\.\d{4,9}/[^\s"<>|`\]\)\(,;，、]+', re.I)
ARX_RE=re.compile(r'(?:arxiv[:/\s]*)(\d{4}\.\d{4,5})', re.I)
def ids_in(line):
    out=[]
    for m in DOI_RE.finditer(line):
        d=m.group(0).rstrip('.,;:)*_').lower()
        if d.startswith('10.6084'): continue
        out.append('doi:'+d)
    for m in ARX_RE.finditer(line): out.append('arxiv:'+m.group(1))
    return out
top={'RQ08':'RQ08_beyond_scene_description.md','RQ15':'RQ15_read_vs_ask_AI_emotion.md','RQ01':'RQ01_emotion_category_replication.md','RQ03':'RQ03_stimulus_ensemble_geometry.md','RQ14':'RQ14_who_did_what_to_whom.md'}
pop_cards={}
for k,f in top.items():
    L=open(R+'rq_cards/'+f).read().split('\n')
    s=[i for i,l in enumerate(L) if l.startswith('## 4. Prior Literature')][0]
    e=[i for i,l in enumerate(L) if l.startswith('## 5.')][0]
    rows=[]
    for i in range(s,e):
        l=L[i]
        if l.startswith('|') and ids_in(l):
            rows.append((i+1,ids_in(l)[0]))
    pop_cards[k]=rows
L=open(R+'final_synthesis.md').read().split('\n')
fs={}
for i,l in enumerate(L):
    for x in ids_in(l):
        fs.setdefault(x,[]).append(i+1)
pop_fs=sorted((v[0],k) for k,v in fs.items())
rng=random.Random(SEED)
draw_fs=rng.sample(pop_fs,5)
draw_cards={k:rng.sample(pop_cards[k],2) for k in sorted(top)}
print('final_synthesis population (first line, id):',len(pop_fs))
for x in sorted(draw_fs): print('  FS',x)
for k in sorted(top):
    print(k,'population',len(pop_cards[k]))
    for x in draw_cards[k]: print('  ',k,x)
json.dump({'fs':draw_fs,'cards':draw_cards},open('draw.json','w'))
