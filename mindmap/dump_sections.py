# -*- coding: utf-8 -*-
"""Dump per-section text snippets so an agent can extract key points.

Usage: python dump_sections.py <bid> [chars]
Writes i18n/snip/b<bid>.txt : one block per section
  #<chapter>.<section> <english title> | <中文> | p<page>
  <first N chars of that section's text, whitespace-collapsed>
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SEC = json.load(open(os.path.join(HERE, "sections.json"), encoding="utf-8"))

FILES = {
    "01": "python-data-science-handbook-jake-vanderplas-pdf.txt",
    "02": "machine-learning-with-python-codebook-pdf.txt",
    "03": "4b075e106d7a719945f8fadfe2e5cb7d-pdf.txt",
    "04": "hands-on-llm-serving-and-optimization-hosting-llms-at-scale-chi-wang-p.txt",
    "05": "financial-theory-with-python-a-gentle-introduction-yves-hilpisch-pdf.txt",
    "06": "reinforcement-learning-for-finance-a-python-based-introduction-yves-j-.txt",
    "07": "deep-learning-for-finance-creating-machine-deep-learning-models-for-tr.txt",
    "08": "learning-modern-c-for-finance-foundations-for-quantitative-programming.txt",
}
EX = r"C:\Users\LENOVO\Downloads\新建文件夹\extracted"


def load_pages(path):
    txt = open(path, encoding="utf-8").read()
    parts = re.split(r"=== PAGE (\d+) ===", txt)
    return {int(parts[i]): parts[i + 1] for i in range(1, len(parts), 2)}


def main():
    bid = sys.argv[1]
    nchars = int(sys.argv[2]) if len(sys.argv) > 2 else 700
    pages = load_pages(os.path.join(EX, FILES[bid]))
    zh = json.load(open(os.path.join(HERE, "i18n", "zh", "b%s.json" % bid), encoding="utf-8"))
    os.makedirs(os.path.join(HERE, "i18n", "snip"), exist_ok=True)
    out = []
    rows = SEC[bid]
    for ci, secs in enumerate(rows, 1):
        for si, (title, page) in enumerate(secs, 1):
            nxt = None
            if si < len(secs):
                nxt = secs[si][1]
            else:
                nxt = page + 3
            body = " ".join(pages.get(p, "") for p in range(page, min(nxt, page + 4)))
            body = re.sub(r"\s+", " ", body).strip()
            zsec = zh["sections_zh"][ci - 1]
            zt = zsec[si - 1] if si - 1 < len(zsec) else ""
            out.append("#%d.%d %s | %s | p%d\n%s\n" % (ci, si, title, zt, page, body[:nchars]))
    p = os.path.join(HERE, "i18n", "snip", "b%s.txt" % bid)
    open(p, "w", encoding="utf-8").write("\n".join(out))
    print(bid, "sections", sum(len(r) for r in rows), "->", p, os.path.getsize(p) // 1024, "KB")


if __name__ == "__main__":
    main()
