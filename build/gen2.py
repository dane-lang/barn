from gen import *

H10S_B64 = "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"

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
        o.append(rect(x0, ey - roof_h, w, roof_h, NAVY, NAVY)); o.append(T(x0 + 30, ey - roof_h + 24, '[roof color] roof plane beyond (6:12)', 9, 400, '#dbe8f3'))
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
        (f"Actual eave lands {ft(S['CEIL_MIN'])}–{ft(eave)} per the site-set level line", 400, INK), ("(Sheet A-2 note 3). Ridge = eave + " + ft(S['RISE']) + " (6:12 per truss mfr (typical))", 400, INK),
        (f"→ {ft(ridge)} at target. Girts, purlins, trusses key off the cut top.", 400, INK)],
        fill='#fff8e1', st='#e6c96a', size=9.5, lh=15, tfill=ACC))
    # finishes
    fx, fy = 920, 206
    o.append(rect(fx, fy, 400, 110, '#fff', RULE)); o.append(T(fx + 14, fy + 22, 'FINISHES', 12, 700))
    for i, (col, lab) in enumerate([(STONE, 'Walls — board & batten, [siding color]'), (NAVY, 'Roof, fascia, corner & opening trim — [roof color]'), ('#eee', 'Soffit — white vented vinyl'), ('#e8f0f8', 'Light slot — clear polycarbonate (screen behind)'), ('#fff', 'Doors — [door color]')]):
        o.append(rect(fx + 14, fy + 32 + i * 15, 14, 10, col, '#999', 0.5)); o.append(T(fx + 36, fy + 41 + i * 15, lab, 9.5))
    return sheet('A-3', 'Exterior Elevations', 'EXTERIOR ELEVATIONS', ''.join(o),
                 "SCHEMATIC — NOT FOR PERMIT · DIMENSIONS GOVERN, DO NOT SCALE · 6:12 roof per truss mfr (typical) · 2'-0\" boxed eave soffits (sidewalls, (typical) tails) · rake FLUSH at gable ends", '3 of 7')

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
        '4. B&B steel siding over girts; screws @ 24", [siding color].', '', '5. Base guard + foam closure at panel bottom.', '',
        ('6. v2: girt COUNT is unchanged from baseline (4 field + sill).', 700, ACC), ('    The added wall foot lands as a ~15" gap between the last', 700, ACC),
        ('    field girt and the sill — shorter span, no panel issue.', 700, ACC), ('    Crew may re-space the top run in the field; do not', 700, ACC), ('    exceed 24" between girts anywhere.', 700, ACC)], size=10, lh=15))
    return sheet('A-4', 'Wall / Girt Detail', 'WALL / GIRT DETAIL · members shown by width', ''.join(o),
                 'MEMBERS BY WIDTH · 1 in = 4 px · NOT FOR PERMIT · connection sizing per the project engineer', '4 of 7')

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
    o.append(T(ox + L * sc / 2, oy + tot_w * 0.66, "T02 = FINK · (gable-end) = GABLE END (blue tags) · 10'-0\" o.c. on 8x8 posts (■) · truss bears on CUT post top", 9, 400, GRAY, 'middle'))
    for i in range(S['NBAYS']): o.append(dimH(ox + i * S['BAY'] * sc, ox + (i + 1) * S['BAY'] * sc, oy + tot_w + 16, "10'-0\"", size=8))
    o.append(dimH(ox, ox + L * sc, oy + tot_w + 40, ft(L) + ' — roof FLUSH at gable ends (no rake overhang)', size=9))
    o.append(dimV(oy + oh * sc, oy + tot_w - oh * sc, ox + L * sc + 44, ft(W) + ' span', left=False, size=9))
    o.append(T(ox + L * sc + 50, oy + tot_w / 2 + 16, "24'-0\" o-o eaves · 2'-0\" tails per (typical)", 8, 400, GRAY))
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
        o.append(T(bx, by + 18, "engineered truss · job CUSTOMER · 6:12 · 20' span · 2'-0\" tails · per manufacturer\'s sealed drawings (provided separately)", 8, 400, GRAY))
    truss(60, 560, 420, False); truss(560, 560, 420, True)
    o.append(note_box(1040, 530, 280, 240, 'ROOF NOTES', [
        '1. Trusses per the truss manufacturer\'s sealed drawings:', "   6:12, 20' span, 2'-0\" tails — 24' o-o", '   eaves. Manufacturer\'s sealed truss drawings govern.', '',
        '2. 2x6 purlins FLAT @ 24" o.c. — wide face', '   bearing on top chords (like girts on posts).', '',
        '3. 26-ga AG panel over purlins; factory', '   anti-condensation felt on underside.', '',
        '4. Truss-to-post & purlin-to-truss', '   connections: see Sheet A-6.', '',
        "5. (gable-end) gable studs @ 2'-0\" o.c.; rake", '   FLUSH — no outlookers, rake trim only.'], size=9.5, lh=13))
    return sheet('A-5', 'Roof Framing', 'ROOF FRAMING', ''.join(o),
                 'DRAWN TO ONE SCALE · NOT FOR PERMIT · trusses per the truss manufacturer\'s sealed drawings', '5 of 7')

