#!/usr/bin/env python3
"""Extract text from pdf/Le-Nam-Phuong.pdf and inject into index.html between markers.

Usage:
  python scripts/extract_pdf_to_html.py

Creates a backup of `index.html` as `index.html.bak` before writing.
"""
from pathlib import Path
import re
import html
import sys

try:
    import pdfplumber
except Exception as e:
    print("Missing dependency: pdfplumber. Install with: pip install -r requirements.txt")
    raise

BASE = Path(__file__).resolve().parents[1]
PDF_PATH = BASE / 'pdf' / 'Le-Nam-Phuong.pdf'
HTML_PATH = BASE / 'index.html'

def extract_text(pdf_path: Path) -> str:
    parts = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for p in pdf.pages:
            t = p.extract_text()
            if t:
                parts.append(t)
    return "\n\n".join(parts)

def text_to_html_block(text: str, max_paragraphs: int = 6) -> str:
    # sanitize & convert line breaks to paragraphs
    escaped = html.escape(text.strip())
    paras = escaped.split('\n\n')
    paras = [p.replace('\n', '<br/>') for p in paras if p.strip()]
    if len(paras) > max_paragraphs:
        paras = paras[:max_paragraphs]
        paras.append('... (Xem file PDF để xem đầy đủ)')
    return '\n'.join(f'<p>{p}</p>' for p in paras)

def replace_between_markers(html_path: Path, new_html_block: str) -> bool:
    s = html_path.read_text(encoding='utf-8')
    pattern = re.compile(r'<!--PDF_CONTENT_START-->.*?<!--PDF_CONTENT_END-->', re.S)
    replacement = '<!--PDF_CONTENT_START-->\n' + new_html_block + '\n<!--PDF_CONTENT_END-->'
    if not pattern.search(s):
        print('Markers not found in', html_path)
        return False
    # backup
    bak = html_path.with_name(html_path.name + '.bak')
    bak.write_text(s, encoding='utf-8')
    s2 = pattern.sub(replacement, s, count=1)
    html_path.write_text(s2, encoding='utf-8')
    return True

def main():
    if not PDF_PATH.exists():
        print('PDF not found at', PDF_PATH)
        sys.exit(1)
    print('Extracting text from', PDF_PATH)
    text = extract_text(PDF_PATH)
    if not text.strip():
        print('No text extracted from PDF.')
        sys.exit(1)
    html_block = text_to_html_block(text)
    ok = replace_between_markers(HTML_PATH, html_block)
    if ok:
        print('index.html updated. Backup saved as', HTML_PATH.name + '.bak')
    else:
        print('Update failed: markers not found.')

if __name__ == '__main__':
    main()
