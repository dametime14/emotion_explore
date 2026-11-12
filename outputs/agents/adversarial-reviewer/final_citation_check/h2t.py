import sys,re,html
s=open(sys.argv[1],encoding='utf-8',errors='ignore').read()
s=re.sub(r'(?is)<(script|style|math)[^>]*>.*?</\1>',' ',s)
s=re.sub(r'(?i)<(h[1-6])[^>]*>','\n\n## ',s)
s=re.sub(r'(?i)</?(p|div|li|tr|section|br)[^>]*>','\n',s)
s=re.sub(r'<[^>]+>',' ',s)
s=html.unescape(s)
s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n\n',s)
open(sys.argv[2],'w').write(s)
