# -*- coding: utf-8 -*-
"""Parse _toc.md into per-book (title, printed page) entries and bucket them by chapter."""
import re, json, os, pprint

TOC = r"C:\Users\LENOVO\Downloads\新建文件夹\extracted\_toc.md"
EXTRACTED = r"C:\Users\LENOVO\Downloads\新建文件夹\extracted"

BOOK_FILES = {
    "PDSH": "python-data-science-handbook-jake-vanderplas-pdf.txt",
    "Cpp": "learning-modern-c-for-finance-foundations-for-quantitative-programming.txt",
    "NLP": "4b075e106d7a719945f8fadfe2e5cb7d-pdf.txt",
    "MLCK": "machine-learning-with-python-codebook-pdf.txt",
    "LLM": "hands-on-llm-serving-and-optimization-hosting-llms-at-scale-chi-wang-p.txt",
    "DLF": "deep-learning-for-finance-creating-machine-deep-learning-models-for-tr.txt",
    "RLF": "reinforcement-learning-for-finance-a-python-based-introduction-yves-j-.txt",
    "FTP": "financial-theory-with-python-a-gentle-introduction-yves-hilpisch-pdf.txt",
}

OFFSET = {"PDSH": 18, "Cpp": 22, "NLP": 22, "LLM": 18, "DLF": 16, "RLF": 14, "FTP": 16, "MLCK": 8}

# chapter start pages (PDF)
CHAPTERS = {
    "PDSH": [19, 51, 115, 235, 349],
    "Cpp": [23, 55, 85, 125, 165, 199, 247, 299, 345, 379],
    "NLP": [23, 55, 79, 111, 143, 173, 205, 229, 265, 289, 317, 345, 381],
    "LLM": [19, 49, 83, 125, 175, 207, 251, 289, 311, 333],
    "DLF": [17, 35, 51, 97, 151, 167, 193, 231, 265, 293, 307, 341],
    "RLF": [17, 33, 51, 65, 81, 99, 119, 143, 181, 203],
    "FTP": [17, 33, 75, 99, 133, 163, 185],
    "MLCK": [9, 27, 42, 77, 96, 108, 125, 138, 168, 180, 190, 217, 230, 240, 259, 270, 276, 286, 293, 301, 312, 344, 354],
}


def load_toc():
    cur = None
    out = {}
    for line in open(TOC, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("## "):
            cur = line[3:].split()[0]
            out.setdefault(cur, [])
        elif cur and line.startswith("  ") and "p." in line:
            title, _, page = line.strip().rpartition("p.")
            title = title.strip()
            if not page.isdigit():
                continue
            if len(title) < 2:
                continue
            out[cur].append((title, int(page)))
    return out


SKIP = {"Preface", "Table of Contents", "Index", "Colophon"}


def clean_title(t):
    t = t.replace("\ufffd", "'")
    # glued chapter headings like "Books 312.Introduction to NumPy"
    m = re.search(r"\b\d{2,3}\.(\S.*)$", t)
    if m and len(m.group(1)) > 3:
        t = m.group(1)
    t = re.sub(r"\s+", " ", t).strip(" .·")
    return t


def body_headings(key):
    """For MLCK: pull '1.2 Creating a Matrix' headings with PDF pages."""
    path = os.path.join(EXTRACTED, BOOK_FILES[key])
    txt = open(path, encoding="utf-8").read()
    parts = re.split(r"=== PAGE (\d+) ===", txt)
    pages = {int(parts[i]): parts[i + 1] for i in range(1, len(parts), 2)}
    found = []
    for p in sorted(pages):
        for line in pages[p].splitlines():
            m = re.match(r"^\s*(\d{1,2})\.(\d{1,2})\s+([A-Z][^\n]{2,70})$", line)
            if m:
                found.append(("%s.%s %s" % (m.group(1), m.group(2), m.group(3).strip()), p))
    # dedupe by title, keep first page
    seen, out = set(), []
    for t, p in found:
        if t in seen:
            continue
        seen.add(t)
        out.append((t, p))
    return out


def main():
    toc = load_toc()
    result = {}
    for key, chs in CHAPTERS.items():
        off = OFFSET[key]
        entries = []
        if key == "MLCK":
            entries = body_headings(key)                      # already PDF pages
        else:
            for t, p in toc.get(key, []):
                entries.append((clean_title(t), p + off))     # printed -> PDF
        # bucket
        buckets = [[] for _ in chs]
        for t, pdfp in entries:
            idx = -1
            for i, c in enumerate(chs):
                if pdfp >= c:
                    idx = i
            if idx >= 0:
                if pdfp == chs[idx]:
                    continue          # 章标题本身
                if buckets[idx] and buckets[idx][-1][0] == t:
                    continue
                # 页码倒退说明是误抓（页眉、断行），丢掉
                if buckets[idx] and pdfp < buckets[idx][-1][1] - 2:
                    continue
                buckets[idx].append((t, pdfp))
        result[key] = buckets
    for key in ["PDSH", "FTP", "MLCK", "NLP"]:
        print("=====", key, [len(b) for b in result[key]])
        for i, b in enumerate(result[key][:3], 1):
            print(" ch%d:" % i, b[:8])
    ids = {"PDSH": "01", "MLCK": "02", "NLP": "03", "LLM": "04",
           "FTP": "05", "RLF": "06", "DLF": "07", "Cpp": "08"}
    out = {}
    for key, buckets in result.items():
        cleaned = []
        for b in buckets:
            keep, prev = [], None
            for t, pg in b:
                t = clean_title(t)
                if not t or t in SKIP:
                    continue
                if prev and (t == prev or t.lower() in prev.lower() and len(t) < len(prev)):
                    continue
                keep.append([t, pg])
                prev = t
            cleaned.append(keep)
        out[ids[key]] = cleaned
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "sections.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("saved sections.json")


if __name__ == "__main__":
    main()
