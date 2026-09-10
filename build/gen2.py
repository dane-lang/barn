from gen import *

# ───────────────────────── A-3 ELEVATIONS ─────────────────────────
def a3():
    o = []
    sc = 10                      # px per ft
    eave = S['CEIL_TARGET']; ridge = S['RIDGE']; oh = S['EAVE_OH']
    def gable(ox, base_y, title, sub, doors):
        """end elevation, 20' wide + 2' eaves"""
        w = S['W'] * sc; ex = oh * sc
        x0, x1 = ox, ox + w; ey = base_y - eave * sc; ry = base_y - ridge * sc
        # wall
        o.append(rect(x0, ey, w, eave * sc, STONE, INK, 1))
        # ONE roof plane at 6:12 from tail tip through ridge — no kink at the wall.
        # Ridge (18'-6") governs; descending at 6:12: wall line = ridge - 5' (heel absorbs the 1'-6" above the 12' cut), tail tip = ridge - 6'.
        cxm = (x0 + x1) / 2
        wy = ry + (S['W'] / 2) * (6 / 12) * sc            # roof edge at the wall plane
        tty = ry + (S['W'] / 2 + oh) * (6 / 12) * sc      # roof edge at tail tip, 2' past the wall — same slope, same line
        # gable wall face fills up to the roofline
        o.append(f'<path d="M{x0} {base_y} L{x0} {wy} L{cxm} {ry} L{x1} {wy} L{x1} {base_y} z" fill="{STONE}" stroke="{INK}" stroke-width="1"/>')
        for sgn, xx in ((-1, x0), (1, x1)):
            tx = xx + sgn * ex
            fb = tty + 5.5 / 12 * sc
            o.append(f'<path d="M{xx} {wy} L{tx} {tty} L{tx} {fb} L{xx} {fb} z" fill="#eee" stroke="{INK}" stroke-width="0.75"/>')  # soffit box
            o.append(rect(min(tx, tx - sgn * 3), tty, 3, fb - tty, NAVY, NAVY))                                                     # vertical fascia
            o.append(line(tx, fb, xx, fb, NAVY, 2))                                                                                 # soffit return
        # roofline drawn LAST as one unbroken stroke: tail tip → ridge → tail tip
        o.append(f'<path d="M{x0-ex} {tty} L{cxm} {ry} L{x1+ex} {tty}" fill="none" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round" stroke-linecap="butt"/>')
        for d in doors:
            dx, dw, dh, kind = d; ddx = x0 + dx * sc
            o.append(rect(ddx - 3, base_y - dh * sc - 3, dw * sc + 6, dh * sc + 3, NAVY, NAVY))
            o.append(rect(ddx, base_y - dh * sc, dw * sc, dh * sc, '#fff', INK, 1))
            if kind == 'ru':
                for k in range(1, 6): o.append(line(ddx, base_y - dh * sc * k / 6, ddx + dw * sc, base_y - dh * sc * k / 6, '#ccc', 1))
                o.append(T(ddx + dw * sc / 2, base_y - dh * sc / 2, "10'×9' ROLL-UP", 8, 700, INK, 'middle'))
            else:
                o.append(T(ddx + dw * sc / 2, base_y - dh * sc / 2, '36"', 8, 700, INK, 'middle'))
        o.append(line(x0 - ex, base_y, x1 + ex, base_y, INK, 1.5))
        # dims
        o.append(dimV(ry, base_y, x0 - ex - 22, ft(ridge), left=True, size=10))
        o.append(dimV(ey, base_y, x1 + ex + 22, ft(eave), left=False, size=10, color=ACC))
        o.append(T(x1 + ex + 28, (ey + base_y) / 2 + 16, 'target · 11\'-0" min', 8, 400, ACC))
        o.append(dimH(x0 - ex, x0, ry + (S['W'] / 2 + oh) * (6 / 12) * sc + 5.5 / 12 * sc + 14, "2'-0\"", size=8, above=False))
        o.append(dimH(x0, x1, base_y + 34, ft(S['W']), size=10))
        o.append(T((x0 + x1) / 2, base_y + 62, title, 11, 700, INK, 'middle'))
        o.append(T((x0 + x1) / 2, base_y + 76, sub, 8.5, 400, GRAY, 'middle'))
        return x0, x1
    # front (left)
    x0, x1 = gable(130, 300, 'FRONT ELEVATION (roll-up end)', "2'-0\" boxed eaves both sides — vented vinyl soffit, level return to wall · no gable overhang",
                   [(5, S['RU_W'], S['RU_H'], 'ru'), (16, S['MD_W'], S['MD_H'], 'md')])
    for a, b, lab in ((0, 5, "5'-0\""), (5, 15, "10'-0\""), (15, 16, "1'"), (16, 19, "3'-0\""), (19, 20, "1'")):
        o.append(dimH(x0 + a * sc, x0 + b * sc, 300 + 16, lab, size=8))
    # rear (right)
    x0, x1 = gable(560, 300, 'REAR ELEVATION', "2'-0\" boxed eaves both sides — vented vinyl soffit, level return to wall · no gable overhang",
                   [(1, S['MD_W'], S['MD_H'], 'md')])
    for a, b, lab in ((0, 1, "1'"), (1, 4, "3'-0\""), (4, 20, "16'-0\"")):
        o.append(dimH(x0 + a * sc, x0 + b * sc, 300 + 16, lab, size=8))

    # sidewalls
    def side(ox, base_y, title, sub, slot):
        w = S['L'] * sc; x0, x1 = ox, ox + w; ey = base_y - eave * sc; roof_h = S['RISE'] * sc
        o.append(rect(x0, ey - roof_h, w, roof_h, NAVY, NAVY)); o.append(T(x0 + 30, ey - roof_h + 24, 'Regal Blue roof plane beyond (6:12)', 9, 400, '#dbe8f3'))
        o.append(rect(x0, ey, w, eave * sc, STONE, INK, 1))
        if slot:
            o.append(rect(x0, ey, w, 1.5 * sc, '#e8f0f8', '#9db8d6', 1))
            for k in range(S['NBAYS'] + 1):
                pxx = min(max(x0 + k * S['BAY'] * sc - 3, x0 + 1), x1 - 7)
                o.append(rect(pxx, ey, 6, 1.5 * sc, TAN, INK, 0.5))
            o.append(dimV(ey, ey + 1.5 * sc, x0 - 22, '~18"', left=True, size=8))
        o.append(line(x0, base_y, x1, base_y, INK, 1.5))
        o.append(dimV(ey - roof_h, ey, x1 + 22, ft(S['RISE']), left=False, size=9))
        o.append(dimV(ey, base_y, x1 + 22, ft(eave), left=False, size=10, color=ACC))
        for k in range(S['NBAYS']): o.append(dimH(x0 + k * S['BAY'] * sc, x0 + (k + 1) * S['BAY'] * sc, base_y - 8, "10'-0\"", size=8, above=True))
        o.append(dimH(x0, x1, base_y + 22, ft(S['L']), size=10))
        o.append(T((x0 + x1) / 2, base_y + 48, title, 11, 700, INK, 'middle')); o.append(T((x0 + x1) / 2, base_y + 62, sub, 8.5, 400, GRAY, 'middle'))
    side(130, 660, 'SIDEWALL A (bench / light-slot side)', '', True)
    side(700, 660, 'SIDEWALL B (opposite — no openings)', '', False)
    # ceiling note (v2)
    o.append(note_box(920, 80, 400, 110, 'CEILING HEIGHT — v2', [
        (f"Eave = {ft(eave)} = post cut line = bottom of truss (target).", 700, ACC),
        (f"Actual eave lands {ft(S['CEIL_MIN'])}–{ft(eave)} per the site-set level line", 400, INK), ("(Sheet A-2 note 3). Ridge = eave + " + ft(S['RISE']) + " (6:12 per Kilby T02)", 400, INK),
        (f"→ {ft(ridge)} at target. Girts, purlins, trusses key off the cut top.", 400, INK)],
        fill='#fff8e1', st='#e6c96a', size=9.5, lh=15, tfill=ACC))
    # finishes
    fx, fy = 920, 206
    o.append(rect(fx, fy, 400, 110, '#fff', RULE)); o.append(T(fx + 14, fy + 22, 'FINISHES', 12, 700))
    for i, (col, lab) in enumerate([(STONE, 'Walls — Lyon board & batten, Light Stone'), (NAVY, 'Roof, fascia, corner & opening trim — Regal Blue'), ('#eee', 'Soffit — white vented vinyl'), ('#e8f0f8', 'Light slot — clear polycarbonate (screen behind)'), ('#fff', 'Doors — Gloss White')]):
        o.append(rect(fx + 14, fy + 32 + i * 15, 14, 10, col, '#999', 0.5)); o.append(T(fx + 36, fy + 41 + i * 15, lab, 9.5))
    return sheet('A-3', 'Exterior Elevations', 'EXTERIOR ELEVATIONS · Mountain City, TN', ''.join(o),
                 "SCHEMATIC — NOT FOR PERMIT · DIMENSIONS GOVERN, DO NOT SCALE · 6:12 roof per Kilby T02 · 2'-0\" boxed eave soffits (sidewalls, T02 tails) · rake FLUSH at gable ends", '3 of 7')

