#!/usr/bin/env bash
# Render an SVG to a high-res PNG via headless Chromium using an HTML wrapper
# (margin:0, exact sizing) so the full canvas is captured with no clipping.
set -e
SVG="$1"; OUT="$2"; Wd="${3:-1760}"; Hd="${4:-1100}"
CHROME=$(ls /opt/pw-browsers/chromium-*/chrome-linux/chrome | head -1)
TMP=$(mktemp -d)
cp "$SVG" "$TMP/img.svg"
cat > "$TMP/page.html" <<HTML
<!doctype html><html><head><meta charset="utf-8">
<style>html,body{margin:0;padding:0;background:#ffffff}
img{display:block;width:${Wd}px;height:${Hd}px}</style></head>
<body><img src="img.svg"></body></html>
HTML
"$CHROME" --headless --disable-gpu --no-sandbox --hide-scrollbars \
  --force-device-scale-factor=2 --window-size=${Wd},${Hd} \
  --screenshot="$OUT" "$TMP/page.html" 2>/dev/null
rm -rf "$TMP"
echo "rendered $OUT"
