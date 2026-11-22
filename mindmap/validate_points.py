# -*- coding: utf-8 -*-
"""Validate i18n/points/*.json against sections.json."""
import json, os, glob

HERE = os.path.dirname(os.path.abspath(__file__))
SEC = json.load(open(os.path.join(HERE, "sections.json"), encoding="utf-8"))
PTS = os.path.join(HERE, "i18n", "points")

ok = True
tot = 0
for fn in sorted(glob.glob(os.path.join(PTS, "*.json"))):
    base = os.path.basename(fn)
    bid = base[1:3]
    try:
        d = json.load(open(fn, encoding="utf-8"))
    except Exception as e:
        print("BAD JSON", base, e)
        ok = False
        continue
    ncap = 0
    for k, v in d.items():
        try:
            ci, si = [int(x) for x in k.split(".")]
        except Exception:
            print("BAD KEY", base, k)
            ok = False
            continue
        if ci < 1 or ci > len(SEC[bid]):
            print("BAD CHAPTER", base, k)
            ok = False
            continue
        if si < 1 or si > len(SEC[bid][ci - 1]):
            print("BAD SECTION", base, k)
            ok = False
            continue
        if not isinstance(v, list) or not (1 <= len(v) <= 3):
            print("BAD COUNT", base, k, len(v) if isinstance(v, list) else type(v))
            ok = False
            continue
        for p in v:
            if not isinstance(p, str) or not p.strip():
                print("BAD ITEM", base, k)
                ok = False
        ncap += len(v)
    tot += ncap
    print("%-14s %3d keys %4d points" % (base, len(d), ncap))

print("TOTAL points:", tot, "->", "OK" if ok else "HAS ERRORS")