# ───────────────────────── A-4 WALL / GIRT DETAIL ─────────────────────────
def a4():
    o = []
    pxin = 4                       # px per inch, uniform (members drawn by WIDTH)
    ox, base = 240, 706            # bay origin, grade line
    bay = S['BAY'] * 12 * pxin     # 480
    post_w = S['POST_IN'] * pxin   # 29
    g6 = 5.5 * pxin; g10 = 9.25 * pxin
    top = base - S['CEIL_TARGET'] * 12 * pxin       # cut line
    o.append(T(ox, 74, "WALL FRAMING — one 10' bay (siding removed) · 8x8 posts · 12'-0\" target wall", 13, 700))
    for x in (ox, ox + bay - post_w): o.append(rect(x, top, post_w, base - top, TAN, INK, 1))
    o.append(rect(ox, base - g10, bay, g10, TAN, INK, 1))                       # splash
    rows = [base - (9.25 + 24 * k) * pxin for k in range(1, 5)]              # field girts @24" from splash top
    sill = base - S['SILL_AFG'] * 12 * pxin
    for yy in rows + [sill]:
        o.append(rect(ox, yy - g6, bay, g6, TAN2, INK, 1))
        for x in (ox + 6, ox + bay - 14): o.append(f'<circle cx="{x+4}" cy="{yy-g6/2-3}" r="1.5"/><circle cx="{x+4}" cy="{yy-g6/2+3}" r="1.5"/>')
    slot_y, slot_h = top + g6, sill - g6 - top - g6
    for x in (ox, ox + bay - post_w):                                          # posts SEEN THROUGH the clear glazing
        o.append(rect(x, slot_y, post_w, slot_h, '#e6d3ae', INK, 0.75))
    o.append(f'<rect x="{ox}" y="{slot_y}" width="{bay}" height="{slot_h}" fill="#e8f0f8" fill-opacity="0.55" stroke="#9db8d6" stroke-width="1"/>')
    o.append(T(ox + bay / 2, (top + sill) / 2 + 3, 'clear-poly light slot — posts visible through glazing', 9, 400, GRAY, 'middle'))
    o.append(rect(ox, top, bay, g6, TAN2, INK, 1))                            # top plate at cut line
    o.append(rect(ox - 8, top - 28, bay + 16, 22, NAVY, NAVY))                 # fascia (beyond)
    o.append(line(ox - 60, top, ox + bay + 60, top, ACC, 1.5, '6 3')); o.append(T(ox + bay + 64, top + 4, 'CUT LINE / bottom of truss', 9, 700, ACC))
    def lab(y, s, bold=False): o.append(T(ox - 12, y, s, 9.5, 700 if bold else 400, INK, 'end'))
    lab(top - 12, '1x6 fascia — 5½" (beyond)'); lab(top + 14, 'top plate 2x6 — rides at cut line'); lab((top + sill) / 2 + 3, 'light slot — 24" at target, ≥12" at min')
    lab(sill - 2, "sill girt @ 10'-0\" AFG", True); lab(rows[-1] - 2, '~15" gap · see note 6', True); lab(rows[1] - 2, '2x6 girts @ 24" o.c.', True); lab(base - g10 / 2 + 3, '2x10 splash — 9¼"')
    o.append(T(ox - 12, (rows[0] + rows[1]) / 2 - 2, '8x8 post — 7¼" wide', 9.5, 400, INK, 'end'))
    o.append(rect(ox - 40, base, bay + 80, 30, 'url(#hatch)', 'none')); o.append(line(ox - 40, base, ox + bay + 40, base, INK, 1))
    for x in (ox - 40, ox + bay + 8): o.append(rect(x, base - 12, 34, 12, '#e2e6ea', INK, 1))
    o.append(dimH(ox, ox + bay, base + 54, "10'-0\" bay (posts o.c., outside face)", size=10))
    o.append(dimV(top, base, ox + bay + 30, ft(S['CEIL_TARGET']), left=False, size=10, color=ACC))
    o.append(dimV(sill, base, ox + bay + 30 + 40, ft(S['SILL_AFG']), left=False, size=9))
    lx, ly = 860, 100
    o.append(T(lx, ly, 'MEMBERS — shown by width · 1 in = 4 px', 12, 700))
    for i, (w, c, s) in enumerate([(post_w, TAN, '8x8 post — 7¼"'), (g6, TAN2, '2x6 girt — 5½"'), (g10, TAN, '2x10 — 9¼"')]):
        o.append(rect(lx, ly + 14 + i * 28, w * 1.25, 12, c, INK, 1)); o.append(T(lx + w * 1.25 + 10, ly + 24 + i * 28, s, 10))
    o.append(T(lx, ly + 104, '8x8 face is 1¾" wider than the 6x6 baseline.', 8.5, 400, ACC)); o.append(T(lx, ly + 117, '(thickness — 1½" — is depth into wall, not contrasted here.)', 8.5, 400, GRAY))
    o.append(note_box(lx, ly + 136, 450, 420, 'GIRT NOTES', [
        '1. 2x6 girts face-applied to the OUTSIDE face of posts', '    @ 24" o.c. from the top of the splash — wall plane = post face.', '',
        '2. Bottom girt: treated 2x10, retains gravel / slab edge.', '',
        "3. Sill girt at 10'-0\" AFG + top plate at the cut line frame the", '    clear-poly light slot: 24" at 12\' target, ≥12" at 11\' minimum.', '',
        '4. B&B steel siding over girts; screws @ 24", Light Stone.', '', '5. Base guard + foam closure at panel bottom.', '',
        ('6. v2: girt COUNT is unchanged from baseline (4 field + sill).', 700, ACC), ('    The added wall foot lands as a ~15" gap between the last', 700, ACC),
        ('    field girt and the sill — shorter span, no panel issue.', 700, ACC), ('    Crew may re-space the top run in the field; do not', 700, ACC), ('    exceed 24" between girts anywhere.', 700, ACC)], size=10, lh=15))
    return sheet('A-4', 'Wall / Girt Detail', 'WALL / GIRT DETAIL · members shown by width', ''.join(o),
                 'MEMBERS BY WIDTH · 1 in = 4 px · NOT FOR PERMIT · connection sizing per Lyon / Simpson', '4 of 7')

