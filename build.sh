#!/usr/bin/env bash
# Rebuild every PDF from source.
# Needs: pandoc 3.8+, Google Chrome, python3, poppler (pdftotext/pdfinfo/pdftoppm for
# contents page numbers, page checks and README cover images).
#   macOS: brew install pandoc poppler
# Override the browser with CHROME=/path/to/chrome ./build.sh
set -euo pipefail
cd "$(dirname "$0")"
export CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"

python3 tools/build_guide.py guides/openclaw-bible.md openclaw-bible.pdf --title "The OpenClaw Bible"
python3 tools/build_guide.py guides/openclaw-full-stack.md openclaw-full-stack.pdf --title "OpenClaw Full Stack"
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=start-here/ai-chief-of-staff-starter.pdf \
  "file://$PWD/start-here/ai-chief-of-staff-starter.html" >/dev/null 2>&1
echo "built start-here/ai-chief-of-staff-starter.pdf"

# README cover thumbnails
if command -v pdftoppm >/dev/null; then
  pdftoppm -png -r 60 -f 1 -l 1 -singlefile openclaw-bible.pdf docs/openclaw-bible-cover
  pdftoppm -png -r 60 -f 1 -l 1 -singlefile openclaw-full-stack.pdf docs/openclaw-full-stack-cover
  pdftoppm -png -r 60 -f 1 -l 1 -singlefile start-here/ai-chief-of-staff-starter.pdf docs/starter-cover
else
  echo "WARNING: pdftoppm (poppler) not found: README covers and page-fill check skipped"
fi

# Layout check: flags any body page under ~70% full (cover and last page exempt).
# It only warns: a green build does not mean the layout passed, read the output.
if command -v pdftoppm >/dev/null; then
  for f in openclaw-bible.pdf openclaw-full-stack.pdf; do
    last=$(pdfinfo "$f" | awk '/^Pages:/{print $2}')
    echo "--- $f ($last pages)"
    python3 tools/check_pages.py "$f" --skip "1,$last" || echo "WARNING: under-filled page(s) in $f"
  done
fi
