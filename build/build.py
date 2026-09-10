import base64, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen import *
from gen2 import *
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHEETS = os.path.join(ROOT, 'sheets'); OUT = os.path.join(ROOT, 'out'); os.makedirs(OUT, exist_ok=True)

def b64(path): return base64.b64encode(open(path, 'rb').read()).decode()

# H10S catalog illustration — crop from baseline A-6 (left panel image area)
im = Image.open(os.path.join(SHEETS, '05.png')); w, h = im.size
crop = im.crop((int(w * .04), int(h * .11), int(w * .40), int(h * .77)))
crop.convert('RGB').quantize(colors=64).save(os.path.join(OUT, 'h10s.png'), optimize=True)

# downsize truss refs (keep legible, cut weight)
for src, dst in (('06.png', 'truss-t02.png'), ('07.png', 'truss-t02ge.png')):
    im = Image.open(os.path.join(SHEETS, src)).convert('RGB'); im.thumbnail((1800, 1800)); im.quantize(colors=32).save(os.path.join(OUT, dst), optimize=True)

sheets = [
    ('A-1 · Floor Plan', a1()), ('A-2 · Foundation & Post Layout', a2()), ('A-3 · Exterior Elevations', a3()),
    ('A-4 · Wall Girt Detail', a4()), ('A-5 · Roof Framing', a5()), ('A-6 · Connection Details', a6(b64(os.path.join(OUT, 'h10s.png')))),
    ('A-7 · Materials List', a7()),
]
refs = [('REF · Kilby Truss T02 — FINK (×3)', b64(os.path.join(OUT, 'truss-t02.png'))),
        ('REF · Kilby Truss T02GE — GABLE END (×2)', b64(os.path.join(OUT, 'truss-t02ge.png')))]

body = ''.join(f'<div class="sheet"><h2>{esc(t)}<span class="zh" onclick="Z(this.closest(&quot;.sheet&quot;).querySelector(&quot;.svgw&quot;))">&#10530; enlarge</span></h2><div class="svgw" onclick="Z(this)">{svg}</div></div>' for t, svg in sheets)
body += ''.join(f'<div class="sheet"><h2>{esc(t)}<span class="zh" onclick="Z(this.closest(&quot;.sheet&quot;).querySelector(&quot;.svgw&quot;))">&#10530; enlarge</span></h2><div class="svgw" onclick="Z(this)"><img loading="lazy" src="data:image/png;base64,{b}" alt="{esc(t)}"></div></div>' for t, b in refs)

chg = f"""<div class="sheet chg"><h2>v2 · What changed from baseline</h2><div class="chgbody">
<p><b>Posts</b> 6x6 → <b>8x8</b>, all 14.</p>
<p><b>Post length</b> 14'-0" → <b>{ft(S['POST_LEN'])}</b>; embed {ft(S['EMBED'])} unchanged; {ft(S['AFG_SET'])} AFG as set.</p>
<p><b>Ceiling</b> 11'-0" → <b>{ft(S['CEIL_TARGET'])} target, {ft(S['CEIL_MIN'])} minimum</b>, cut to a level line by transit/laser after posts are set. Ceiling = grade to bottom of truss = cut post top.</p>
<p><b>Eave</b> 11'-0" → {ft(S['CEIL_TARGET'])}; <b>ridge</b> 17'-6" → {ft(S['RIDGE'])}.</p>
<p><b>Girts</b> count unchanged (4 field + sill). Sill held at 10'-0" to keep the 2' light slot; the added foot lands as a ~15" gap below the sill (A-4 note 6).</p>
<p><b>Datum</b> stated: 40'×20' is out-to-out of posts; wall plane = outside face; girts + metal outboard.</p>
<p><b>New</b> Sheet A-7 dry-in materials list (framing, walls, roof, doors, trim), quantities estimated from these dimensions. Electrical and interior excluded.</p>
<p><b>Open items</b> flagged on sheets: hole diameter for 8x8 + sleeve; H10S pattern on the wider face — confirm with Lyon / Simpson. Kilby truss references unchanged.</p>
</div></div>"""