# ───────────────────────── A-5 ROOF FRAMING ─────────────────────────
def a5():
    o = []
    sc = 14; ox, oy = 180, 130; L = S['L']; W = S['W']; oh = S['EAVE_OH']
    o.append(T(120, 92, 'ROOF FRAMING PLAN (top-down)', 13, 700))
    tot_w = (W + 2 * oh) * sc
    o.append(rect(ox, oy, L * sc, tot_w, '#fafafa', INK, 1))
    # trusses FIRST (below), then purlins drawn OVER them
    for i in range(S['NBAYS'] + 1):
        x = ox + i * S['BAY'] * sc; ge = i in (0, S['NBAYS'])
        o.append(line(x, oy, x, oy + tot_w, INK, 3 if ge else 2))
        o.append(T(x, oy - 22, f'T{i+1}', 10, 700, BLUE if ge else INK, 'middle')); o.append(T(x, oy - 10, 'T02GE' if ge else 'T02', 8, 700, BLUE if ge else INK, 'middle'))
        for y_ in (oy + oh * sc, oy + tot_w - oh * sc): o.append(rect(x - 5, y_ - 5, 10, 10, INK, INK))
    pw = 5.5 / 12 * sc
    y = oy + 0.5 * sc
    while y < oy + tot_w - 0.4 * sc:
        o.append(rect(ox, y - pw / 2, L * sc, pw, '#e8e2d2', '#8f866f', 0.75)); y += 2 * sc
    o.append(line(ox, oy + tot_w / 2, ox + L * sc, oy + tot_w / 2, BLUE, 1.5)); o.append(T(ox + L * sc / 2, oy + tot_w / 2 - 4, 'RIDGE', 9, 700, BLUE, 'middle'))
    o.append(line(ox, oy + oh * sc, ox + L * sc, oy + oh * sc, GRAY, 1, '3 3')); o.append(line(ox, oy + tot_w - oh * sc, ox + L * sc, oy + tot_w - oh * sc, GRAY, 1, '3 3'))
    o.append(T(ox + L * sc / 2, oy + 14, "2'-0\" eave overhang — fascia at edge · closed vented vinyl soffit below, level return to wall", 8.5, 400, GRAY, 'middle'))
    o.append(T(ox + L * sc / 2, oy + tot_w - 6, "2'-0\" eave overhang — fascia at edge · closed vented vinyl soffit below, level return to wall", 8.5, 400, GRAY, 'middle'))
    o.append(T(ox + L * sc / 2, oy + tot_w * 0.32, '2x6 purlins FLAT @ 24" o.c. ON TOP of truss top chords — 5½" face shown, to scale', 9, 400, GRAY, 'middle'))
    o.append(T(ox + L * sc / 2, oy + tot_w * 0.66, "T02 = FINK · T02GE = GABLE END (blue tags) · 10'-0\" o.c. on 8x8 posts (■) · truss bears on CUT post top", 9, 400, GRAY, 'middle'))
    for i in range(S['NBAYS']): o.append(dimH(ox + i * S['BAY'] * sc, ox + (i + 1) * S['BAY'] * sc, oy + tot_w + 16, "10'-0\"", size=8))
    o.append(dimH(ox, ox + L * sc, oy + tot_w + 40, ft(L) + ' — roof FLUSH at gable ends (no rake overhang)', size=9))
    o.append(dimV(oy + oh * sc, oy + tot_w - oh * sc, ox + L * sc + 44, ft(W) + ' span', left=False, size=9))
    o.append(T(ox + L * sc + 50, oy + tot_w / 2 + 16, "24'-0\" o-o eaves · 2'-0\" tails per T02", 8, 400, GRAY))
    # truss thumbs — simple line fink to scale
    def truss(x, y, w, gable):
        h = S['RISE'] / S['SPAN'] * w * 0.85
        o.append(rect(x, y - 30, w + 20, 28, ACC, ACC)); o.append(T(x + 10, y - 11, 'T02GE — GABLE END' if gable else 'T02 — FINK', 11, 700, '#fff')); o.append(T(x + w + 10, y - 11, 'QTY 2 · T1 · T5' if gable else 'QTY 3 · T2 · T3 · T4', 9, 700, '#fff', 'end'))
        bx, ex = x + 10, x + w + 10; by = y + 130; ax = (bx + ex) / 2; ay = by - h
        o.append(f'<path d="M{bx} {by} L{ex} {by} L{ax} {ay} z" fill="none" stroke="{INK}" stroke-width="2"/>')
        if gable:
            for k in range(1, 12): xx = bx + (ex - bx) * k / 12; yy = by - (h * (1 - abs(k - 6) / 6)); o.append(line(xx, by, xx, yy, GRAY, 1))
        else:
            b1 = bx + (ex - bx) / 3; b2 = ex - (ex - bx) / 3; t1x = bx + (ex - bx) / 4; t2x = ex - (ex - bx) / 4; ty = by - h / 2
            o.append(f'<path d="M{t1x} {ty} L{b1} {by} L{ax} {ay} L{b2} {by} L{t2x} {ty}" stroke="{GRAY}" stroke-width="1.5" fill="none"/>')
        o.append(T(bx, by + 18, "Kilby Truss, Inc. · MiTek · job DANE GROVE · 6:12 · 20' span · 2'-0\" tails · see REF sheets", 8, 400, GRAY))
    truss(60, 560, 420, False); truss(560, 560, 420, True)
    o.append(note_box(1040, 530, 280, 240, 'ROOF NOTES', [
        '1. Trusses per Kilby/MiTek T02 & T02GE:', "   6:12, 20' span, 2'-0\" tails — 24' o-o", '   eaves. Truss sheets govern.', '',
        '2. 2x6 purlins FLAT @ 24" o.c. — wide face', '   bearing on top chords (like girts on posts).', '',
        '3. 26-ga AG panel over purlins; factory', '   anti-condensation felt on underside.', '',
        '4. Truss-to-post & purlin-to-truss', '   connections: see Sheet A-6.', '',
        "5. T02GE gable studs @ 2'-0\" o.c.; rake", '   FLUSH — no outlookers, rake trim only.'], size=9.5, lh=13))
    return sheet('A-5', 'Roof Framing', 'ROOF FRAMING · Mountain City, TN', ''.join(o),
                 'DRAWN TO ONE SCALE · NOT FOR PERMIT · trusses per Kilby Truss / MiTek T02 & T02GE', '5 of 7')

