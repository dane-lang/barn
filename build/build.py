HTML_TEMPLATE = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n<title>40\' x 20\' Pole Barn — Construction Drawings v3</title>\n<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400&family=Poppins:wght@200;300;400&display=swap" rel="stylesheet">\n<style>\n:root{--cream:#FFFBBF;--ink:#333333;--ox:#7A1220;--pine:#0B5E3A;--navy:#1B2A47;--brown:#3D2314;--hair:#C6B667}\n*{box-sizing:border-box;margin:0}\nbody{font-family:Manrope,Poppins,Arial,sans-serif;font-weight:400;background:var(--cream);color:var(--ink)}\nheader{background:var(--navy);color:#fff;padding:28px 24px;border-bottom:3px solid var(--ink)}\nheader h1{font-family:Poppins;font-weight:300;font-size:26px}\nheader p{opacity:.85;margin-top:7px;font-size:14px;font-weight:300}\nheader .v{display:inline-block;margin-left:10px;padding:2px 9px;border:1px solid rgba(255,255,255,.55);font-size:13px;font-weight:400;vertical-align:middle}\nmain{max-width:1100px;margin:0 auto;padding:24px}\n.sheet{background:var(--cream);border:2px solid var(--navy);margin-bottom:26px;overflow:hidden;box-shadow:0 3px 12px rgba(61,35,20,.16)}\n.sheet h2{font-family:Poppins;font-size:15px;font-weight:300;padding:0 0 0 16px;min-height:44px;border-bottom:1px solid var(--hair);color:var(--navy);display:flex;align-items:center;justify-content:space-between;gap:10px}\n.sheet img,.sheet svg{display:block;width:100%;height:auto;cursor:zoom-in}\n.svgw{position:relative}\n.zh,.zx{color:#fff;border:0;font:400 13px Manrope,sans-serif;cursor:pointer;white-space:nowrap;flex:none;align-self:stretch;display:flex;align-items:center;justify-content:center;width:11%;min-width:92px}\n.zh{background:var(--pine)} .zx{background:var(--ox)}\n.zbar{position:fixed;top:0;left:0;right:0;height:46px;background:var(--cream);border-bottom:1px solid var(--hair);display:flex;align-items:center;justify-content:space-between;padding:0 0 0 14px;z-index:11}\n.zbar .t{font:400 15px Poppins,sans-serif;color:var(--navy);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}\nfooter{text-align:center;color:#e9e1d8;background:var(--brown);font-size:12px;font-weight:300;padding:20px}\n#zoom{position:fixed;inset:0;background:rgba(27,42,71,.94);display:none;overflow:auto;z-index:9;cursor:zoom-out;padding-top:46px}\n#zoom .svgw{min-width:1200px;width:160%;display:block;margin:0 auto;background:var(--cream)}\n#zoom .svgw>svg,#zoom .svgw>img{width:100%;height:auto;display:block}\n</style></head><body>\n<header><h1>40&#39; &times; 20&#39; Pole Barn <span class="v">v3</span></h1>\n<p>Construction drawing set &middot; schematic, not for permit &middot; 8&times;8 posts &middot; __CEIL__ ceiling target &middot; tap any sheet to zoom, tap again to return</p></header>\n<main>__BODY__</main>\n<div id="zoom" onclick="this.style.display=\'none\'"></div>\n<script>function Z(el){var sh=el.closest(\'.sheet\');if(!sh)return;var z=document.getElementById(\'zoom\');z.innerHTML=\'\';var t=sh.querySelector(\'h2\').firstChild.textContent;var bar=document.createElement(\'div\');bar.className=\'zbar\';bar.innerHTML=\'<span class="t"></span><span class="zx">close</span>\';bar.querySelector(\'.t\').textContent=t;var c=el.cloneNode(true);c.removeAttribute(\'onclick\');z.appendChild(bar);z.appendChild(c);z.style.display=\'block\';}</script>\n</body></html>'

REDIRECT = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">\n<title>Redirecting to v3</title>\n<link rel="canonical" href="https://dane-lang.github.io/barn/v3.html">\n<meta http-equiv="refresh" content="0; url=v3.html">\n<script>location.replace(\'v3.html\'+location.hash);</script>\n<style>body{font-family:Manrope,Arial,sans-serif;background:#FFFBBF;color:#333;padding:44px;font-weight:400}a{color:#7A1220}</style>\n</head><body><p>This drawing set has moved to <a href="v3.html">v3.html</a>. Redirecting&hellip;</p></body></html>'

import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen import *
from gen2 import *
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SHEETS = [('A-1 · Floor Plan', a1()), ('A-2 · Foundation & Post Layout', a2()),
          ('A-3 · Exterior Elevations', a3()), ('A-4 · Wall Girt Detail', a4()),
          ('A-5 · Roof Framing', a5()), ('A-6 · Connection Details', a6()),
          ('A-7 · Materials List', a7())]

# palette map: original tokens -> cream / charcoal / navy / oxblood / pine / brown
REMAP = [('#fff8e1','#FBF0B0'),('#e6c96a','#B98900'),('#dbe8f3','#E9EDF5'),('#eef1f4','#F3EAA0'),
 ('#f4f6f8','#FFFEF2'),('#f1eee6','#F3E9A6'),('#e3dccd','#EEDF9A'),('#e6d6b8','#EEDF9A'),('#c9a97a','#B98A4E'),
 ('#dde3e8','#C6B667'),('#8a8a8a','#6E6A55'),('#2b3f74','#1B2A47'),('#1470AF','#1B2A47'),
 ('#FF0000','#7A1220'),('#222','#333333'),('#ffffff','#FFFBBF'),('#fff','#FFFBBF'),('__PINE__','#0B5E3A')]

def process(svg):
    svg = re.sub(r'fill="#1470AF"([^>]*>[^<]*(?:FUTURE|future)[^<]*</text>)', r'fill="__PINE__"\1', svg)
    for a,b in REMAP: svg = svg.replace(a,b)
    for a,b in (('="800"','="300"'),('="700"','="400"'),('="600"','="400"'),('="500"','="400"')):
        svg = svg.replace('font-weight'+a, 'font-weight'+b)
    return svg

sheets = [(t, process(s)) for t,s in SHEETS]
body = ''.join(f'<div class="sheet"><h2>{esc(t)}<span class="zh" onclick="Z(this.closest(&quot;.sheet&quot;).querySelector(&quot;.svgw&quot;))">enlarge</span></h2><div class="svgw" onclick="Z(this)">{svg}</div></div>' for t,svg in sheets)

html = HTML_TEMPLATE.replace('__BODY__', body).replace('__CEIL__', ft(S['CEIL_TARGET']))
open(os.path.join(ROOT,'v3.html'),'w').write(html)
open(os.path.join(ROOT,'v2.html'),'w').write(REDIRECT)
print('v3.html', len(html.encode()), 'bytes')