html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>40' x 20' Agricultural Pole Barn — Construction Drawings v2</title>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{{--acc:{ACC};--ink:#222}}
*{{box-sizing:border-box;margin:0}}
body{{font-family:Manrope,Poppins,Arial,sans-serif;background:#f4f6f8;color:var(--ink)}}
header{{background:var(--acc);color:#fff;padding:28px 24px}}
header h1{{font-size:26px;font-weight:800}}
header p{{opacity:.85;margin-top:6px;font-size:14px}}
header .v{{display:inline-block;margin-left:10px;padding:2px 8px;border:1px solid rgba(255,255,255,.6);border-radius:0;font-size:13px;font-weight:700;vertical-align:middle}}
main{{max-width:1100px;margin:0 auto;padding:24px}}
.sheet{{background:#fff;border:1px solid #dde3e8;border-radius:0;margin-bottom:28px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,.06)}}
.sheet h2{{font-size:15px;font-weight:700;padding:0 0 0 16px;min-height:44px;border-bottom:1px solid #eef1f4;color:var(--acc);display:flex;align-items:center;justify-content:space-between;gap:10px}}
.sheet img,.sheet svg{{display:block;width:100%;height:auto;cursor:zoom-in}}
.svgw{{position:relative}}
.zh,.zx{{background:#FF0000;color:#fff;border:0;font:600 13px Manrope,sans-serif;border-radius:0;cursor:pointer;white-space:nowrap;flex:none;align-self:stretch;display:flex;align-items:center;justify-content:center;width:11%;min-width:88px}}
.zbar{{position:fixed;top:0;left:0;right:0;height:46px;background:#fff;border-bottom:1px solid #dde3e8;display:flex;align-items:center;justify-content:space-between;padding:0 0 0 14px;z-index:11}}
.zbar .t{{font:700 15px Manrope,sans-serif;color:var(--acc);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.chg h2{{color:#8a6d1a;background:#fff8e1}}
.chgbody{{padding:14px 16px;font-size:14px;line-height:1.5}} .chgbody p{{margin:0 0 6px}}
footer{{text-align:center;color:#8a8a8a;font-size:12px;padding:20px}}
footer a{{color:var(--acc)}}
#zoom{{position:fixed;inset:0;background:rgba(20,20,20,.92);display:none;overflow:auto;z-index:9;cursor:zoom-out;padding-top:46px}}
#zoom .svgw{{min-width:1200px;width:160%;display:block;margin:0 auto;background:#fff}}
#zoom .svgw>svg,#zoom .svgw>img{{width:100%;height:auto;display:block}}
</style></head><body>
<header><h1>40&#39; &times; 20&#39; Agricultural Pole Barn <span class="v">v2</span></h1>
<p>Construction drawing set &middot; Mountain City, TN &middot; schematic, not for permit &middot; 8x8 posts &middot; {ft(S['CEIL_TARGET'])} ceiling target &middot; tap any sheet to zoom &middot; tap again to return</p></header>
<main>{body}</main>
<div id="zoom" onclick="this.style.display='none'"></div>
<script>function Z(el){{var sh=el.closest('.sheet');if(!sh)return;var z=document.getElementById('zoom');z.innerHTML='';var t=sh.querySelector('h2').firstChild.textContent;var bar=document.createElement('div');bar.className='zbar';bar.innerHTML='<span class="t"></span><span class="zx">&#10005; close</span>';bar.querySelector('.t').textContent=t;var c=el.cloneNode(true);c.removeAttribute('onclick');z.appendChild(bar);z.appendChild(c);z.style.display='block';}}</script>
</body></html>"""
open(os.path.join(OUT, 'v2.html'), 'w').write(html)
for t, svg in sheets: open(os.path.join(OUT, t.split(' ')[0].lower() + '.svg'), 'w').write(svg)
print('v2.html', len(html.encode()), 'bytes')