# ───────────────────────── A-6 CONNECTION DETAILS ─────────────────────────
def a6():
    o = []
    # truss-to-post tie — manufacturer illustration (Simpson Strong-Tie H10S)
    o.append(rect(20, 68, 540, 700, '#fff', RULE)); o.append(rect(20, 68, 540, 30, ACC, ACC)); o.append(T(34, 88, 'TRUSS-TO-POST TIE', 12, 700, '#fff'))
    o.append(f'<image href="data:image/png;base64,{H10S_B64}" x="60" y="110" width="460" height="560" preserveAspectRatio="xMidYMid meet"/>')
    o.append(T(290, 690, 'Illustration: Simpson Strong-Tie', 8.5, 400, GRAY, 'middle'))
    o.append(rect(20, 706, 540, 60, '#f4f6f8', 'none')); o.append(T(34, 728, 'Tie shown in a catalog stud-wall condition.', 9, 400, GRAY)); o.append(T(34, 744, 'This build: truss bears directly on the CUT 8x8 post top — same tie, same fastening, no wall plates.', 9, 700, INK))
    o.append(T(34, 758, 'Confirm tie model, hole pattern, and screw length for the 8x8 post face with the manufacturer / project engineer.', 8.5, 700, ACC))
    # rule + other connections
    o.append(note_box(580, 68, 340, 400, 'TIE RULE', [
        '• One tie per truss, each bearing — 8 trusses,', '  both ends. No HGA. No notching.', '',
        '• REQUIRED: 8 fasteners into the truss chord', '  + 8 into the post.', '',
        '• FULL PATTERN: fill every hole — up to 16 in', '  the post where fasteners clear.', '',
        '• All fasteners: #9 × 1½" structural screw', '  (SD Connector #9 × 1½"). No nails.', '',
        '• Install tie flat — no bending, no field', '  modification of the connector.', '',
        '• Same tie, same pattern at the future rear', '  roll-up jamb trusses.'], size=10, lh=14))
    o.append(note_box(580, 488, 340, 280, 'OTHER CONNECTIONS', [
        ('PURLIN TO TRUSS', 700, ACC), '2 screws toe-driven per bearing, opposing', 'angles. H1 clip if the connector package requires.', '',
        ('GIRT TO POST', 700, ACC), '2 screws per post, staggered. Girts land', 'flush on exterior post face, 24" o.c.', '',
        ('SPLASH BOARD TO POST', 700, ACC), 'Treated 2x10: 3 screws per post.', '',
        ('HEADER TO JAMB POST', 700, ACC), '8x8 + 2x12 header: 6" structural timber', 'screws down into jamb-post end. Both roll-ups.'], size=10, lh=14))
    o.append(note_box(940, 68, 380, 400, 'INSTALL SEQUENCE', [
        '1  Cut all post tops to the level line (A-2 note 3).', '2  Set truss on post; center bearing, crown up.', '3  Tack truss plumb; brace before tying.',
        '4  Place tie on post face, tight to chord.', '5  Drive 8 screws into the truss chord.', '6  Drive 8 (up to 16) screws into the post.',
        '7  Repeat both bearings, all 8 trusses.', '8  Inspect: every listed hole filled, screws', '   flush, no shiners.'], size=10, lh=22))
    o.append(note_box(940, 488, 380, 280, 'JOB-SITE NOTES', [
        '• Buy tie in the 8-pack carton (16 needed', '  + 2 spares).', '• screws: ~400 screws — one 3-lb box covers', '  ties + girt schedule margin.',
        '• Drive with #2 square/hex bit, impact driver,', '  clutch set to seat — do not overdrive.', '• Ties are G90 galvanized — fine over', '  treated 8x8 in this dry-service barn.',
        '• Do not substitute drywall or deck screws.', '', 'Fasteners: truss-to-post tie · #9×1½" screw · 6" timber screw'], fill='#fff8e1', st='#e6c96a', size=10, lh=14))
    return sheet('A-6', 'Connection Details', 'CONNECTION DETAILS', ''.join(o),
                 'NOT FOR PERMIT · connector capacities per manufacturer\'s current catalog · verify hole fill & screw length at install', '6 of 7')

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
         [('truss mfr (typical) fink truss', "6:12 · 20' span · 2' tails", 3, 'ea', 'T2 T3 T4'),
          ('truss mfr (gable-end) gable-end truss', "6:12 · 20' span · 2' tails", 2, 'ea', 'T1 T5'),
          ('2x6 purlins', '12\' · flat @ 24" o.c.', int(purlin_lf / 12) + 2, 'ea', f"~{purlin_lf:.0f} LF"),
          ('2x6 gable studs', '12\' @ 24" o.c.', 20, 'ea', 'both gable ends'),
          ('26-ga AG roof panel', '[roof color] · anti-condensation felt', int(roof_area * 1.1), 'sq ft', f"~{roof_area:.0f} sf + 10% waste"),
          ('Ridge cap', '[roof color]', 44, 'LF', '40\' + laps'),
          ('Eave / drip trim', '[roof color]', 88, 'LF', '2 × 40\' + laps'),
          ('Rake trim', '[roof color] · flush rake', 50, 'LF', '4 rakes × ~12\''),
          ('Vented vinyl soffit', 'white · 2\' boxed eaves', 170, 'sq ft', '2 × 40\' × 2\' + returns'),
          ('Foam closures, roof', 'panel profile', 90, 'LF', 'eave + ridge')]),
        ('SIDING & TRIM',
         [('board & batten steel panel', '[siding color] · 12\' & 13\' lengths', int(wall_area * 1.1), 'sq ft', f"~{wall_area:.0f} sf + 10% waste"),
          ('Corner trim', '[roof color]', 52, 'LF', '4 corners × 12\'+'),
          ('J / opening trim', '[roof color] · roll-ups + man doors', 90, 'LF', 'buy future roll-up trim NOW'),
          ('Base guard / foam closure, wall', 'panel profile', 120, 'LF', 'perimeter'),
          ('Clear polycarbonate light-slot panel', '~18" × 40\'', 60, 'sq ft', 'sidewall A top 2\''),
          ('Insect screen, light slot', 'behind poly', 60, 'sq ft', '')]),
        ('DOORS',
         [("10'×9' roll-up door", '[door color]', 1, 'ea', 'front, installed now'),
          ('36" steel man door, prehung', '[door color] · OUTSWING · NRP hinges', 1, 'ea', 'front endwall (B)'),
          ('36" steel man door, prehung', '[door color] · OUTSWING · NRP hinges', 1, 'ea', 'rear endwall (C)')]),
        ('CONNECTORS & FASTENERS',
         [(' tie truss tie', 'G90', 18, 'ea', '16 + 2 spares'),
          ('#9 × 1½" structural screw screw', '#9 × 1½"', 400, 'ea', '1 × 3-lb box — ties + girts'),
          (' 6" structural timber screw', '6"', 24, 'ea', 'headers to jamb posts'),
          ('Panel screws, siding', '#12 × 1½" color-match, [siding color]', 1200, 'ea', '~1 per sf / 24" pattern'),
          ('Panel screws, roof', '#12 × 1½" color-match, [roof color]', 1100, 'ea', ''),
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
    return sheet('A-7', 'Materials List', 'DRY-IN MATERIALS LIST · estimated quantities', ''.join(o),
                 'ESTIMATES — verify every quantity with supplier take-off before ordering · buy future roll-up trim + fasteners now', '7 of 7')
