#!/usr/bin/env python3
"""Build one guide: Markdown -> HTML (pandoc) -> PDF (Chrome headless).

Two passes: the first render finds which page each chapter starts on
(via pdftotext), the second fills those numbers into the contents page.
Chapters are numbered automatically from their order in the Markdown.

usage: build_guide.py <in.md> <out.pdf> --title "Doc title"
"""
import argparse, html, os, re, shutil, subprocess, sys, tempfile

CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = os.path.join(ROOT, "guides", "assets", "guide.css")


def pandoc(md, out_html, title):
    subprocess.run(["pandoc", md, "-f", "markdown", "-t", "html5", "-s",
                    "--css", CSS, "--embed-resources", "--syntax-highlighting=none",
                    "--metadata", f"pagetitle={title}", "-o", out_html], check=True)


def chrome(in_html, out_pdf):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={out_pdf}", "file://" + in_html],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def number_chapters(doc):
    """Prefix every chapter <h1 id=...> with a number chip; return doc + chapter list."""
    chapters = []

    def sub(m):
        attrs, text = m.group(1), m.group(2)
        if "unnumbered" in attrs or 'id="' not in attrs:
            return m.group(0)
        n = len(chapters) + 1
        cid = re.search(r'id="([^"]+)"', attrs).group(1)
        plain = html.unescape(re.sub(r"<[^>]+>", "", text)).strip()
        chapters.append((cid, n, plain))
        return f'<h1{attrs}><span class="n">{n:02d}</span>{text}<span class="mk">@@ch-{cid}@@</span></h1>'

    doc = re.sub(r"<h1([^>]*)>(.*?)</h1>", sub, doc, flags=re.S)
    return doc, chapters


def parts_before(doc, chapters):
    """Map chapter id -> part label if a .part block sits right before it."""
    out = {}
    for m in re.finditer(r'<div class="part"[^>]*data-part="([^"]+)"[^>]*data-title="([^"]+)"', doc):
        nxt = re.search(r'<h1 id="([^"]+)"', doc[m.end():])
        if nxt:
            out[nxt.group(1)] = (m.group(1), m.group(2))
    return out


def toc_html(chapters, parts, pages):
    rows = []
    for cid, n, title in chapters:
        if cid in parts:
            p, t = parts[cid]
            rows.append(f'<li class="toc-part"><span>{html.escape(p)}</span> {html.escape(t)}</li>')
        pg = pages.get(cid, "00")
        rows.append(f'<li><a href="#{cid}"><span class="tn">{n:02d}</span>'
                    f'<span class="tt">{html.escape(title)}</span><span class="dots"></span>'
                    f'<span class="tp">{pg}</span></a></li>')
    return '<ol class="toc-list">' + "".join(rows) + "</ol>"


def page_texts(pdf):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
    texts = []
    for i in range(1, n + 1):
        t = subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), "-layout", pdf, "-"],
                           capture_output=True, text=True).stdout
        texts.append(re.sub(r"\s+", " ", t))
    return texts


def find_pages(pdf, chapters):
    texts = page_texts(pdf)
    pages, start = {}, 1  # never match the cover
    for cid, n, title in chapters:
        needle = f"@@ch-{cid}@@"  # invisible marker printed inside each chapter heading
        for i in range(start, len(texts)):
            if needle in texts[i]:
                pages[cid] = str(i + 1)
                start = i
                break
        else:
            sys.exit(f"build_guide: could not find chapter '{needle}' in {pdf}")
    return pages


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("md"); ap.add_argument("pdf"); ap.add_argument("--title", required=True)
    a = ap.parse_args()
    if not shutil.which("pdftotext") or not shutil.which("pdfinfo"):
        sys.exit("build_guide: poppler (pdftotext, pdfinfo) is required for contents page numbers; brew install poppler")
    with tempfile.TemporaryDirectory() as tmp:
        build(a, tmp)
    if re.search(rb"file://", open(a.pdf, "rb").read()):
        sys.exit(f"build_guide: {a.pdf} contains a file:// link (a relative link leaked a local path); use an absolute URL")


def build(a, tmp):
    raw = os.path.join(tmp, "raw.html")
    pandoc(a.md, raw, a.title)
    doc = open(raw, encoding="utf-8").read()
    doc, chapters = number_chapters(doc)
    parts = parts_before(doc, chapters)
    has_toc = '<div id="toc"></div>' in doc
    out_html = os.path.join(tmp, "doc.html")

    def write(pages, markers):
        d = doc.replace('<div id="toc"></div>', '<div id="toc">' + toc_html(chapters, parts, pages) + "</div>")
        if not markers:
            d = re.sub(r'<span class="mk">@@ch-[^@]+@@</span>', "", d)
        open(out_html, "w", encoding="utf-8").write(d)

    if has_toc:
        write({}, True)  # pass 1: invisible markers locate each chapter's page
        chrome(out_html, a.pdf)
        pages = find_pages(a.pdf, chapters)
        write(pages, False)  # pass 2: real numbers, markers stripped from the text layer
        chrome(out_html, a.pdf)
        texts = page_texts(a.pdf)
        for cid, n, title in chapters:
            needle = re.sub(r"\s+", " ", f"{n:02d} {title}")
            if needle not in texts[int(pages[cid]) - 1]:
                sys.exit(f"build_guide: chapter '{needle}' moved off page {pages[cid]} in the final pass")
    else:
        write({}, False)
        chrome(out_html, a.pdf)
    print(f"built {a.pdf}: {len(chapters)} chapters")


if __name__ == "__main__":
    main()
