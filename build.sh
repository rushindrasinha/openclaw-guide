#!/usr/bin/env bash
# Rebuild the PDFs from source. Needs pandoc and Google Chrome.
set -euo pipefail
cd "$(dirname "$0")"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
TMP="$(mktemp -d)"
render() { "$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="$2" "file://$1" 2>/dev/null; }
pandoc guides/openclaw-bible.md -s --css guides/assets/guide.css --metadata pagetitle="OpenClaw Bible" --embed-resources -o "$TMP/bible.html"
pandoc guides/openclaw-full-stack.md -s --css guides/assets/guide-compact.css --metadata pagetitle="OpenClaw Full Stack" --embed-resources -o "$TMP/fullstack.html"
render "$TMP/bible.html" openclaw-bible.pdf
render "$TMP/fullstack.html" openclaw-full-stack.pdf
render "$PWD/start-here/ai-chief-of-staff-starter.html" start-here/ai-chief-of-staff-starter.pdf
echo "Built: openclaw-bible.pdf, openclaw-full-stack.pdf, start-here/ai-chief-of-staff-starter.pdf"