# ───────────────────────── A-6 CONNECTION DETAILS ─────────────────────────
def a6(h10s_b64):
    o = []
    # H10S image panel (Simpson catalog reference carried from baseline)
    o.append(rect(20, 68, 540, 700, '#fff', RULE)); o.append(rect(20, 68, 540, 30, ACC, ACC)); o.append(T(34, 88, 'TRUSS-TO-POST TIE — Simpson Strong-Tie H10S', 12, 700, '#fff'))
    o.append(f'<image href="data:image/png;base64,{h10s_b64}" x="60" y="110" width="460" height="560" preserveAspectRatio="xMidYMid meet"/>')
    o.append(T(290, 690, 'Illustration: Simpson Strong-Tie', 8.5, 400, GRAY, 'middle'))
    o.append(rect(20, 706, 540, 60, '#f4f6f8', 'none')); o.append(T(34, 728, 'Shown: Simpson catalog condition (stud wall).', 9, 400, GRAY)); o.append(T(34, 744, 'This build: truss bears directly on the CUT 8x8 post top — same tie, same fastening, no wall plates.', 9, 700, INK))
    o.append(T(34, 758, 'v2: 8x8 face is wider than the 6x6 the tie pattern was reviewed against — confirm pattern / screw length with Lyon / Simpson.', 8.5, 700, ACC))
    # rule + other connections
    o.append(note_box(580, 68, 340, 400, 'H10S RULE', [
        '• One H10S per truss, each bearing — 8 trusses,', '  both ends. No HGA. No notching.', '',
        '• REQUIRED: 8 fasteners into the truss chord', '  + 8 into the post.', '',
        '• FULL PATTERN: fill every hole — up to 16 in', '  the post where fasteners clear.', '',
        '• All fasteners: Simpson SD9112', '  (SD Connector #9 × 1½"). No nails.', '',
        '• Install tie flat — no bending, no field', '  modification of the connector.', '',
        '• Same tie, same pattern at the future rear', '  roll-up jamb trusses.'], size=10, lh=14))
    o.append(note_box(580, 488, 340, 280, 'OTHER CONNECTIONS', [
        ('PURLIN TO TRUSS', 700, ACC), '2 SD9112 toe-driven per bearing, opposing', 'angles. H1 clip if Lyon pkg requires.', '',
        ('GIRT TO POST', 700, ACC), '2 SD9112 per post, staggered. Girts land', 'flush on exterior post face, 24" o.c.', '',
        ('SPLASH BOARD TO POST', 700, ACC), 'Treated 2x10: 3 SD9112 per post.', '',
        ('HEADER TO JAMB POST', 700, ACC), '8x8 + 2x12 header: SDWS22600 timber', 'screws down into jamb-post end. Both roll-ups.'], size=10, lh=14))
    o.append(note_box(940, 68, 380, 400, 'INSTALL SEQUENCE', [
        '1  Cut all post tops to the level line (A-2 note 3).', '2  Set truss on post; center bearing, crown up.', '3  Tack truss plumb; brace before tying.',
        '4  Place H10S on post face, tight to chord.', '5  Drive 8 SD9112 into the truss chord.', '6  Drive 8 (up to 16) SD9112 into the post.',
        '7  Repeat both bearings, all 8 trusses.', '8  Inspect: every listed hole filled, screws', '   flush, no shiners.'], size=10, lh=22))
    o.append(note_box(940, 488, 380, 280, 'JOB-SITE NOTES', [
        '• Buy H10S in the 8-pack carton (16 needed', '  + 2 spares).', '• SD9112: ~400 screws — one 3-lb box covers', '  ties + girt schedule margin.',
        '• Drive with #2 square/hex bit, impact driver,', '  clutch set to seat — do not overdrive.', '• Ties are G90 galvanized — fine over', '  treated 8x8 in this dry-service barn.',
        '• Do not substitute drywall or deck screws.', '', 'Simpson p/n: H10S · SD9112 · SDWS22600'], fill='#fff8e1', st='#e6c96a', size=10, lh=14))
    return sheet('A-6', 'Connection Details', 'CONNECTION DETAILS · Mountain City, TN', ''.join(o),
                 'NOT FOR PERMIT · connector capacities per Simpson Strong-Tie current catalog · verify hole fill & screw length at install', '6 of 7')

