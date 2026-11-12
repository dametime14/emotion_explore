import json, time, urllib.request, urllib.parse, sys, re, xml.etree.ElementTree as ET
ids=json.load(open('uniq_ids.json'))
out={}
try: out=json.load(open('resolved.json'))
except Exception: pass
UA={'User-Agent':'citation-check/1.0'}
def get(url):
    req=urllib.request.Request(url,headers=UA)
    with urllib.request.urlopen(req,timeout=40) as r: return r.status, r.read()
for k in ids:
    if k in out and out[k].get('ok') is not None: continue
    if k.startswith('doi:'):
        d=k[4:]
        rec={'ok':None}
        for attempt in range(4):
            try:
                st,b=get('https://api.crossref.org/works/'+urllib.parse.quote(d,safe='/'))
                j=json.loads(b)['message']
                rec={'ok':True,'src':'crossref','title':(j.get('title') or [''])[0],'year':(j.get('issued',{}).get('date-parts',[[None]])[0][0]),'container':(j.get('container-title') or [''])[0],'first_author':((j.get('author') or [{}])[0].get('family','')),'type':j.get('type')}
                break
            except urllib.error.HTTPError as e:
                if e.code==404:
                    try:
                        st,b=get('https://doi.org/api/handles/'+d)
                        j=json.loads(b); rec={'ok':j.get('responseCode')==1,'src':'doi.org handle','title':'','note':'not in crossref'}
                    except Exception as e2: rec={'ok':False,'src':'doi.org handle','err':str(e2)}
                    break
                elif e.code==429: time.sleep(5*(attempt+1)); continue
                else: rec={'ok':None,'err':str(e)}; time.sleep(3)
            except Exception as e:
                rec={'ok':None,'err':str(e)}; time.sleep(3)
        out[k]=rec; time.sleep(1.2)
    json.dump(out,open('resolved.json','w'),ensure_ascii=False,indent=1)
# arxiv batch
arx=[k[6:] for k in ids if k.startswith('arxiv:') and not (k in out and out[k].get('ok'))]
if arx:
    st,b=get('https://export.arxiv.org/api/query?max_results=100&id_list='+','.join(arx))
    ns={'a':'http://www.w3.org/2005/Atom'}
    root=ET.fromstring(b)
    for e in root.findall('a:entry',ns):
        idu=e.find('a:id',ns).text
        m=re.search(r'abs/(\d{4}\.\d{4,5})',idu)
        t=e.find('a:title',ns)
        if not m: continue
        auth=e.find('a:author/a:name',ns)
        out['arxiv:'+m.group(1)]={'ok':True,'src':'arxiv','title':' '.join((t.text or '').split()),'year':e.find('a:published',ns).text[:4],'first_author':auth.text if auth is not None else ''}
    for a in arx:
        if 'arxiv:'+a not in out: out['arxiv:'+a]={'ok':False,'src':'arxiv','err':'no entry'}
json.dump(out,open('resolved.json','w'),ensure_ascii=False,indent=1)
print(sum(1 for v in out.values() if v.get('ok')), 'ok of', len(out))
for k,v in out.items():
    if not v.get('ok'): print(k,v)
