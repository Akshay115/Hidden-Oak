#!/usr/bin/env python3
"""
Generate themed SVG placeholder images for the Hidden Oak gallery.
Each image is a distinct gradient + label reflecting its category,
with varying aspect ratios to create masonry rhythm when real photos
are dropped in later.

Categories: Exterior & Setting, The Sauna, Ice Bath, Details, Community
"""
import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'public', 'images', 'gallery')
os.makedirs(OUT, exist_ok=True)

# (filename, label, w, h, gradient stops, icon path)
# Varying aspect ratios create the masonry feel.
images = [
    # ---- Exterior & Setting (landscape + wide) ----
    ("exterior-approach", "Exterior · The approach", 1200, 800,
     [("#3a2818", "#6e5839", "#8a6a3b")],
     # palms
     'M180 700 Q160 500 210 360 Q175 480 230 320 M180 700 Q200 500 240 380'),
    ("exterior-dusk", "Exterior · Dusk light", 1200, 600,
     [("#2B1D14", "#5e4727", "#b08a52")], ''),
    ("exterior-garden", "Exterior · Garden path", 1200, 900,
     [("#2A3D31", "#4d6b56", "#6f7a5a")], ''),

    # ---- The Sauna (mixed: portrait, square, landscape) ----
    ("sauna-bench", "Sauna · Wooden bench", 800, 1000,
     [("#3a2818", "#8a6a3b", "#b08a52")], ''),
    ("sauna-stove", "Sauna · The stone stove", 1200, 1200,
     [("#3a1f12", "#8f4d14", "#c4631f")], ''),
    ("sauna-steam", "Sauna · Steam rising", 1000, 750,
     [("#4a3422", "#8a6a3b", "#d8cdb4")], ''),

    # ---- Ice Bath (portrait + landscape) ----
    ("ice-tub", "Ice Bath · The plunge tub", 800, 1000,
     [("#2a3438", "#4d6b56", "#c6bcad")], ''),
    ("ice-detail", "Ice Bath · Cold water detail", 1200, 800,
     [("#2a3438", "#5e4727", "#b3a888")], ''),

    # ---- Details: wood/clay textures (square + wide) ----
    ("detail-wood-grain", "Details · Wood grain", 1200, 1200,
     [("#3a2818", "#5e4727", "#8a6a3b")], ''),
    ("detail-clay-wall", "Details · Clay plaster wall", 1200, 800,
     [("#4a3422", "#8f4d14", "#b5651d")], ''),
    ("detail-venik", "Details · Venik bundle", 1000, 1000,
     [("#2A3D31", "#6f7a5a", "#d8cdb4")], ''),

    # ---- Community / Sessions (mixed) ----
    ("community-tea", "Community · Tea between rounds", 1200, 800,
     [("#4a3422", "#8a6a3b", "#d8cdb4")], ''),
    ("community-rest", "Community · Rest area", 1000, 1000,
     [("#3a2818", "#5e4727", "#b08a52")], ''),
    ("community-hands", "Community · Venik ritual", 800, 1000,
     [("#3a1f12", "#b5651d", "#e4572e")], ''),
]


def grad(id, stops, w, h):
    """Linear gradient from stops list."""
    s = stops[0]
    c = ', '.join(
        f'<stop offset="{i/(len(s)-1)*100:.0f}%" stop-color="{color}"/>'
        for i, color in enumerate(s)
    )
    return f'''<linearGradient id="{id}" x1="0" y1="0" x2="{w}" y2="{h}" gradientUnits="userSpaceOnUse">{c}</linearGradient>'''


def svg(filename, label, w, h, stops, icon=''):
    gid = f"g_{filename.replace('-', '_')}"
    g = grad(gid, stops, w, h)
    # subtle texture overlay
    texture = f'''
      <rect width="{w}" height="{h}" fill="url(#{gid})"/>
      <rect width="{w}" height="{h}" fill="url(#{gid})" opacity="0.5"/>
      <!-- subtle grain -->
      <filter id="grain_{gid}">
        <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" result="noise"/>
        <feColorMatrix in="noise" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.06 0"/>
      </filter>
      <rect width="{w}" height="{h}" filter="url(#grain_{gid})"/>
    '''
    # Label block at bottom
    label_block = f'''
      <rect x="40" y="{h-90}" width="{len(label)*12+32}" height="50" rx="8"
            fill="#0d0b09" fill-opacity="0.72"/>
      <text x="56" y="{h-57}" font-family="ui-sans-serif, system-ui, sans-serif"
            font-size="20" fill="#f1e7d0" font-weight="500">{label}</text>
    '''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>{g}</defs>
  {texture}
  {label_block}
</svg>
'''


for img in images:
    fn, *rest = img
    content = svg(fn, *rest)
    path = os.path.join(OUT, fn + '.svg')
    with open(path, 'w') as f:
        f.write(content)
    print(f"  wrote {fn}.svg  ({rest[1]}×{rest[2]})")

print(f"\nGenerated {len(images)} placeholder images in {OUT}")