# ───────────────────────── A-7 MATERIALS LIST (new) ─────────────────────────
def materials():
    """(category, item, spec, est qty, unit, basis) — qty derived from SPEC where possible"""
    n_post = 14; bays = S['NBAYS']; girt_rows = S['GIRT_ROWS']
    side_len = S['L']; end_len = S['W']
    # girt LF: 2 sidewalls + 2 endwalls, rows each, minus roll-up/door openings ignored (over-est is fine)
    girt_lf = girt_rows * 2 * (side_len + end_len)
    purlin_lf = int((end_len + 2 * S['EAVE_OH']) / 2 + 1) * side_len   # rows across 24' @ 2'
    roof_area = 2 * S['L'] * (((S['W'] / 2 + S['EAVE_OH']) ** 2 + (S['RISE'] - 0.9) ** 2) ** 0.5)
    wall_area = 2 * side_len * S['CEIL_TARGET'] + 2 * end_len * S['CEIL_TARGET'] + 2 * (0.5 * end_len * (S['RISE'] - 0.9))
    return [
        ('POSTS & FOUNDATION',
         [('8x8 treated post', f"{ft(S['POST_LEN'])} · ground-contact rated (UC4B)", n_post, 'ea', '10 field + 4 roll-up jamb'),
          ('Precast concrete footing pad', 'sized per engineering', n_post, 'ea', '1 per post'),
          ('Concrete, collar', f"~{S['HOLE_IN']}\" hole × {ft(S['EMBED'])} · verify for 8x8", n_post * 3, 'bag 80 lb', '~3 bags/post or ~1.5 cy mix'),
          ('Rigid HDPE post sleeve', '~60-mil, sized for 8x8', n_post, 'ea', '1 per post'),
          ('Temporary bracing lumber', '2x4 × 12\'', 28, 'ea', '2 per post'),
          ('Treated 2x10 splash plank', '12\'', 10, 'ea', f"perimeter {2*(side_len+end_len):.0f} LF")]),
        ('WALL FRAMING',
         [('2x6 girts', '12\' · #2 SPF', int(girt_lf / 12) + 2, 'ea', f"{girt_rows} runs × perimeter = {girt_lf:.0f} LF"),
          ('2x6 top plate', '16\'', 8, 'ea', 'at cut line, perimeter'),
          ('2x12 header', '12\' · roll-up openings', 4, 'ea', '2 per roll-up (front + future rear)'),
          ('2x6 jamb studs', '12\'', 8, 'ea', 'man doors, 2 per side'),
          ('1x6 fascia', '16\'', 8, 'ea', 'sidewall eaves 2 × 40\' + rake')]),
        ('ROOF',
         [('Kilby T02 fink truss', "6:12 · 20' span · 2' tails", 3, 'ea', 'T2 T3 T4'),
          ('Kilby T02GE gable-end truss', "6:12 · 20' span · 2' tails", 2, 'ea', 'T1 T5'),
          ('2x6 purlins', '12\' · flat @ 24" o.c.', int(purlin_lf / 12) + 2, 'ea', f"~{purlin_lf:.0f} LF"),
          ('2x6 gable studs', '12\' @ 24" o.c.', 20, 'ea', 'both gable ends'),
          ('26-ga AG roof panel', 'Regal Blue · anti-condensation felt', int(roof_area * 1.1), 'sq ft', f"~{roof_area:.0f} sf + 10% waste"),
          ('Ridge cap', 'Regal Blue', 44, 'LF', '40\' + laps'),
          ('Eave / drip trim', 'Regal Blue', 88, 'LF', '2 × 40\' + laps'),
          ('Rake trim', 'Regal Blue · flush rake', 50, 'LF', '4 rakes × ~12\''),
          ('Vented vinyl soffit', 'white · 2\' boxed eaves', 170, 'sq ft', '2 × 40\' × 2\' + returns'),
          ('Foam closures, roof', 'panel profile', 90, 'LF', 'eave + ridge')]),
        ('SIDING & TRIM',
         [('Lyon board & batten steel panel', 'Light Stone · 12\' & 13\' lengths', int(wall_area * 1.1), 'sq ft', f"~{wall_area:.0f} sf + 10% waste"),
          ('Corner trim', 'Regal Blue', 52, 'LF', '4 corners × 12\'+'),
          ('J / opening trim', 'Regal Blue · roll-ups + man doors', 90, 'LF', 'buy future roll-up trim NOW'),
          ('Base guard / foam closure, wall', 'panel profile', 120, 'LF', 'perimeter'),
          ('Clear polycarbonate light-slot panel', '~18" × 40\'', 60, 'sq ft', 'sidewall A top 2\''),
          ('Insect screen, light slot', 'behind poly', 60, 'sq ft', '')]),
        ('DOORS',
         [("10'×9' Janus roll-up", 'Gloss White', 1, 'ea', 'front, installed now'),
          ('36" steel man door, prehung', 'Gloss White · OUTSWING · NRP hinges', 1, 'ea', 'front endwall (B)'),
          ('36" steel man door, prehung', 'Gloss White · OUTSWING · NRP hinges', 1, 'ea', 'rear endwall (C)')]),
        ('CONNECTORS & FASTENERS',
         [('Simpson H10S truss tie', 'G90', 18, 'ea', '16 + 2 spares'),
          ('Simpson SD9112 screw', '#9 × 1½"', 400, 'ea', '1 × 3-lb box — ties + girts'),
          ('Simpson SDWS22600 timber screw', '6"', 24, 'ea', 'headers to jamb posts'),
          ('Panel screws, siding', '#12 × 1½" color-match, Light Stone', 1200, 'ea', '~1 per sf / 24" pattern'),
          ('Panel screws, roof', '#12 × 1½" color-match, Regal Blue', 1100, 'ea', ''),
          ('Stitch screws', '¼" lap', 200, 'ea', 'trim + laps')]),
        ('FLOOR',
         [('Compacted structural fill', 'to raise pad', 20, 'cy', '800 sf × ~6"; confirm on site'),
          ('#57 clean gravel', '4" crowned', 12, 'cy', '800 sf × 4" + crown')]),
    ]

