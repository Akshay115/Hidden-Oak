# Real photography still needed

This list covers every placeholder that should be replaced with **real photos of Hidden Oak** before launch.  
Decorative AI assets under `public/images/generated/` are **not** substitutes for venue photography.

**Do not use AI-generated images for any of the items below** — they depict the physical banya, sauna, ice bath, grounds, or people.

---

## Homepage — `/` (`src/pages/index.astro`)

| # | Location in code | Placeholder text / role | Suggested shot |
|---|------------------|-------------------------|----------------|
| 1 | Hero `poster` prop (~line 36) | `/images/hero/hero-poster.svg` — full-bleed hero background | Wide exterior or warm doorway at dusk; optional looping video later (`/video/hero-loop.mp4`) |
| 2 | “What we offer” section — `.imgslot` (~line 54–56) | `[IMAGE: Warm interior of the banya — wooden bench, steam rising, clay walls catching firelight. Landscape orientation.]` | Interior landscape: bench, steam, clay walls |
| 3 | “Why Hidden Oak” section — `.imgslot--wide` (~line 111–113) | `[IMAGE: Exterior of the banya in its jungle setting — mud/clay walls, surrounded by palms and greenery, warm light from the doorway at dusk. Wide landscape.]` | Wide exterior at dusk among palms |
| 4 | Closing CTA — `.imgslot` (~line 187–189) | `[IMAGE: A guest mid-session — feet on a wooden bench, hands resting, steam softening the frame. Warm tones, calm mood. Portrait or square.]` | Guest mid-session (with consent); portrait/square |

---

## Gallery — `/gallery` (`src/pages/gallery.astro`)

All entries in the `images` array currently point at themed SVGs in `public/images/gallery/`. Replace each `.svg` with a real `.jpg`/`.webp`, update `w`/`h`, and keep categories.

| # | Current file | Category | Alt / intent |
|---|--------------|----------|--------------|
| 5 | `exterior-approach.svg` | exterior | Path approaching the banya through palms |
| 6 | `exterior-dusk.svg` | exterior | Exterior at dusk, warm light from doorway |
| 7 | `exterior-garden.svg` | exterior | Garden path / outdoor seating |
| 8 | `sauna-bench.svg` | sauna | Wooden bench in steam room |
| 9 | `sauna-stove.svg` | sauna | Stone stove (kamenka) |
| 10 | `sauna-steam.svg` | sauna | Steam rising as water hits stones |
| 11 | `ice-tub.svg` | ice | Cold plunge tub |
| 12 | `ice-detail.svg` | ice | Close-up of cold water surface |
| 13 | `detail-wood-grain.svg` | details | Close-up of interior wood grain *(decorative tile textures elsewhere are OK; this gallery entry should still be real wood from the venue)* |
| 14 | `detail-clay-wall.svg` | details | Troweled clay plaster wall on site |
| 15 | `detail-venik.svg` | details | Birch/oak venik bundle used at Hidden Oak |
| 16 | `community-tea.svg` | community | Tea in the rest area between rounds |
| 17 | `community-rest.svg` | community | Rest area with benches / soft light |
| 18 | `community-hands.svg` | community | Hands with venik during ritual (consent) |

Gallery copy still notes placeholders (~line 166 area in the page template).

---

## Open Graph / default social image

| # | Location | Current asset | Notes |
|---|----------|---------------|-------|
| 19 | `BaseLayout.astro` default `ogImage` | `/images/og-default.svg` | Prefer a real 1200×630 photo of the venue for social shares |

---

## Explicitly out of scope for this checklist

These are **decorative**, already generated/wired, and must **not** be treated as venue photos:

- `public/images/generated/birch-motif.svg` / `birch-motif-glyph.svg`
- `public/images/generated/wood-texture-tile.png` / `clay-texture-tile.png`
- `public/images/generated/steam-overlay.png`
- `public/images/generated/icon-*.svg`

---

## Launch readiness

- [ ] All homepage `[IMAGE: …]` slots replaced with real `<img>` (or picture) elements  
- [ ] Hero poster (and optional hero video) is real photography  
- [ ] Gallery array points at real raster images with correct dimensions  
- [ ] OG image is a real 1200×630 venue photo  
- [ ] Guest/community photos have model releases / consent  
- [ ] Compress exports (WebP/JPEG quality ~80) before deploy  

When photography is ready: drop files into `public/images/` (or `gallery/`), update paths in `index.astro` / `gallery.astro` / `BaseLayout`, and delete or archive the SVG stand-ins.
