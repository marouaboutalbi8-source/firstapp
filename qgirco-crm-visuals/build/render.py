# -*- coding: utf-8 -*-
"""Render SVG -> high-res PNG via headless Chromium.
Chromium headless clips ~70px at the window bottom, so we render into a taller
window and crop back to the exact canvas size. Inlines the SVG into an HTML page
(margin:0) for reliable full-canvas rendering.
"""
import glob
import os
import subprocess
import sys
import tempfile

from PIL import Image

SCALE = 2
PAD = 160


def chrome():
    c = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))
    if not c:
        raise SystemExit("chromium not found")
    return c[-1]


def render(svg_path, out_path, w=1760, h=1100):
    with open(svg_path, encoding="utf-8") as f:
        svg = f.read()
    td = tempfile.mkdtemp()
    html = ('<!doctype html><html><head><meta charset="utf-8">'
            '<style>html,body{margin:0;padding:0;background:#fff}'
            'svg{display:block}</style></head><body>' + svg + '</body></html>')
    page = os.path.join(td, "page.html")
    with open(page, "w", encoding="utf-8") as f:
        f.write(html)
    raw = os.path.join(td, "raw.png")
    subprocess.run([
        chrome(), "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
        f"--force-device-scale-factor={SCALE}",
        f"--window-size={w},{h + PAD}",
        f"--screenshot={raw}", page,
    ], check=True, stderr=subprocess.DEVNULL)
    im = Image.open(raw).convert("RGB")
    crop = im.crop((0, 0, w * SCALE, h * SCALE))
    crop.save(out_path)
    print("rendered", out_path, crop.size)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        # explicit pairs: svg out [w h]
        w = int(args[2]) if len(args) > 2 else 1760
        h = int(args[3]) if len(args) > 3 else 1100
        render(args[0], args[1], w, h)
    else:
        os.makedirs("../png", exist_ok=True)
        for svg in sorted(glob.glob("../svg/*.svg")):
            out = "../png/" + os.path.splitext(os.path.basename(svg))[0] + ".png"
            render(svg, out)