def a7():
    o = []
    rows = materials()
    o.append(T(24, 72, 'DRY-IN MATERIALS — framing, walls, roof, doors, trim · all items named · quantities are ESTIMATES from the v2 dimensions', 13, 700))
    colw = 640; gap = 16
    def render(x0, groups):
        y = 90; cols = (x0 + 8, x0 + 190, x0 + 400, x0 + 440, x0 + 500)
        o.append(rect(x0, y, colw, 18, '#eef1f4', 'none'))
        for cx, hd in zip(cols, ('item', 'spec', 'qty', 'unit', 'basis')): o.append(T(cx + (34 if hd == 'qty' else 0), y + 13, hd, 9, 700, GRAY, 'end' if hd == 'qty' else 'start'))
        y += 24
        for cat, items in groups:
            o.append(rect(x0, y - 2, colw, 15, '#eaf3fb', 'none')); o.append(T(x0 + 8, y + 9, cat, 9.5, 700, ACC)); y += 19
            for item, spec, q, unit, basis in items:
                o.append(T(cols[0], y + 4, item, 9, 600)); o.append(T(cols[1], y + 4, spec, 8.5)); o.append(T(cols[2] + 34, y + 4, str(q), 9, 700, INK, 'end')); o.append(T(cols[3], y + 4, unit, 8.5)); o.append(T(cols[4], y + 4, basis, 8, 400, GRAY))
                o.append(line(x0, y + 9, x0 + colw, y + 9, '#eef1f4', 0.5)); y += 14
            y += 4
    render(24, rows[:3]); render(24 + colw + gap, rows[3:])
    o.append(T(24 + colw + gap, 700, 'Electrical, fixtures, and interior fit-out are a later stage — not listed.', 9, 400, GRAY))
    return sheet('A-7', 'Materials List', 'DRY-IN MATERIALS LIST · estimated quantities · Mountain City, TN', ''.join(o),
                 'ESTIMATES — verify every quantity with supplier take-off before ordering · buy future roll-up trim + fasteners now', '7 of 7')
