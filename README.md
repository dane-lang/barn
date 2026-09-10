# barn

Construction drawing set for a 40' × 20' agricultural pole barn, Mountain City, TN. Schematic — not for permit. Hosted on GitHub Pages.

| file | what it is |
|---|---|
| `index.html` | **v1 baseline** — eight raster sheets (PNG). Frozen. Do not edit. |
| `v2.html` | **v2** — sheets A-1 to A-7 as inline SVG generated from a single spec block; Kilby truss references carried over as PNG. |
| `build/` | generator source for v2 |

Live: `index.html` → baseline · `v2.html` → v2

## v2 — how it is built

Every dimension on A-1 to A-7 derives from the `S = dict(...)` block at the top of `build/gen.py`. Change a number there, rebuild, re-push. Nothing is hand-drawn.

```
python3 build/extract.py     # once — pulls the 8 baseline PNGs out of index.html into ./sheets/
python3 build/build.py       # writes ./out/v2.html and one .svg per sheet
```

Requires Python 3 with Pillow. `build.py` crops the Simpson H10S illustration and the two Kilby truss sheets from the extracted baseline PNGs, so `extract.py` must run first.

`build/gen.py` — spec block, drawing helpers, sheets A-1 and A-2
`build/gen2.py` — sheets A-3 to A-7 and the materials list
`build/build.py` — assembles `v2.html`

## Datum conventions (v2)

- **Horizontal** — 40' × 20' is out-to-out of posts. The outside face of the post is the wall plane: girts on it, steel over the girts. Posts 10'-0" o.c. Lay out from the datum corner (A-2).
- **Vertical** — AFG = above finished grade (top of pad). Ceiling = grade to bottom of truss = cut post top. Trusses bear directly on cut post tops.

## Deploying a new v2

Rebuild, then upload `out/v2.html` over `v2.html` in this repo. Same URL forever. Leave `index.html` alone.
