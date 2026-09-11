"""
barn drawing-set generator — v2
Emits v2.html: six SVG sheets (A-1..A-6) + A-7 materials list + two the truss mfr truss reference PNGs.
Every dimension is derived from the SPEC block below. Change a number there, re-run, re-push.
"""
import base64, os, html as H

# ───────────────────────── SPEC (single source of truth) ─────────────────────────
S = dict(
    L=40.0, W=20.0,            # out-to-out of posts, ft
    BAY=10.0,                  # post o.c., ft
    POST_IN=7.25,              # 8x8 actual, in
    POST_LEN=16.0,             # purchased post, ft
    EMBED=3.0,                 # ft below grade
    AFG_SET=13.0,              # as set, ft (POST_LEN-EMBED)
    CEIL_TARGET=12.0,          # cut-to target AFG, ft = bottom of truss
    CEIL_MIN=11.0,             # absolute minimum, ft
    PITCH=6, SPAN=20.0,        # 6:12 on 20' span
    RISE=6.5,                  # ft eave->ridge incl. heel (per the truss mfr T02)
    EAVE_OH=2.0,               # ft
    GIRT_OC=2.0,               # ft
    HOLE_IN=18, PAD='precast',
    RJ_OC=10.4583,             # 10'-5 1/2" roll-up jamb o.c.
    RU_W=10.0, RU_H=9.0,       # roll-up clear
    MD_W=3.0, MD_H=6.667,      # 36" man door
)
S['RIDGE'] = S['CEIL_TARGET'] + S['RISE']
S['TRIM']  = S['AFG_SET'] - S['CEIL_TARGET']
S['NBAYS'] = int(S['L'] / S['BAY'])
S['POST_FT'] = S['POST_IN'] / 12
S['GIRT_ROWS'] = 5            # 4 field girts @24" from splash + sill girt at 10'-0" (light slot above)
S['SILL_AFG'] = 10.0

ACC = '#1470AF'; INK = '#222'; NAVY = '#2b3f74'; TAN = '#c9a97a'; TAN2 = '#e6d6b8'
STONE = '#e3dccd'; GRAY = '#8a8a8a'; LITE = '#f4f6f8'; RULE = '#dde3e8'; BLUE = ACC
SRED = '#FF0000'   # alert / not-for-permit accent
SHW, SHH = 1340, 820

def ft(v):
    """decimal feet -> 12'-5½\" style"""
    neg = v < 0; v = abs(v)
    f = int(v); i = round((v - f) * 12 * 4) / 4
    if i >= 12: f += 1; i -= 12
    fr = {0.25: '¼', 0.5: '½', 0.75: '¾'}.get(i % 1, '')
    inch = int(i)
    s = f"{f}'-{inch}{fr}\""
    return ('-' if neg else '') + s

def esc(t): return H.escape(str(t), quote=True)

def T(x, y, s, size=11, w=400, fill=INK, anchor='start', fam='Manrope', extra=''):
    return (f'<text x="{x}" y="{y}" font-family="{fam},Poppins,Arial" font-size="{size}" '
            f'font-weight="{w}" fill="{fill}" text-anchor="{anchor}" {extra}>{esc(s)}</text>')

def line(x1, y1, x2, y2, st=INK, w=1, dash=''):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{st}" stroke-width="{w}"{d}/>'

