"""Generate self-contained profile artwork; run with Python 3."""
from pathlib import Path
from math import sin, cos, pi
from html import escape

OUT = Path(__file__).resolve().parents[1] / 'assets'
OUT.mkdir(exist_ok=True)

def text(x,y,s,size=14,color='var(--muted)',weight=400,extra=''):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" {extra}>{escape(s)}</text>'

def start(h,theme,title,desc):
    colors=('#0b1220','#eef5ff','#96a9c3','#24344d','#69e1d4','#a6a1ff') if theme=='dark' else ('#f5f8fc','#172b46','#546982','#d3ddeb','#087f80','#6853c8')
    bg,fg,muted,line,accent,violet=colors
    return [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" viewBox="0 0 1200 {h}" role="img" aria-labelledby="title desc">
<title id="title">{title}</title><desc id="desc">{desc}</desc>
<defs><radialGradient id="halo"><stop stop-color="{accent}" stop-opacity=".14"/><stop offset="1" stop-color="{bg}" stop-opacity="0"/></radialGradient>
<linearGradient id="beam"><stop stop-color="{accent}"/><stop offset="1" stop-color="{violet}"/></linearGradient>
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".8" fill="{muted}" opacity=".16"/></pattern></defs>
<style>svg{{--bg:{bg};--fg:{fg};--muted:{muted};--line:{line};--accent:{accent};--violet:{violet};font-family:Inter,Segoe UI,Arial,sans-serif}}
.flow{{stroke-dasharray:5 16;animation:travel 8s linear infinite}}.pulse{{transform-box:fill-box;transform-origin:center;animation:breathe 5s ease-in-out infinite}}
@keyframes travel{{to{{stroke-dashoffset:-168}}}}@keyframes breathe{{0%,100%{{opacity:.15;transform:scale(.85)}}50%{{opacity:.4;transform:scale(1.2)}}}}
@media(prefers-reduced-motion:reduce){{.flow,.pulse{{animation:none}}}}</style>
<rect x="1" y="1" width="1198" height="{h-2}" rx="24" fill="{bg}" stroke="{line}"/><rect x="1" y="1" width="1198" height="{h-2}" rx="24" fill="url(#grid)"/>''']

def hero(theme):
    p=start(440,theme,'Chxnho — Connecting knowledge. Understanding learning.','A layered network connects curriculum concepts, knowledge representation, reasoning, and learning.')
    p += ['<ellipse cx="925" cy="210" rx="290" ry="230" fill="url(#halo)"/>',text(54,58,'CHXNHO / RESEARCH & DEVELOPMENT',12,'var(--accent)',600,'letter-spacing="2.2"'),text(50,145,'Connecting',58,'var(--fg)',650),text(50,211,'knowledge.',58,'var(--fg)',650),text(54,259,'Understanding learning.',29,'var(--accent)',500),text(54,309,'Knowledge graphs, grounded reasoning,',17),text(54,336,'and intelligent systems for education.',17),'<path d="M54 373 H105" stroke="var(--accent)" stroke-width="2"/>',text(119,378,'ONTOLOGY  /  GRAPHRAG  /  AGENTS',11,extra='letter-spacing="1.5"')]
    p += ['<g id="network">']
    nodes=[]
    for ring,(rx,ry,n) in enumerate([(201,105,10),(137,163,9),(81,66,6)]):
        p += [f'<ellipse cx="889" cy="213" rx="{rx}" ry="{ry}" fill="none" stroke="var(--line)" transform="rotate({-24+ring*28} 889 213)"/>']
        for i in range(n):
            a=2*pi*i/n+ring*.42
            nodes.append((889+rx*cos(a),213+ry*sin(a)))
    for i,(x,y) in enumerate(nodes):
        for j in [(i+1)%len(nodes),(i+9)%len(nodes)]:
            xx,yy=nodes[j]
            p += [f'<path d="M{x:.1f} {y:.1f} L{xx:.1f} {yy:.1f}" fill="none" stroke="var(--line)" opacity=".7"/>']
    d='M'+' L'.join(f'{nodes[i][0]:.1f} {nodes[i][1]:.1f}' for i in [6,14,22,1,18])
    p += [f'<path d="{d}" fill="none" stroke="url(#beam)" stroke-width="2" opacity=".5"/>',f'<path class="flow" d="{d}" fill="none" stroke="var(--accent)" stroke-width="2.5"/>']
    for i,(x,y) in enumerate(nodes):
        color='var(--accent)' if i%3==0 else 'var(--violet)' if i%4==0 else 'var(--muted)'
        if i%3==0:p += [f'<circle class="pulse" cx="{x:.1f}" cy="{y:.1f}" r="12" fill="{color}" opacity=".15" style="animation-delay:-{i%5}s"/>']
        p += [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{4 if i%3 else 6}" fill="var(--bg)" stroke="{color}" stroke-width="1.8"/>']
    for x,y,w,label in [(689,74,139,'CURRICULUM'),(970,152,156,'KNOWLEDGE'),(727,337,150,'REASONING'),(968,350,148,'LEARNING')]:
        p += [f'<rect x="{x}" y="{y}" width="{w}" height="32" rx="16" fill="var(--bg)" stroke="var(--line)"/>',text(x+w/2,y+21,label,10,'var(--fg)',500,'text-anchor="middle" letter-spacing="1.5"')]
    art=''.join(p)+'</g></svg>'
    (OUT/f'hero-{theme}.svg').write_text(art,encoding='utf-8')
    mobile=art.replace('width="1200" height="440" viewBox="0 0 1200 440"','width="640" height="800" viewBox="0 0 640 800"').replace('width="1198" height="438"','width="638" height="798"').replace('<g id="network">','<g id="network" transform="translate(-570 345)">').replace('cx="925" cy="210"','cx="325" cy="560"')
    (OUT/f'hero-mobile-{theme}.svg').write_text(mobile,encoding='utf-8')

def workflow(theme,mobile=False):
    p=start(540 if mobile else 296,theme,'From curriculum to personalized feedback','Conceptual research workflow: structure curriculum, retrieve evidence, reason about learning gaps, and support the learner.')
    p += [text(36,42,'FROM STRUCTURE TO SUPPORT',12,'var(--accent)',600,'letter-spacing="2"'),text(1164,42,'RESEARCH WORKFLOW',10,extra='text-anchor="end" letter-spacing="1.6"')]
    items=[('01','Structure','Curriculum → knowledge graph','Concepts · prerequisites'),('02','Retrieve','Graph-grounded context','Neo4j · GraphRAG'),('03','Reason','Investigate learning gaps','Agentic workflows'),('04','Support','Personalized feedback','Educational applications')]
    for i,(num,title,sub,tag) in enumerate(items):
        x=36+(i%2 if mobile else i)*289
        p += [f'<g transform="translate(0 {230 if mobile and i>1 else 0})">']
        if i<3 and (not mobile or i%2==0):p += [f'<path class="flow" d="M{x+261} 164 h28" stroke="var(--accent)" stroke-width="2"/>']
        p += [f'<rect x="{x}" y="72" width="261" height="190" rx="16" fill="var(--bg)" stroke="var(--line)"/>',text(x+20,104,num,12,'var(--accent)',600),text(x+20,156,title,28,'var(--fg)',600),text(x+20,188,sub,12),f'<path d="M{x+20} 211 h221" stroke="var(--line)"/>',text(x+20,239,tag,11)]
        for j in range(3):p += [f'<circle cx="{x+205+j*10}" cy="100" r="2" fill="var(--accent)" opacity="{.25+j*.25}"/>']
        p += ['</g>']
    art=''.join(p)+'</svg>'
    if mobile:
        art=art.replace('width="1200" height="540" viewBox="0 0 1200 540"','width="622" height="540" viewBox="0 0 622 540"').replace('width="1198"','width="620"').replace('x="1164"','x="586"').replace('RESEARCH WORKFLOW','')
    (OUT/f'workflow-{"mobile-" if mobile else ""}{theme}.svg').write_text(art,encoding='utf-8')

def contact(theme,key,label,caption,icon):
    dark=theme=='dark'
    bg,fg,muted,line,accent=('#0b1220','#eef5ff','#96a9c3','#24344d','#69e1d4') if dark else ('#f5f8fc','#172b46','#546982','#d3ddeb','#087f80')
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="280" height="84" viewBox="0 0 280 84" role="img" aria-label="{escape(label)}">
<rect x="1" y="1" width="278" height="82" rx="14" fill="{bg}" stroke="{line}"/>
<rect x="15" y="22" width="40" height="40" rx="12" fill="{accent}" opacity=".1"/>
<g transform="translate(24 31)" fill="none" stroke="{accent}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{icon}</g>
<g font-family="Segoe UI,Arial,sans-serif"><text x="69" y="36" fill="{fg}" font-size="15" font-weight="600">{escape(label)}</text><text x="69" y="57" fill="{muted}" font-size="10.5">{escape(caption)}</text></g>
<path d="M250 31 h10 v10 m0 -10 -11 11" fill="none" stroke="{accent}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'''
    (OUT/f'contact-{key}-{theme}.svg').write_text(svg,encoding='utf-8')

for theme in ['dark','light']:
    hero(theme)
    workflow(theme)
    workflow(theme,True)
    contact(theme,'email','Email','chxnho@gmail.com','<rect x="1" y="3" width="20" height="15" rx="3"/><path d="m2 5 9 7 9-7"/>')
    contact(theme,'team','Indispensable AI','Explore the team','<circle cx="5" cy="6" r="3"/><circle cx="17" cy="6" r="3"/><path d="M0 19v-3a5 5 0 0 1 10 0v3m2 0v-3a5 5 0 0 1 10 0v3"/>')
    contact(theme,'repos','Repositories','Browse projects & code','<path d="M3 2h7l3 4h7v14H3z"/><path d="m9 11-3 3 3 3m6-6 3 3-3 3"/>')
print('Built fourteen SVG assets.')
