# -*- coding: utf-8 -*-
"""把仓库里的课程/概念/书单打包成插件用的单个 content.json。

用法：python scripts/pack_content.py
输出：content/content.json
"""
import ast, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)            # plugin/
REPO = os.path.dirname(ROOT)            # repo root
COURSE = os.path.join(REPO, "course")
MINDMAP = os.path.join(REPO, "mindmap")
GRAPH = os.path.join(REPO, "graph")

VERSION = "0.3.0"


def load(path):
    return json.load(open(path, encoding="utf-8"))


def literals_from_builder():
    """从 build_course.py 里取 INTROS / BOOKS（它们仍是源码字面量）。"""
    src = open(os.path.join(COURSE, "build_course.py"), encoding="utf-8").read()
    tree = ast.parse(src)
    out = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id in ("INTROS", "BOOKS", "LESSON_BOOKS"):
                    out[t.id] = ast.literal_eval(node.value)
    return out


NEXT_TRACK = {
    "llm": {"id": "eng", "why": "LLM 线讲「怎么用起来」，工程线（eng1–eng6）讲「怎么不崩」：评估、RAG、结构化输出、安全"},
}


def build_tracks():
    llm = load(os.path.join(COURSE, "llm_lessons.json"))
    quant = load(os.path.join(COURSE, "lessons.json"))
    rl = load(os.path.join(COURSE, "rl_stage.json"))
    nlp = load(os.path.join(COURSE, "nlp_lessons.json"))
    cpp = load(os.path.join(COURSE, "cpp_lessons.json"))
    eng = load(os.path.join(COURSE, "eng_lessons.json"))
    starters = [load(os.path.join(COURSE, f)) for f in
                ("starter_lesson.json", "starter_vars.json", "starter_control.json")]

    lit = literals_from_builder()
    intros = lit["INTROS"]

    q_stages = list(quant["stages"]) + [rl["stage"]]
    raw = [
        ("llm", "LLM 线", llm["sub"], llm["stages"], intros["llm"]),
        ("quant", "量化线", "10 关 + 3 关起步", q_stages, intros["quant"]),
        ("nlp", "文本线", nlp["sub"], nlp["stages"], intros["nlp"]),
        ("cpp", "C++ 线", cpp["sub"], cpp["stages"], intros["cpp"]),
        ("eng", "LLM 工程线", eng["sub"], eng["stages"], intros["eng"]),
    ]

    tracks = []
    for tid, name, sub, stages, intro in raw:
        out_stages = []
        for si, st in enumerate(stages):
            lessons = []
            src_lessons = st["lessons"]
            if si == 0:
                src_lessons = starters + src_lessons
            for l in src_lessons:
                lessons.append({
                    "id": l["id"], "title": l["title"], "min": l["min"],
                    "hook": l["hook"], "goals": l["goals"], "concepts": l["concepts"],
                    "steps": l["steps"], "quiz": l["quiz"], "can": l["can"],
                })
            out_stages.append({"name": st["name"], "hint": st.get("hint", ""), "lessons": lessons})
        tracks.append({"id": tid, "name": name, "sub": sub, "intro": intro, "stages": out_stages,
                       "next": NEXT_TRACK.get(tid)})
    return tracks


def main():
    tracks = build_tracks()
    concepts = load(os.path.join(GRAPH, "concepts.json"))
    readlist = load(os.path.join(COURSE, "readlist.json"))
    readback = load(os.path.join(COURSE, "readback.json"))
    sections = load(os.path.join(MINDMAP, "sections.json"))
    lit = literals_from_builder()

    lessons = [l for t in tracks for s in t["stages"] for l in s["lessons"]]
    content = {
        "version": VERSION,
        "meta": {
            "title": "8 本书 · 学习路线",
            "description": "4 条路线 41 关，配套 51 个概念与 8 本书的章节索引",
            "tracks": [{"id": t["id"], "name": t["name"], "sub": t["sub"],
                        "count": sum(len(s["lessons"]) for s in t["stages"]),
                        "minutes": sum(l["min"] for s in t["stages"] for l in s["lessons"])} for t in tracks],
        },
        "tracks": tracks,
        "lessons": {l["id"]: l for l in lessons},
        "concepts": concepts,
        "books": lit["BOOKS"],
        "readlist": readlist,
        "readback": readback,
        "lesson_books": lit["LESSON_BOOKS"],
        "sections": sections,
    }

    # 校验
    problems = []
    for l in lessons:
        if not (2 <= len(l["concepts"]) <= 4):
            problems.append(l["id"] + ": 概念数 %d" % len(l["concepts"]))
        if not (1 <= len(l["steps"]) <= 6):
            problems.append(l["id"] + ": 步骤数 %d" % len(l["steps"]))
        if not (2 <= len(l["quiz"]) <= 5):
            problems.append(l["id"] + ": 自测数 %d" % len(l["quiz"]))
        if not l["hook"] or not l["can"]:
            problems.append(l["id"] + ": 缺字段")
    for b in readlist:
        for ch in b["need"]:
            secs = sections.get(b["code"], [])
            if ch["ch"] > len(secs):
                problems.append("%s ch%d 超出章节数" % (b["code"], ch["ch"]))
    if problems:
        print("校验失败：")
        for p in problems[:10]:
            print("  -", p)
        sys.exit(1)

    out = os.path.join(ROOT, "content")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "content.json")
    json.dump(content, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    size = os.path.getsize(path) / 1024
    print("wrote %s (%.0f KB)" % (path, size))
    print("tracks=%d lessons=%d concepts=%d books=%d readchapters=%d sections=%d"
          % (len(tracks), len(lessons), len(concepts["nodes"]), len(readlist),
             sum(len(b["need"]) for b in readlist),
             sum(len(v) for v in sections.values() for _ in [0])))


if __name__ == "__main__":
    main()