def rect(x, y, w, h, fill='none', st=INK, sw=1, rx=0, extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{st}" stroke-width="{sw}" rx="{rx}" {extra}/>'

def dimH(x1, x2, y, label, tick=6, above=True, size=10, color=INK):
    """horizontal dimension line with extension ticks"""
    ty = y - 4 if above else y + 12
    return ''.join([
        line(x1, y, x2, y, color, 1),
        line(x1, y - tick, x1, y + tick, color, 1),
        line(x2, y - tick, x2, y + tick, color, 1),
        T((x1 + x2) / 2, ty, label, size, 600, color, 'middle')])

def dimV(y1, y2, x, label, tick=6, left=True, size=10, color=INK):
    tx = x - 6 if left else x + 6
    anc = 'end' if left else 'start'
    return ''.join([
        line(x, y1, x, y2, color, 1),
        line(x - tick, y1, x + tick, y1, color, 1),
        line(x - tick, y2, x + tick, y2, color, 1),
        T(tx, (y1 + y2) / 2 + 4, label, size, 600, color, anc)])

def sheet(num, title, sub, body, foot_left, n_of):
    """wrap a sheet body in the standard chrome"""
    return f'''<svg viewBox="0 0 {SHW} {SHH}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(title)}">
<rect width="{SHW}" height="{SHH}" fill="#fff"/>
<rect width="{SHW}" height="52" fill="{ACC}"/>
{T(24, 34, "40' × 20' AGRICULTURAL POLE BARN", 22, 700, '#fff', 'start', 'Poppins')}
{T(SHW-24, 24, f'SHEET {num}', 15, 700, '#fff', 'end', 'Poppins')}
{T(SHW-24, 42, sub, 11, 400, '#dbe8f3', 'end')}
{body}
<rect y="{SHH-40}" width="{SHW}" height="40" fill="#eef1f4"/>
{T(24, SHH-15, foot_left, 11, 700, SRED)}
{T(SHW-24, SHH-15, f'Drawing {n_of} · {title}', 11, 400, GRAY, 'end')}
</svg>'''

def note_box(x, y, w, h, title, lines, fill='#fff', st=RULE, tcolor=INK, size=11, lh=17, tfill=None):
    out = [rect(x, y, w, h, fill, st, 1, 2)]
    out.append(T(x + 14, y + 22, title, 12, 700, tfill or INK))
    yy = y + 44
    for ln in lines:
        w_ = 400; c = tcolor
        if isinstance(ln, tuple): ln, w_, c = ln
        out.append(T(x + 14, yy, ln, size, w_, c)); yy += lh
    return ''.join(out)

# ───────────────────────── A-1 FLOOR PLAN ─────────────────────────
def a1():
    sc = 20                           # px per ft
    ox, oy = 250, 150                 # plan origin (outside face, top-left)
    L, W = S['L'], S['W']
    px = S['POST_FT'] * sc            # post drawn size
    Xr, Yb = ox + L * sc, oy + W * sc
    o = []
    # floor (post-face rectangle) + siding line OUTBOARD on all four walls
    sd = 4
    mid0 = oy + W * sc / 2; ru0 = S['RU_W'] * sc
    Xr0, Yb0 = ox + L * sc, oy + W * sc
    # siding line: continuous on top, bottom, REAR (sided over); broken at the FRONT roll-up opening
    o.append(f'<path d="M{ox-sd} {mid0-ru0/2} L{ox-sd} {oy-sd} L{Xr0+sd} {oy-sd} L{Xr0+sd} {Yb0+sd} L{ox-sd} {Yb0+sd} L{ox-sd} {mid0+ru0/2}" fill="none" stroke="{INK}" stroke-width="2"/>')
    o.append(rect(ox, oy, L * sc, W * sc, '#f1eee6', GRAY, 0.75, extra='stroke-dasharray="3 3"'))
    o.append(T(ox + L * sc / 2, oy - sd - 6, 'B&B steel siding over girts — OUTSIDE face of posts, all four walls', 8.5, 400, GRAY, 'middle'))
    # posts — sidewalls at 10' o.c., datum = outside face
    def post(cx, cy, tag=''):
        o.append(rect(cx - px / 2, cy - px / 2, px, px, INK, INK))
        if tag: o.append(f'<circle cx="{cx}" cy="{cy}" r="10" fill="none" stroke="{BLUE}" stroke-width="2"/>')
    for i in range(S['NBAYS'] + 1):
        x = ox + i * S['BAY'] * sc
        cx_ = x - px / 2 if i == S['NBAYS'] else x + px / 2      # rear corner posts sit INSIDE the 40' line
        post(cx_, oy + px / 2); post(cx_, Yb - px / 2)
    # roll-up jamb posts, front (left) + rear (right, future)
    mid = oy + W * sc / 2
    for yy in (mid - S['RJ_OC'] * sc / 2, mid + S['RJ_OC'] * sc / 2):
        post(ox + px / 2, yy, 'RJ'); post(Xr - px / 2, yy, 'RJ')
    # roll-up openings
    ru = S['RU_W'] * sc
    o.append(rect(ox - 4, mid - ru / 2, 8, ru, '#fff', 'none'))                     # RO breaks the wall — same rule as man doors
    o.append(line(ox - 7, mid - ru / 2, ox + 7, mid - ru / 2, INK, 2))              # jamb ticks
    o.append(line(ox - 7, mid + ru / 2, ox + 7, mid + ru / 2, INK, 2))
    o.append(f'<line x1="{ox}" y1="{mid-ru/2+4}" x2="{ox}" y2="{mid+ru/2-4}" stroke="{BLUE}" stroke-width="2.5" stroke-dasharray="6 4"/>')   # curtain OVERHEAD — dashed at RO
    o.append(T(ox - sd - 12, mid, "A · 10'×9' ROLL-UP", 10, 700, BLUE, 'middle', extra=f'transform="rotate(-90 {ox-sd-12} {mid})"'))
    o.append(f'<rect x="{Xr+sd+2}" y="{mid-ru/2}" width="4" height="{ru}" fill="none" stroke="{BLUE}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    o.append(T(Xr + sd + 22, mid - ru / 2 - 6, 'siding CONTINUOUS here — RO sided over', 8, 400, GRAY, 'middle', extra=f'transform="rotate(90 {Xr+sd+22} {mid-ru/2-6})"'))
    o.append(T(Xr + sd + 32, mid, "D · FUTURE ROLL-UP", 10, 700, BLUE, 'middle', extra=f'transform="rotate(90 {Xr+sd+32} {mid})"'))
    # man doors — ENDWALLS (match A-3 + baseline): B front-left, C rear-right, 12" from workbench corner, OUTSWING
    md = S['MD_W'] * sc
    y2 = Yb - 1 * sc          # hinge jamb — corner side
    y1 = y2 - md              # latch jamb
    for (wx, sw) in ((ox, -1), (Xr, 1)):
        o.append(rect(wx - 4, y1, 8, md, '#fff', 'none'))              # RO breaks the wall
        o.append(line(wx - 7, y1, wx + 7, y1, INK, 2))                 # jamb ticks
        o.append(line(wx - 7, y2, wx + 7, y2, INK, 2))
        o.append(line(wx, y2, wx + sw * md, y2, INK, 2))               # leaf shown OPEN — swung OUTSIDE
        o.append(f'<path d="M{wx} {y1} A{md} {md} 0 0 {1 if sw>0 else 0} {wx + sw*md} {y2}" fill="none" stroke="{GRAY}" stroke-dasharray="3 3"/>')
    o.append(T(ox - md / 2, y1 - 8, 'B', 10, 700, INK, 'middle')); o.append(T(Xr + md / 2, y1 - 8, 'C', 10, 700, INK, 'middle'))
    # HVLS fan + high bays
    cx, cy = ox + L * sc / 2, mid
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{4.5*sc}" fill="none" stroke="{GRAY}" stroke-dasharray="5 4"/>')
    o.append(T(cx, cy - 4, "9' HVLS FAN", 11, 700, GRAY, 'middle')); o.append(T(cx, cy + 12, "ctr 20'×10' · ceiling plan", 9, 400, GRAY, 'middle'))
    for hx in (ox + 7 * sc, cx, Xr - 7 * sc):
        for hy in (oy + 5 * sc, Yb - 5 * sc):
            o.append(f'<circle cx="{hx}" cy="{hy}" r="9" fill="none" stroke="{GRAY}" stroke-dasharray="2 2"/>'); o.append(T(hx, hy + 3, 'HB', 7, 700, GRAY, 'middle'))
    # workbench
    bx, bw = ox + 5 * sc, 30 * sc
    o.append(rect(bx, Yb - 1.5 * sc, bw, 1.5 * sc, TAN2, TAN, 1))
    o.append(T(bx + bw / 2, Yb - 0.6 * sc, 'WORKBENCH · 30\' · 2x4 & ¾" ply', 11, 700, INK, 'middle'))
    for rx_ in (bx, bx + 7.5 * sc, bx + 15 * sc, bx + 22.5 * sc, bx + bw):
        o.append(f'<circle cx="{rx_}" cy="{Yb}" r="6" fill="#fff" stroke="{INK}"/>')
    # switches
    for sx in (ox + 26, Xr - 26):
        o.append(f'<circle cx="{sx}" cy="{y2 - md/2}" r="7" fill="#fff" stroke="{INK}"/>'); o.append(T(sx, y2 - md / 2 + 3, 'S3', 7, 700, INK, 'middle'))
    # dimensions — top
    o.append(dimH(ox, Xr, oy - 60, ft(L), size=11))
    for i in range(S['NBAYS']):
        o.append(dimH(ox + i * S['BAY'] * sc, ox + (i + 1) * S['BAY'] * sc, oy - 35, ft(S['BAY'])))
    o.append(T(Xr + 8, oy - 31, 'o.c. both sidewalls · outside face of post', 9, 400, GRAY))
    # right
    o.append(dimV(oy, Yb, Xr + 62, ft(W), left=False, size=11))
    # left — post c/c + openings
    e = (W - S['RJ_OC']) / 2
    o.append(T(ox - 155, oy - 18, 'post c/c', 9, 400, GRAY, 'middle')); o.append(T(ox - 95, oy - 18, 'openings', 9, 400, GRAY, 'middle'))
    o.append(dimV(oy, oy + e * sc, ox - 155, ft(e), left=True))
    o.append(dimV(oy + e * sc, Yb - e * sc, ox - 155, ft(S['RJ_OC']), left=True))
    o.append(dimV(Yb - e * sc, Yb, ox - 155, ft(e), left=True))
    o.append(dimV(mid - ru / 2, mid + ru / 2, ox - 95, "10'-0\" clr", left=True))
    o.append(dimV(Yb - 1 * sc - md, Yb - 1 * sc, ox - 95, "3'-0\"", left=True))
    o.append(dimV(Yb - 1 * sc, Yb, ox - 95, "1'-0\"", left=True))
    # bottom
    yb2 = Yb + 40
    o.append(dimH(ox, bx, yb2, "5'-0\"")); o.append(dimH(bx, bx + bw, yb2, "30'-0\" bench")); o.append(dimH(bx + bw, Xr, yb2, "5'-0\""))
    yb3 = Yb + 66
    for (a, b, lab) in ((0, 7, "7'-0\""), (7, 20, "13'-0\""), (20, 33, "13'-0\""), (33, 40, "7'-0\"")):
        o.append(dimH(ox + a * sc, ox + b * sc, yb3, lab))
    o.append(T(cx, Yb + 90, "light columns (fan centered at 20'-0\")", 9, 400, GRAY, 'middle'))
    # openings box
    o.append(note_box(ox + 12, oy + 8, 400, 107, 'OPENINGS', [
        "A · 10'×9' roll-up door — RO 10'-0\"w, 2 jamb posts @ 10'-5½\" o.c.",
        'B · 36" man door — FRONT endwall, OUTSWING, 12" fr corner (2x jambs)',
        'C · 36" man door — REAR endwall, OUTSWING (geom = B mirrored, 2x jambs)',
        ('B/C hinges face OUTSIDE — NRP pins · stainless/coated hardware', 700, INK),
        ("D · FUTURE 10'×9' roll-up — RO framed & sided over (rear, ctr)", 700, BLUE)], size=10, lh=15))
    # legend
    lx, ly = Xr + 112, oy
    o.append(rect(lx, ly, 150, 232, '#fff', RULE)); o.append(T(lx + 14, ly + 22, 'LEGEND', 12, 700))
    o.append(rect(lx + 16, ly + 34, 10, 10, INK, INK)); o.append(T(lx + 36, ly + 43, '8x8 post', 10))
    o.append(f'<circle cx="{lx+21}" cy="{ly+62}" r="5" fill="#fff" stroke="{INK}"/>'); o.append(T(lx + 36, ly + 66, 'receptacle', 10))
    o.append(f'<circle cx="{lx+21}" cy="{ly+86}" r="6" fill="#fff" stroke="{INK}"/>'); o.append(T(lx + 36, ly + 90, '3-way switch', 10))
    o.append(f'<circle cx="{lx+21}" cy="{ly+110}" r="6" fill="none" stroke="{GRAY}" stroke-dasharray="2 2"/>'); o.append(T(lx + 36, ly + 114, 'high bay (ceiling)', 10))
    o.append(f'<circle cx="{lx+21}" cy="{ly+134}" r="6" fill="none" stroke="{GRAY}" stroke-dasharray="4 3"/>'); o.append(T(lx + 36, ly + 138, 'fan (ceiling)', 10))
    o.append(f'<path d="M{lx+15} {ly+165} A10 10 0 0 1 {lx+25} {ly+155}" fill="none" stroke="{GRAY}" stroke-dasharray="2 2"/>'); o.append(T(lx + 36, ly + 162, 'door swing', 10))
    o.append(line(lx + 14, ly + 178, lx + 30, ly + 178, BLUE, 2.5, '6 4')); o.append(T(lx + 36, ly + 182, 'roll-up (curtain o/h)', 10))
    o.append(line(lx + 14, ly + 196, lx + 30, ly + 196, BLUE, 2, '4 3')); o.append(T(lx + 36, ly + 200, 'roll-up (future)', 10))
    o.append(rect(lx, ly, 150, 232, 'none', RULE)); o.append(line(lx + 14, ly + 214, lx + 30, ly + 214, INK, 1.5)); o.append(T(lx + 36, ly + 218, 'siding (outboard)', 10))
    # datum note (new in v2)
    o.append(note_box(lx, ly + 246, 150, 150, 'DATUM — v2', [
        ('40\'×20\' is OUT-TO-OUT', 700, ACC), ('of posts. Girts + metal', 400, INK), ('sit on the OUTSIDE face,', 400, INK),
        ('so the wall plane is the', 400, INK), ('post face. 8x8 posts take', 400, INK), ('2" of clear per wall vs', 400, INK), ('the 6x6 baseline.', 400, INK)],
        fill='#fff8e1', st='#e6c96a', size=10, lh=14, tfill=ACC))
    # foot notes
    ny = Yb + 118
    for i, s_ in enumerate([
        "5 GFCI receptacles — one at each bench end + ~8' o.c. between (nailer board for backing where no post), ~42\" AFF, two 20A alt · 6 high bays: 3 cols × 2 rows @ 5'-0\" off each sidewall",
        "SIDEWALL A (bottom): continuous screened vent slot in top 2' of wall above · S3 at each man door · man doors framed with 2x jamb studs",
        "FRONT ENDWALL = left · BACK ENDWALL = right · posts 10'-0\" o.c. outside-face-to-outside-face · 4 roll-up jamb posts circled (front installed, rear future)"]):
        o.append(T(cx, ny + i * 17, s_, 9.5, 400, GRAY if i else INK, 'middle'))
    return sheet('A-1', 'Floor Plan', 'FLOOR PLAN & ELECTRICAL', ''.join(o),
                 'SCHEMATIC — NOT FOR PERMIT · DIMENSIONS GOVERN, DO NOT SCALE', '1 of 7')

# ───────────────────────── A-2 FOUNDATION & POST ─────────────────────────
def a2():
    o = []
    sc = 13; ox, oy = 110, 150; L, W = S['L'], S['W']
    px = S['POST_FT'] * sc; Xr, Yb = ox + L * sc, oy + W * sc
    o.append(T(ox, 92, 'POST LAYOUT PLAN', 13, 700))
    sd = 3
    o.append(rect(ox - sd, oy - sd, L * sc + 2 * sd, W * sc + 2 * sd, 'none', INK, 1.5))
    o.append(rect(ox, oy, L * sc, W * sc, '#f1eee6', GRAY, 0.75, extra='stroke-dasharray="3 3"'))
    o.append(T(ox + L * sc / 2, Yb + 14, 'outer line = siding, outboard of post faces all four walls · dashed = post-face / layout line', 8, 400, GRAY, 'middle'))
    def post(cx, cy, rj=False):
        o.append(rect(cx - px / 2, cy - px / 2, px, px, INK, INK))
        if rj: o.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="none" stroke="{BLUE}" stroke-width="2"/>')
    for i in range(S['NBAYS'] + 1):
        x = ox + i * S['BAY'] * sc; cx_ = x - px / 2 if i == S['NBAYS'] else x + px / 2
        post(cx_, oy + px / 2); post(cx_, Yb - px / 2)
    mid = oy + W * sc / 2
    for yy in (mid - S['RJ_OC'] * sc / 2, mid + S['RJ_OC'] * sc / 2):
        post(ox + px / 2, yy, True); post(Xr - px / 2, yy, True); o.append(T(ox + 16, yy + 4, 'RJ', 8, 700, BLUE)); o.append(T(Xr - 26, yy + 4, 'RJ', 8, 700, BLUE))
    o.append(T(ox + L * sc / 2, mid + 4, '8x8 posts typ. · 14 total · 16\'-0" long', 11, 400, GRAY, 'middle'))
    # datum flag
    o.append(f'<path d="M{ox-4} {oy-4} l-16 -12 l4 16 z" fill="{BLUE}"/>'); o.append(T(ox - 40, oy - 24, 'DATUM', 9, 700, INK, 'middle')); o.append(T(ox - 40, oy - 12, 'lay out from here', 8, 400, GRAY, 'middle')); o.append(T(ox - 40, oy - 2, 'outside face', 8, 400, GRAY, 'middle'))
    o.append(dimH(ox, Xr, oy - 40, ft(L)))
    for i in range(S['NBAYS']): o.append(dimH(ox + i * S['BAY'] * sc, ox + (i + 1) * S['BAY'] * sc, oy - 22, ft(S['BAY'])))
    o.append(dimV(oy, Yb, Xr + 40, ft(W), left=False))
    e = (W - S['RJ_OC']) / 2
    o.append(dimV(oy, oy + e * sc, ox - 50, ft(e))); o.append(dimV(oy + e * sc, Yb - e * sc, ox - 50, ft(S['RJ_OC']))); o.append(dimV(Yb - e * sc, Yb, ox - 50, ft(e)))
    # section cut marker
    cxm = ox + L * sc / 2
    o.append(line(cxm, Yb - 10, cxm, Yb + 28, BLUE, 1, '4 3')); o.append(f'<circle cx="{cxm}" cy="{Yb+40}" r="10" fill="#fff" stroke="{BLUE}" stroke-width="1.5"/>'); o.append(T(cxm, Yb + 44, '2', 10, 700, BLUE, 'middle'))
    o.append(T(ox + L * sc / 2, Yb + 68, "RJ = roll-up jamb posts (10'-5½\" o.c.) — front installed, rear future · posts 10'-0\" o.c. outside face", 9.5, 400, GRAY, 'middle'))

    # ── post-in-ground section (THE v2 change) ──
    sx0, gy = 960, 462          # ground line y
    ssc = 25                    # px per ft vertical
    o.append(T(760, 92, 'POST-IN-GROUND SECTION', 13, 700)); o.append(T(760, 108, 'detail 2 · typical field post (jamb posts same, sized per engineering)', 9.5, 400, GRAY))
    pw = 8 / 12 * ssc            # 8" face at true scale = 16.7px
    top_set = gy - S['AFG_SET'] * ssc; top_cut = gy - S['CEIL_TARGET'] * ssc; top_min = gy - S['CEIL_MIN'] * ssc; bot = gy + S['EMBED'] * ssc
    # earth
    o.append(rect(sx0 - 200, gy, 380, S['EMBED'] * ssc + 20, '#f3efe5', 'none'))
    o.append(f'<pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="8" stroke="#c8bfa8" stroke-width="1"/></pattern>')
    o.append(rect(sx0 - 200, gy, 380, S['EMBED'] * ssc + 20, 'url(#hatch)', 'none'))
    o.append(line(sx0 - 220, gy, sx0 + 200, gy, INK, 1.5)); o.append(T(sx0 + 60, gy - 6, 'finished grade (top of pad)', 9, 400, GRAY))
    # hole + collar + pad
    hw = S['HOLE_IN'] / 12 * ssc  # 18" hole at true scale = 37.5px
    o.append(rect(sx0 - hw / 2, gy, hw, S['EMBED'] * ssc, '#e2e6ea', INK, 1))
    o.append(rect(sx0 - hw / 2 + 3, gy + 0.17 * ssc, hw - 6, S['EMBED'] * ssc - 0.17 * ssc - 8, '#d0d5db', 'none'))
    o.append(rect(sx0 - hw / 2 - 8, bot - 8, hw + 16, 12, '#b9bec4', INK, 1)); o.append(T(sx0 - hw / 2 - 14, bot + 2, 'precast concrete footing pad', 9, 400, INK, 'end'))
    # post: trim zone above cut
    o.append(rect(sx0 - pw / 2, top_cut, pw, bot - top_cut, TAN, INK, 1))
    o.append(rect(sx0 - pw / 2, top_set, pw, top_cut - top_set, '#f0e4cc', INK, 1, extra='stroke-dasharray="4 3"'))
    # poly sleeve
    o.append(rect(sx0 - pw / 2 - 2, gy - 6, pw + 4, S['EMBED'] * ssc - 8, 'none', BLUE, 1.5))
    # truss bearing marker
    o.append(f'<path d="M{sx0-24} {top_cut} L{sx0} {top_cut-14} L{sx0+24} {top_cut} z" fill="#fff" stroke="{INK}" stroke-width="1"/>')
    o.append(T(sx0 + 30, top_cut - 6, 'truss bears here', 8.5, 400, GRAY))
    # cut line + min line
    o.append(line(sx0 - 60, top_cut, sx0 + 60, top_cut, ACC, 2)); o.append(T(sx0 - 66, top_cut + 4, 'CUT LINE — level by transit / laser', 9.5, 700, ACC, 'end'))
    o.append(line(sx0 - 60, top_min, sx0 + 60, top_min, '#c0392b', 1, '5 3')); o.append(T(sx0 - 66, top_min + 4, "11'-0\" absolute minimum", 9, 600, '#c0392b', 'end'))
    o.append(line(sx0 - 60, top_set, sx0 + 60, top_set, GRAY, 1, '3 3')); o.append(T(sx0 - 66, top_set + 4, "as set — 13'-0\" AFG, uncut", 9, 400, GRAY, 'end'))
    # dims (right stack)
    dx = sx0 + 190
    o.append(dimV(top_cut, gy, dx, ft(S['CEIL_TARGET']) + ' AFG', left=False, size=11, color=ACC))
    o.append(T(dx + 8, (top_cut + gy) / 2 + 18, 'target ceiling', 8.5, 400, ACC)); o.append(T(dx + 8, (top_cut + gy) / 2 + 30, '= bottom of truss', 8.5, 400, ACC))
    o.append(dimV(top_set, top_cut, dx, ft(S['TRIM']) + ' trim', left=False, size=10, color=GRAY))
    o.append(dimV(gy, bot, dx, ft(S['EMBED']) + ' embed', left=False, size=11))
    o.append(dimV(top_set, bot, dx + 80, ft(S['POST_LEN']) + ' post', left=False, size=11, color=INK))
    # labels left
    o.append(T(sx0 - hw / 2 - 14, gy + 14, 'concrete collar (top 2" b.g.)', 9, 400, INK, 'end'))
    o.append(T(sx0 - hw / 2 - 14, gy - 10, f'~{S["HOLE_IN"]}" dia hole — verify for 8x8 + sleeve', 9, 400, INK, 'end'))
    o.append(rect(sx0 + 50, gy + 14, 130, 34, '#eaf3fb', BLUE, 1, 3)); o.append(T(sx0 + 58, gy + 28, 'HDPE POST SLEEVE', 9.5, 700, ACC)); o.append(T(sx0 + 58, gy + 41, '~60-mil rigid, full base', 8.5)); o.append(line(sx0 + 50, gy + 30, sx0 + pw / 2 + 2, gy + 20, BLUE, 1))
    o.append(T(sx0 + 30, top_set - 12, "8x8 × 16'-0\" post (as purchased)", 10, 700, INK))

    # ── floor buildup — true section, SAME 25 px/ft scale + visual system as Post-in-Ground Section ──
    fx, fy = 110, 566
    fsc = 25                    # px per ft vertical — matches ssc above
    o.append(T(fx, fy - 6, 'FLOOR BUILDUP — RAISED PAD', 13, 700))
    o.append(T(fx, fy + 10, 'perimeter section at a post · same scale as Post-in-Ground Section', 9.5, 400, GRAY))
    o.append(T(fx, fy + 26, 'FINISHED FLOOR 4"–6" ABOVE exterior grade · taper gravel to grade at door openings', 9, 700, INK))
    px0 = fx + 110              # post left face
    pw2 = 8 / 12 * fsc          # 8" face at true scale — matches section
    gly = fy + 84               # exterior grade line
    ffy = gly - 5 / 12 * fsc    # finished floor ~5" above grade; gravel 4" thick crowns just above grade
    bot2 = gly + S['EMBED'] * fsc          # 3'-0" embed to scale
    # earth below grade — same fill + hatch
    o.append(rect(fx, gly, 480, S['EMBED'] * fsc + 12, '#f3efe5', 'none'))
    o.append(rect(fx, gly, 480, S['EMBED'] * fsc + 12, 'url(#hatch)', 'none'))
    # hole + collar around post — same greys as section
    hw2 = S['HOLE_IN'] / 12 * fsc # 18" hole at true scale
    o.append(rect(px0 + pw2 / 2 - hw2 / 2, gly, hw2, S['EMBED'] * fsc, '#e2e6ea', INK, 1))
    o.append(rect(px0 + pw2 / 2 - hw2 / 2 + 3, gly + 4, hw2 - 6, S['EMBED'] * fsc - 12, '#d0d5db', 'none'))
    # HDPE sleeve — blue outline, same as section
    o.append(rect(px0 - 2, gly - 4, pw2 + 4, S['EMBED'] * fsc - 4, 'none', BLUE, 1.2))
    # post — continuous, breaks UP (it runs 12' AFG), full embed to footing pad
    o.append(rect(px0, fy + 42, pw2, bot2 - (fy + 42), TAN, INK, 1))
    o.append(f'<path d="M{px0} {fy+38} l6 -4 l7 8 l7 -8 l6 4" stroke="{INK}" stroke-width="1" fill="none"/>')
    o.append(T(px0 + pw2 + 8, fy + 46, "8x8 post continues up — 12'-0\" AFG", 8.5, 400, GRAY))
    # footing pad — same grey block as section
    o.append(rect(px0 - 8, bot2 - 2, pw2 + 16, 10, '#b9bec4', INK, 1))
    o.append(T(px0 - 4, bot2 + 20, 'precast footing pad', 8.5, 400, INK))
    # splash plank on exterior face — treated 2x10 on edge, retains gravel
    o.append(rect(px0 - 3.1, gly - 19.3, 3.1, 19.3, INK, INK))   # 1.5" x 9.25" actual, to scale
    o.append(T(px0 - 8, gly - 24, 'treated 2x10 splash plank', 8.5, 400, TAN, 'end'))
    # gravel band — interior of post, 4" thick, floor 4"–6" above grade
    o.append(rect(px0 + pw2, ffy, fx + 470 - (px0 + pw2), gly - ffy, '#e2e6ea', INK, 1))
    o.append(T(px0 + pw2 + 170, ffy - 5, '4" CLEAN GRAVEL — compacted, crowned', 9, 700, INK, 'middle'))
    # exterior grade line
    o.append(line(fx - 10, gly, px0, gly, INK, 1.5)); o.append(T(fx + 2, gly - 5, 'exterior grade', 8.5, 400, GRAY))
    o.append(f'<path d="M{fx+2} {gly+14} L{fx+26} {gly+2}" stroke="{INK}" fill="none"/>')
    # embed dim — exterior side (right corridor is occupied by framing notes)
    o.append(dimV(gly, bot2, fx + 40, "3'-0\"", left=False, size=9))
    o.append(T(fx + 48, (gly + bot2) / 2 + 16, 'embed', 8, 400, INK))
    # clay label
    o.append(T(px0 + pw2 + 190, gly + 44, 'GRADED NATIVE CLAY — no structural fill needed', 8.5, 700, GRAY, 'middle'))
    o.append(T(px0 + pw2 + 190, gly + 57, '(site clay is dense-bearing)', 8.5, 400, GRAY, 'middle'))
    # floor height label — right of gravel band, clear of framing notes box
    o.append(T(fx + 486, ffy + 4, '4"–6"', 9, 700, INK))
    o.append(T(fx, fy + 197, "grade slopes away — 5% min. first 10'", 8.5, 400, GRAY))
    o.append(T(fx, fy + 213, 'NO geotextile · NO vapor barrier — raised pad + positive drainage do the work', 10, 700, ACC))

    # ── framing notes ──
    o.append(note_box(640, 560, 670, 218, 'FRAMING NOTES', [
        ('1. Lay out all posts from the DATUM corner, outside face; do not chain-measure hole to hole.', 400, INK),
        (f"2. All holes {ft(S['EMBED'])} deep. Post purchased {ft(S['POST_LEN'])} (8x8), set {ft(S['EMBED'])} in concrete collar on precast pad — {ft(S['AFG_SET'])} AFG as set.", 400, INK),
        (f"3. CEILING: set posts plumb & true, cure, then CUT ALL POST TOPS to one LEVEL LINE by transit/laser at {ft(S['CEIL_TARGET'])} AFG target.", 700, ACC),
        (f"   Absolute minimum {ft(S['CEIL_MIN'])} AFG. Never cut to a fixed length — the level line governs; ~1' trim absorbs grade variation.", 700, ACC),
        ('4. Trusses bear directly on cut post tops @ 10\' o.c. Ceiling height = grade to bottom of truss = cut post top.', 400, INK),
        ('5. Rigid HDPE post sleeve (~60-mil) on every post base before the pour — isolates timber from concrete & moisture.', 400, INK),
        ('6. Collar to 2" b.g., level & plumb, brace — cure 7 days before framing. Verify hole dia for 8x8 + sleeve + collar cover.', 400, INK),
        ('7. Floor: RAISED PAD — 4" clean gravel over graded native clay (no structural fill — dense-bearing site), finished 4"–6" above grade, crowned.', 400, INK),
        ('8. Rear endwall mirrors front — 2 RJ posts + 2x12 header, sided over for future 10×9 roll-up (Floor Plan note D).', 400, INK)],
        size=9.5, lh=18))
    return sheet('A-2', 'Foundation & Post Layout', 'FOUNDATION & POST LAYOUT', ''.join(o),
                 'SCHEMATIC — NOT FOR PERMIT · DIMENSIONS GOVERN, DO NOT SCALE · connection & collar sizing per the project engineer', '2 of 7')
