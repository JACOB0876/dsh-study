# -*- coding: utf-8 -*-
"""四线课程 + 8 本书总表：生成 index.html 与 workbook.html。"""
import json, os, html

HERE = os.path.dirname(os.path.abspath(__file__))


def load(fn):
    p = os.path.join(HERE, fn)
    if not os.path.exists(p):
        return None
    return json.load(open(p, encoding="utf-8"))


LLM = load("llm_lessons.json")
QUANT = load("lessons.json")
RL = load("rl_stage.json")
NLP = load("nlp_lessons.json")
CPP = load("cpp_lessons.json")
ENG = load("eng_lessons.json")

q_stages = list(QUANT["stages"]) if QUANT else []
if RL:
    q_stages.append(RL["stage"])

INTROS = {
    "llm": {
        "why": "把大模型从「在网页上聊天」，变成「接进你自己程序里、能部署、能算账」。",
        "do": ["用 API 做出自己的小工具：抽取字段、分类、问答",
               "在一个需求开始前，算清它要花多少钱、要什么卡",
               "在本机跑起 7B，并给出吞吐和延迟的数字"],
        "who": "想转 AI 工程 / 想给产品加 AI 能力 / 不需要数学背景",
        "need": "完全零基础可以：前 3 关从装 Python 开始；一个 DeepSeek key；后 4 关需要 8GB 显卡",
        "time": "11 关 + 3 关起步，约 6.5 小时；每天一关，三周",
        "not": "不训练模型、不推公式、不做微调",
        "first": "只想看一句话结论：这条线教的是「怎么把模型用起来」，不是「怎么造模型」。",
        "next": ["学完这条线 → 直接进入「LLM 工程线」（eng1–eng6）：评估、RAG、结构化输出、安全",
                 "那 6 关解决的是「演示能跑、上线就崩」，是你这条线之后最该补的一层",
                 "再往后：微调（LoRA）、Agent 与工具调用、多模型路由"]
    },
    "quant": {
        "why": "用数据判断一个交易想法，是真本事，还是运气和幻觉。",
        "do": ["拿到一份行情 CSV，十分钟内算出收益、波动、回撤",
               "看穿一个「回测年化 180%」的骗局，知道钱被什么吃掉了",
               "给一份合约定出可解释的价格，并说清它为什么是这个数"],
        "who": "对市场好奇 / 想自己验证策略 / 想补金融理论",
        "need": "完全零基础可以：前 3 关补 Python；高中数学够用",
        "time": "10 关 + 3 关起步，约 6 小时",
        "not": "不教高频交易、不教盘口和订单簿、不保证能赚钱",
        "first": "这条线最重要的一句：先学会分辨「假的好」，再谈找「真的好」。",
        "next": ["给一个策略写完整的回测报告，能说服别人也说服自己",
                 "往下走：因子研究、组合优化、风控与归因",
                 "再往后：把研究代码搬进 C++ 或向量化引擎，跑实盘数据"]
    },
    "nlp": {
        "why": "把一堆文本（评论、工单、新闻）变成能统计、能分类、能解释的东西。",
        "do": ["在 500 条评论里，五分钟看出大家在抱怨什么",
               "搭一个分类器，并给出一个可信的准确率",
               "把「模型为什么这么判」讲给不写代码的同事听"],
        "who": "手里有文本数据 / 做运营分析 / 想入门 NLP",
        "need": "完全零基础可以：前 3 关补 Python，第 1 关只用到 count 和 plot",
        "time": "5 关 + 3 关起步，约 3.5 小时",
        "not": "不训练大模型、不深入 Transformer 结构",
        "first": "文本分析 80% 的工作在第 1、2 关：看清数据和清洗；模型只占 20%。",
        "next": ["把一批真实评论/工单跑一遍，产出一页结论",
                 "往下走：embedding 检索、向量库、多标签分类",
                 "再往后：接上 LLM 做摘要与抽取，形成完整流水线"]
    },
    "cpp": {
        "why": "把 Python 里「算得太慢」的那一部分，用 C++ 重写——通常快几十倍。",
        "do": ["在本机编译并运行第一个程序，看懂报错",
               "写一个 Black-Scholes 定价类，和 Python 版对同一个数",
               "用并发跑蒙特卡洛，把一亿条路径压进几秒"],
        "who": "想碰生产代码 / 对性能好奇 / 准备量化开发岗",
        "need": "零基础可以：前 3 关补 Python；还需要装编译器（第 1 关给命令）",
        "time": "6 关 + 3 关起步，约 4 小时",
        "not": "不教 C++ 全部语法、不讲模板元编程、不涉及 Boost",
        "first": "这条线可以完全独立学：它和另外三条线几乎不重叠。",
        "next": ["把 Python 里的慢函数改写成 C++，对比耗时",
                 "往下走：Eigen 做矩阵运算、多线程做蒙特卡洛",
                 "再往后：把定价库包成 Python 扩展，给研究端调用"]
    },
    "eng": {
        "why": "把「演示能跑」变成「上线不崩」：评估、检索、结构化输出、安全，这四件工程活。",
        "do": ["建一套 20 条的评估集，用数字比较 prompt 版本",
               "把手头文档做成能问答的 RAG，回答带引用",
               "让模型稳定输出 JSON，接进你的程序"],
        "who": "已经会调 API、准备把模型接进真实流程或产品的人",
        "need": "会 Python、跑通过一次 API 调用（LLM 线前 6 关即可）",
        "time": "6 关，约 3 小时；每关都能直接用在自己的项目上",
        "not": "不训练模型、不微调、不碰 GPU 部署（那是《04 LLM Serving》的事）",
        "first": "一句话：这条线只解决一件事——让模型从「看着挺好」变成「敢给人用」。",
        "next": ["给自己做一个文档问答机器人，带引用和评估集",
                 "往下走：Promptfoo 做回归测试、DPO 做领域对齐（第 8 章）",
                 "再往后：多模型路由、成本与延迟优化"]
    },
}


STARTERS = [json.load(open(os.path.join(HERE, fn), encoding="utf-8"))
            for fn in ("starter_lesson.json", "starter_vars.json", "starter_control.json")]

TRACKS = []
if LLM:
    TRACKS.append({"id": "llm", "name": "LLM 线", "sub": LLM["sub"], "stages": LLM["stages"],
                   "intro": INTROS["llm"]})
if q_stages:
    TRACKS.append({"id": "quant", "name": "量化线", "sub": "10 关 · 算账 → 判断 → 回测 → 定价 → 决策",
                   "stages": q_stages, "intro": INTROS["quant"]})
if NLP:
    TRACKS.append({"id": "nlp", "name": "文本线", "sub": NLP["sub"], "stages": NLP["stages"],
                   "intro": INTROS["nlp"]})
if CPP:
    TRACKS.append({"id": "cpp", "name": "C++ 线", "sub": CPP["sub"], "stages": CPP["stages"],
                   "intro": INTROS["cpp"]})
if ENG:
    TRACKS.append({"id": "eng", "name": "LLM 工程线", "sub": ENG["sub"], "stages": ENG["stages"],
                   "intro": INTROS["eng"]})


READLIST = json.load(open(os.path.join(HERE, "readlist.json"), encoding="utf-8"))

BOOKS = [
    {"code": "01", "short": "PDSH", "zh": "Python 数据科学手册", "role": "工具底座 A",
     "need": "零基础起点，不需要前置", "rel": "与 02 二选一（内容重叠约 60%）",
     "cover": "量化 1–3 关 · LLM 线 1 关", "tip": "先读第 3 章 pandas 和第 5 章 sklearn，其余当手册查。"},
    {"code": "02", "short": "MLCK", "zh": "Python 机器学习经典实例", "role": "工具底座 B（配方集）",
     "need": "会一点 pandas 即可", "rel": "与 01 二选一；23 章可跳读",
     "cover": "量化线 5 关（评估与选择）", "tip": "当字典用：遇到具体问题查对应配方，不要从头读。"},
    {"code": "03", "short": "NLP", "zh": "Python 文本分析实战", "role": "文本工程线",
     "need": "pandas 基础", "rel": "独立；LLM 线只借用 embedding/分类两关",
     "cover": "文本线 5 关", "tip": "重点第 1、4、5、6 章；抓数据那两章可以跳。"},
    {"code": "04", "short": "LLM", "zh": "LLM 服务与优化实战", "role": "推理部署线",
     "need": "Python + 一点神经网络概念", "rel": "独立栈，不依赖任何金融书",
     "cover": "LLM 线 8 关", "tip": "第 5–8 章是核心：瓶颈、优化、框架、实战。"},
    {"code": "05", "short": "FTP", "zh": "Python 金融理论", "role": "定价理论",
     "need": "会写函数、懂一点概率", "rel": "是 06 的上游（第 7 章动态对冲要用它）",
     "cover": "量化线 7–8 关", "tip": "204 页最短，建议整本读完，跳了会断。"},
    {"code": "06", "short": "RLF", "zh": "面向金融的强化学习", "role": "决策 / 强化学习",
     "need": "05 的 BSM 与蒙特卡洛 + 神经网络", "rel": "全套装唯一有真上游的书",
     "cover": "量化线 9–10 关", "tip": "第 2、3、7 章最重要；第 4–5 章造数据可跳。"},
    {"code": "07", "short": "DLF", "zh": "面向金融的深度学习", "role": "策略流水线",
     "need": "pandas + sklearn（01/02）", "rel": "与 05 无耦合（全书 0 次 Black-Scholes）",
     "cover": "量化线 5–6 关", "tip": "第 3、7、8、9 章是主干；前 6 章可快读。"},
    {"code": "08", "short": "C++", "zh": "面向金融的现代 C++", "role": "工程技能线",
     "need": "会一点编程即可，不需要前置金融知识", "rel": "与其余 7 本几乎不重叠，可单独学",
     "cover": "C++ 线 6 关", "tip": "第 1、2、3、6、8 章精读；STL 两章按需查。"},
    {
        "code": "09",
        "short": "HTP",
        "zh": "大语言模型的硬骨头",
        "role": "工程实践线（进阶）",
        "need": "会 Python、调过 API（LLM 线前 6 关的水平）",
        "rel": "接在《04 LLM》之后：04 讲推理怎么跑，这本讲应用怎么不崩",
        "cover": "LLM 工程线 6 关（待建）",
        "tip": "第 2、4、5 章精读；第 1、6、7 章按需；第 8 章当案例读。",
    },
]

for _t in TRACKS:
    for _i, _ls in enumerate(STARTERS):
        _t["stages"][0]["lessons"].insert(_i, _ls)


# 关卡 → 回书指引：purpose ∈ 佐证 / 拓展 / 推导 / 查漏
READBACK = json.load(open(os.path.join(HERE, "readback.json"), encoding="utf-8"))

LESSON_BOOKS = {
    "llm1": [
        [
            "01",
            1
        ]
    ],
    "llm2": [
        [
            "04",
            1
        ]
    ],
    "llm3": [
        [
            "04",
            2
        ]
    ],
    "llm4": [
        [
            "03",
            10
        ]
    ],
    "llm5": [
        [
            "03",
            6
        ]
    ],
    "llm6": [
        [
            "04",
            5
        ]
    ],
    "llm7": [
        [
            "04",
            6
        ]
    ],
    "llm8": [
        [
            "04",
            9
        ]
    ],
    "l1": [
        [
            "01",
            1
        ]
    ],
    "l2": [
        [
            "01",
            3
        ]
    ],
    "l3": [
        [
            "01",
            4
        ]
    ],
    "l4": [
        [
            "07",
            3
        ]
    ],
    "l5": [
        [
            "02",
            11
        ]
    ],
    "l6": [
        [
            "07",
            7
        ]
    ],
    "l7": [
        [
            "05",
            2
        ]
    ],
    "l8": [
        [
            "05",
            5
        ]
    ],
    "rl1": [
        [
            "06",
            2
        ]
    ],
    "rl2": [
        [
            "06",
            7
        ]
    ],
    "nlp1": [
        [
            "03",
            1
        ]
    ],
    "nlp2": [
        [
            "03",
            4
        ]
    ],
    "nlp3": [
        [
            "03",
            5
        ]
    ],
    "nlp4": [
        [
            "03",
            6
        ]
    ],
    "nlp5": [
        [
            "03",
            8
        ]
    ],
    "cpp1": [
        [
            "08",
            1
        ]
    ],
    "cpp2": [
        [
            "08",
            2
        ]
    ],
    "cpp3": [
        [
            "08",
            3
        ]
    ],
    "cpp4": [
        [
            "08",
            5
        ]
    ],
    "cpp5": [
        [
            "08",
            6
        ]
    ],
    "cpp6": [
        [
            "08",
            8
        ]
    ],
    "eng1": [["09", 1]], "eng2": [["09", 2]], "eng3": [["09", 2]],
    "eng4": [["09", 4]], "eng5": [["09", 5]], "eng6": [["09", 6]],
    "llm0a": [["04", 2]], "llm0b": [["04", 1]], "llm0c": [["04", 2]],
}

BY_ORDER = {"nlp": [(3, 1), (3, 4), (3, 5), (3, 6), (3, 8)],
            "cpp": [(8, 1), (8, 2), (8, 3), (8, 4), (8, 6), (8, 8)]}
for t in TRACKS:
    if t["id"] in BY_ORDER:
        seq = BY_ORDER[t["id"]]
        k = 0
        for s in t["stages"]:
            for l in s["lessons"]:
                if l["id"] in ("start", "vars", "control"):
                    continue
                if k < len(seq):
                    LESSON_BOOKS[l["id"]] = [seq[k]]
                k += 1

HTML = r"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<title>8 本书 · 学习路线</title>
<style>
  :root{--bg:#f7f9fc;--ink:#0f172a;--muted:#64748b;--line:#e2e8f0;--accent:#2563eb;--ok:#059669}
  *{box-sizing:border-box}
  html,body{margin:0;height:100%;background:var(--bg);color:var(--ink);
    font-family:"Segoe UI","Microsoft YaHei","PingFang SC",system-ui,sans-serif}
  #app{display:flex;height:100%}
  aside{width:300px;flex:0 0 300px;background:#fff;border-right:1px solid var(--line);
    display:flex;flex-direction:column;overflow:auto}
  aside .top{padding:14px 16px 12px;border-bottom:1px solid #eef2f7}
  .tabs{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-bottom:12px}
  .tab{text-align:center;font-size:12.5px;padding:8px 0;border-radius:9px;cursor:pointer;
    border:1px solid #dbe3ee;color:#475569;background:#fff;font-weight:600}
  .tab.on{background:#0f172a;color:#fff;border-color:#0f172a}
  .tab.wide{grid-column:1 / -1}
  aside h1{font-size:15px;margin:0 0 4px;font-weight:700}
  aside .sub{font-size:11.5px;color:var(--muted);line-height:1.6}
  .bar{height:6px;background:#eef2f7;border-radius:6px;margin-top:12px;overflow:hidden}
  .bar i{display:block;height:100%;background:linear-gradient(90deg,#60a5fa,#2563eb);width:0;transition:width .3s}
  .pct{font-size:11px;color:var(--muted);margin-top:6px;display:flex;justify-content:space-between}
  .pct span:last-child{cursor:pointer;color:#2563eb}
  .stage{padding:13px 16px 6px;font-size:11px;color:#94a3b8;letter-spacing:.6px;font-weight:600}
  .stage .hint{display:block;color:#b6c2d1;font-weight:400;letter-spacing:0;margin-top:3px}
  .lesson{display:flex;gap:10px;align-items:flex-start;padding:9px 16px;cursor:pointer;
    border-left:3px solid transparent;font-size:13px;color:#334155;line-height:1.5}
  .lesson:hover{background:#f8fafc}
  .lesson.active{background:#eff6ff;border-left-color:var(--accent);color:#1d4ed8;font-weight:600}
  .lesson .dot{width:16px;height:16px;border-radius:50%;border:1.5px solid #cbd5e1;flex:0 0 16px;
    margin-top:1px;display:flex;align-items:center;justify-content:center;font-size:10px;color:#fff}
  .lesson.done .dot{background:var(--ok);border-color:var(--ok)}
  .lesson .meta{display:block;font-size:10.5px;color:#94a3b8;margin-top:3px;font-weight:400}
  main{flex:1;overflow:auto;padding:32px 44px 80px;max-width:920px;margin:0 auto}
  .kicker{font-size:11.5px;color:var(--accent);font-weight:700;letter-spacing:1px}
  h2{font-size:27px;margin:8px 0 6px;letter-spacing:.5px}
  .min{font-size:12px;color:var(--muted);margin-bottom:12px}
  .bookchips{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px}
  .bchip{font-size:11.5px;padding:5px 10px;border-radius:20px;background:#eef6ff;color:#1d4ed8;
    text-decoration:none;border:1px solid #dbeafe}
  .bchip:hover{background:#dbeafe}
  .hook{background:#fff;border:1px solid #e2e8f0;border-left:4px solid #93c5fd;border-radius:0 12px 12px 0;
    padding:16px 18px;font-size:15px;line-height:1.9;margin-bottom:22px}
  h3{font-size:14px;margin:30px 0 10px;letter-spacing:.5px;display:flex;align-items:center;gap:8px}
  h3::before{content:"";width:5px;height:16px;background:var(--accent);border-radius:3px}
  ul.goals{margin:0;padding-left:20px;font-size:14px;line-height:1.95}
  .concept{background:#fff;border:1px solid #e8eef6;border-radius:12px;padding:14px 16px;margin:10px 0}
  .concept b{font-size:14px}
  .concept em{font-style:normal;color:#94a3b8;font-size:11.5px;margin-left:6px}
  .concept p{margin:6px 0 0;font-size:13.5px;line-height:1.85;color:#334155}
  .step{margin:16px 0}
  .step .txt{font-size:13.6px;line-height:1.8;margin-bottom:8px}
  pre{background:#0f172a;color:#e2e8f0;padding:14px 16px;border-radius:10px;overflow:auto;
    font-family:Consolas,ui-monospace,monospace;font-size:12.6px;line-height:1.65;margin:0}
  .out{font-size:12.6px;color:#047857;background:#ecfdf5;border:1px solid #a7f3d0;
    border-radius:8px;padding:8px 12px;margin-top:8px;font-family:Consolas,monospace}
  details{background:#fff;border:1px solid #e8eef6;border-radius:10px;padding:11px 14px;margin:8px 0;
    font-size:13.6px;line-height:1.8}
  details summary{cursor:pointer;color:#1d4ed8;font-weight:600}
  details[open] summary{margin-bottom:6px}
  .can{background:#f0f9ff;border:1px solid #bae6fd;border-radius:12px;padding:14px 16px;
    font-size:13.6px;line-height:1.8;margin-top:26px}
  .nav{display:flex;gap:12px;margin-top:30px;align-items:center}
  button{font:inherit;font-size:13.5px;padding:11px 20px;border-radius:10px;border:1px solid #cbd5e1;
    background:#fff;cursor:pointer;color:#334155;transition:.15s}
  button:hover{border-color:#94a3b8;background:#f8fafc}
  button.primary{background:var(--accent);border-color:var(--accent);color:#fff;font-weight:600}
  button.done{background:var(--ok);border-color:var(--ok);color:#fff}
  .spacer{flex:1}
  /* intro */
  .intro .lead{font-size:17px;line-height:1.95;background:#fff;border:1px solid #e2e8f0;
    border-left:4px solid #2563eb;border-radius:0 12px 12px 0;padding:18px 20px;margin-bottom:22px}
  .intro .grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:6px 0 10px}
  .intro .cell{background:#fff;border:1px solid #e8eef6;border-radius:12px;padding:14px 16px;
    font-size:13.4px;line-height:1.85}
  .intro .cell b{display:block;font-size:11px;color:#94a3b8;letter-spacing:1px;margin-bottom:6px}
  .intro .not{background:#fff7ed;border:1px solid #fed7aa;color:#7c2d12;border-radius:12px;
    padding:12px 16px;font-size:13.2px;line-height:1.8;margin-top:14px}
  .intro .start{display:flex;gap:14px;align-items:center;margin-top:26px}
  .readback{margin-top:28px;background:#fcfdff;border:1px solid #e6eef7;border-radius:14px;padding:6px 16px 14px}
  .readback h3{margin:14px 0 8px}
  .rbrow{display:flex;gap:10px;align-items:flex-start;padding:10px 12px;margin:8px 0;border:1px solid #eef2f7;
    border-radius:10px;background:#fff;text-decoration:none;color:#0f172a;transition:.15s}
  .rbrow:hover{border-color:#bfdbfe;transform:translateX(2px)}
  .rbq{display:inline-block;font-size:10.5px;padding:1px 7px;border-radius:20px;margin-right:6px;font-weight:600;white-space:nowrap}
.rbw{display:block;font-style:normal;font-size:10.5px;color:#94a3b8;margin-top:2px}
.rbp{font-size:10.5px;padding:3px 8px;border-radius:20px;border:1px solid;white-space:nowrap;font-weight:600;margin-top:1px}
  .rbt{flex:1;font-size:12.8px;line-height:1.6}
  .rbt b{display:block;font-weight:600}
  .rbt i{font-style:normal;color:#64748b;font-size:11.8px}
  .rbg{font-size:11px;color:#94a3b8;white-space:nowrap;margin-top:2px}
  .rbnote{font-size:11.3px;color:#94a3b8;line-height:1.8;margin-top:6px}
  /* read list */
  .bgrid.rgrid{display:block;column-count:2;column-gap:14px}
  .bgrid.rgrid .bcard{display:inline-block;width:100%;margin:0 0 14px;break-inside:avoid;vertical-align:top}
  @media (max-width: 1180px){.bgrid.rgrid{column-count:1}}
  .rrow{display:flex;gap:10px;align-items:flex-start;padding:9px 10px;border:1px solid #eef2f7;
    border-radius:10px;margin:7px 0;cursor:pointer;background:#fff;transition:.15s}
  .rrow:hover{border-color:#bfdbfe;background:#f8fbff}
  .rrow.on{background:#f0fdf4;border-color:#a7f3d0}
  .rrow input{margin-top:3px;accent-color:#059669;width:15px;height:15px}
  .rrow .rt{flex:1;font-size:12.6px;line-height:1.65}
  .rrow .rt b{display:block;font-weight:600;color:#0f172a}
  .rrow .rt em{font-style:normal;color:#94a3b8;margin-left:6px;font-size:11px}
  .rrow .rt i{display:block;font-style:normal;color:#64748b;font-size:11.5px;margin-top:2px}
  .rrow .rlink{font-size:11px;color:#2563eb;text-decoration:none;white-space:nowrap;margin-top:2px}
  .rskip{font-size:11.8px;color:#94a3b8;margin-top:8px;line-height:1.7}
  .cnt{float:right;color:#2563eb;font-weight:600;letter-spacing:0}
  .bcard .rlist{margin-top:6px}
  /* books view */
  .bgrid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:18px}
  .bcard{background:#fff;border:1px solid #e6ecf4;border-radius:14px;padding:16px 18px}
  .bcard .code{font-size:11px;color:#94a3b8;letter-spacing:1px}
  .bcard h4{margin:4px 0 8px;font-size:16px}
  .bcard .row{font-size:12.8px;color:#475569;line-height:1.8;margin:2px 0}
  .bcard .row b{color:#0f172a;font-weight:600}
  .bcard a{font-size:12px;color:#2563eb;text-decoration:none}
  .bcard a:hover{text-decoration:underline}
  .note{background:#fff7ed;border:1px solid #fed7aa;border-radius:12px;padding:14px 16px;
    font-size:13.4px;line-height:1.85;color:#7c2d12;margin-top:18px}
</style></head><body>
<div id="app">
  <aside>
    <div class="top">
      <div class="tabs" id="tabs"></div>
      <h1 id="tname"></h1>
      <div class="sub" id="tsub"></div>
      <div class="bar" id="barwrap"><i id="barfill"></i></div>
      <div class="pct" id="pctwrap"><span id="pcttext"></span><span id="resume">继续 →</span></div>
    </div>
    <div id="list"></div>
  </aside>
  <main id="main"></main>
</div>
<script>
const DATA = __DATA__;
const BOOKS = __BOOKS__;
const LB = __LB__;
const READBACK = __RB__;
const READ = __READ__;
window.__READ = READ;
const KEY = "course-progress-v3";
let done = {};
try { done = JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch(e) { done = {}; }
let ti = +(localStorage.getItem("course-track-v3") || 0);
if (ti >= DATA.tracks.length) ti = 0;
let cur = 0;
let readDone = {};
try { readDone = JSON.parse(localStorage.getItem("reading-v1") || "{}") || {}; } catch(e) { readDone = {}; }

function track(){ return DATA.tracks[ti]; }
function isBooks(){ return track().kind === "books"; }
function isRead(){ return track().kind === "readlist"; }
function lessons(){ return (isBooks() || isRead()) ? [] : track().stages.flatMap(s => s.lessons.map(l => Object.assign({}, l, {stage: s.name}))); }
function save(){ try{ localStorage.setItem(KEY, JSON.stringify(done)); }catch(e){} }

function renderTabs(){
  document.getElementById("tabs").innerHTML = DATA.tracks.map((t,i) =>
    `<div class="tab ${(t.kind==="books"||t.kind==="readlist")?"wide":""} ${i===ti?"on":""}" data-i="${i}">${t.name}</div>`).join("");
  document.querySelectorAll(".tab").forEach(el => el.onclick = () => {
    ti = +el.dataset.i; try{ localStorage.setItem("course-track-v3", ti); }catch(e){}
    cur = -1; renderTabs(); show(-1);
  });
  document.getElementById("tname").textContent = track().name;
  document.getElementById("tsub").textContent = track().sub;
  const hide = isBooks() || isRead();
  document.getElementById("barwrap").style.display = hide ? "none" : "block";
  document.getElementById("pctwrap").style.display = hide ? "none" : "flex";
}

function updateList(){
  if (isBooks()) { document.getElementById("list").innerHTML = `<div class="stage">8 本书<span class="hint">点右侧卡片里的链接可跳到导图</span></div>`; return; }
  if (isRead()) {
    const total = READ.reduce((n, b) => n + b.need.length, 0);
    const doneN = Object.keys(readDone).filter(k => readDone[k]).length;
    document.getElementById("list").innerHTML =
      `<div class="stage">回书清单<span class="hint">${doneN} / ${total} 章已读</span></div>`;
    return;
  }
  const ls = lessons();
  document.getElementById("list").innerHTML = `
    <div class="lesson ${cur === -1 ? "active" : ""}" data-i="-1">
      <span class="dot">i</span><span>这条线是什么<span class="meta">先看这一页</span></span>
    </div>` + track().stages.map(s => `
    <div class="stage">${s.name}<span class="hint">${s.hint || ""}</span></div>
    ${s.lessons.map(l => {
      const i = ls.indexOf(l);
      const cls = (i === cur ? "active " : "") + (done[l.id] ? "done" : "");
      return `<div class="lesson ${cls}" data-i="${i}">
        <span class="dot">${done[l.id] ? "✓" : ""}</span>
        <span>${l.title}<span class="meta">${l.min} 分钟${done[l.id] ? " · 已完成" : ""}</span></span>
      </div>`;
    }).join("")}`).join("");
  document.querySelectorAll(".lesson").forEach(el => el.onclick = () => show(+el.dataset.i));
  const n = ls.filter(l => done[l.id]).length;
  document.getElementById("pcttext").textContent = `${n} / ${ls.length} 关`;
  document.getElementById("barfill").style.width = (n / ls.length * 100) + "%";
}

const PURPOSE_STYLE = {
  "佐证": ["#eff6ff", "#1d4ed8", "#dbeafe"],
  "拓展": ["#f5f3ff", "#6d28d9", "#ddd6fe"],
  "推导": ["#fffbeb", "#b45309", "#fde68a"],
  "查漏": ["#ecfeff", "#0e7490", "#a5f3fc"]
};

// 必读 / 备查：只有「推导」现在就该读，其余等遇到问题再查
const WHEN_READ = {
  "推导": ["必读", "#fef2f2", "#b91c1c", "现在就值得读——课程只给结论，推导在书里"],
  "佐证": ["备查", "#f1f5f9", "#475569", "想验证这个结论、或写东西要引用时"],
  "拓展": ["备查", "#f1f5f9", "#475569", "等你真要动手做那件事时"],
  "查漏": ["备查", "#f1f5f9", "#475569", "遇到具体问题、出现意外报错时"]
};

function readback(id){
  const refs = LB[id] || [];
  const rb = READBACK[id];
  if (!refs.length || !rb) return "";
  const [purpose, why] = rb;
  const st = PURPOSE_STYLE[purpose] || PURPOSE_STYLE["佐证"];
  const wr = WHEN_READ[purpose] || WHEN_READ["佐证"];
  const rows = refs.map(([code, ch]) => {
    const b = BOOKS.find(x => x.code === code);
    let extra = "";
    const rl = (window.__READ || []).find(x => x.code === code);
    if (rl) { const it = rl.need.find(x => x.ch === ch); if (it) extra = " · p." + it.p; }
    return `<a class="rbrow" target="_blank" rel="noopener"
      href="../mindmap/books-mindmap.html#${code}-${ch}">
      <span class="rbp" style="background:${st[0]};color:${st[1]};border-color:${st[2]}">${purpose}</span>
      <span class="rbq" style="background:${wr[1]};color:${wr[2]}">${wr[0]}</span>
      <span class="rbt"><b>《${code} ${b.short}》第 ${ch} 章${extra}</b><i>${why}</i><em class="rbw">${wr[3]}</em></span>
      <span class="rbg">打开 →</span></a>`;
  }).join("");
  return `<div class="readback"><h3>学完这关，回书补什么</h3>${rows}
    <div class="rbnote">四种回书目的：<b style="color:#1d4ed8">佐证</b> 验证课程的数字 ·
    <b style="color:#6d28d9">拓展</b> 课程没覆盖的延伸 ·
    <b style="color:#b45309">推导</b> 公式与假设的来路 ·
    <b style="color:#0e7490">查漏</b> 边界与细节。</div></div>`;
}

function chips(id){
  const refs = LB[id] || [];
  return refs.map(([code, ch]) => {
    const b = BOOKS.find(x => x.code === code);
    return `<a class="bchip" target="_blank" rel="noopener"
      href="../mindmap/books-mindmap.html#${code}-${ch}">《${code} ${b.short}》第 ${ch} 章 →</a>`;
  }).join("");
}

function showRead(){
  const total = READ.reduce((n, b) => n + b.need.length, 0);
  const doneN = Object.keys(readDone).filter(k => readDone[k]).length;
  const cards = READ.map(b => {
    const rows = b.need.map(x => {
      const key = b.code + "-" + x.ch;
      const on = !!readDone[key];
      return `<label class="rrow ${on ? "on" : ""}">
        <input type="checkbox" data-k="${key}" ${on ? "checked" : ""}>
        <span class="rt"><b>第 ${x.ch} 章 ${x.t}</b><em>${x.p}</em><i>${x.why}</i></span>
        <a class="rlink" target="_blank" rel="noopener"
           href="../mindmap/books-mindmap.html#${b.code}-${x.ch}">导图 →</a>
      </label>`;
    }).join("");
    return `<div class="bcard">
      <div class="code">${b.code} · 课程覆盖：${b.cover} <span class="cnt">必读 ${b.need.length} 章</span></div>
      <h4>${b.short} · ${b.zh}</h4>
      <div class="rlist">${rows}</div>
      <div class="rskip"><b>可以跳过：</b>${b.skip}</div>
    </div>`;
  }).join("");
  document.getElementById("main").innerHTML = `
    <div class="kicker">回书清单</div>
    <h2>课程没替代的那 ${total} 章</h2>
    <div class="min">课时用来跑通，书用来知道什么时候会失效 · 约 750 页，占全套四分之一 · 已读 ${doneN}/${total} 章</div>
    <div class="note" style="margin-top:0">三类内容必须回书：<b>推导与假设</b>（公式成立的条件）、
      <b>课程跳过的进阶章</b>、以及你<b>遇到具体问题时</b>去查的相邻做法。</div>
    <div class="bgrid rgrid">${cards}</div>`;
  document.querySelectorAll(".rrow input").forEach(cb => cb.onchange = () => {
    readDone[cb.dataset.k] = cb.checked;
    try { localStorage.setItem("reading-v1", JSON.stringify(readDone)); } catch(e) {}
    showRead();
  });
  updateList();
}

function showBooks(){
  const cards = BOOKS.map(b => `
    <div class="bcard">
      <div class="code">${b.code} · ${b.role}</div>
      <h4>${b.short} · ${b.zh}</h4>
      <div class="row"><b>前置：</b>${b.need}</div>
      <div class="row"><b>关系：</b>${b.rel}</div>
      <div class="row"><b>课程覆盖：</b>${b.cover}</div>
      <div class="row"><b>怎么读：</b>${b.tip}</div>
      <div class="row" style="margin-top:8px">
        <a target="_blank" rel="noopener" href="../mindmap/books-mindmap.html#${b.code}">打开这本书的目录 →</a>
      </div>
    </div>`).join("");
  document.getElementById("main").innerHTML = `
    <div class="kicker">总表</div>
    <h2>8 本书：谁在前、谁在后、谁可以单独看</h2>
    <div class="min">排序依据不是出版年份，也不是页数，而是「书里真的引用了谁」</div>
    <div class="bgrid">${cards}</div>
    <div class="note"><b>四条线，一处交汇：</b><br>
      · 01 / 02 是工具底座（二选一），其余六本都要用到；<br>
      · 05 → 06 是全套装唯一一处真正的“上游→下游”（06 里出现 65 次 replication）；<br>
      · 03、04 自成一条文本栈，与金融无关；<br>
      · 07 是孤岛：有 01/02 就能读，读完接不上别的书；<br>
      · 08 与所有书几乎零重叠，随时可单独开。</div>`;
}

function showIntro(){
  cur = -1;
  const t = track(), it = t.intro || {}, ls = lessons();
  document.getElementById("main").innerHTML = `
    <div class="intro">
      <div class="kicker">${t.name} · 导言</div>
      <h2>这条线是干什么的</h2>
      <div class="min">${t.sub}</div>
      <div class="lead">${it.why || ""}</div>
      <h3>学完之后，你能亲手做这三件事</h3>
      <ul class="goals">${(it.do || []).map(x => `<li>${x}</li>`).join("")}</ul>
      <div class="grid">
        <div class="cell"><b>适合谁</b>${it.who || ""}</div>
        <div class="cell"><b>需要什么</b>${it.need || ""}</div>
        <div class="cell"><b>要花多久</b>${it.time || ""}</div>
        <div class="cell"><b>这条线不包含</b>${it.not || ""}</div>
      </div>
      <div class="not">${it.first || ""}</div>
      ${(it.next && it.next.length) ? `<h3>学完之后，往哪走</h3>
        <ul class="goals">${it.next.map(x => `<li>${x}</li>`).join("")}</ul>` : ""}
      <div class="start">
        <button class="primary" id="go">开始第 1 关 →</button>
        <span class="min" style="margin:0">${ls[0].title} · ${ls[0].min} 分钟</span>
      </div>
    </div>`;
  document.getElementById("go").onclick = () => show(0);
  updateList();
}

function show(i){
  if (isBooks()) { showBooks(); updateList(); return; }
  if (isRead()) { showRead(); updateList(); return; }
  if (i === -1) { showIntro(); return; }
  const ls = lessons();
  cur = Math.max(0, Math.min(i, ls.length - 1));
  const l = ls[cur];
  const q = (l.quiz || []).map((x, k) => `<details><summary>自测 ${k+1}：${x.q}</summary>${x.a}</details>`).join("");
  const cs = (l.concepts || []).map(c => `<div class="concept"><b>${c.t}</b><em>${c.en}</em><p>${c.d}</p></div>`).join("");
  const st = (l.steps || []).map((s, k) => `<div class="step"><div class="txt"><b>${k+1}.</b> ${s.text}</div>
      <pre>${s.code.replace(/</g,"&lt;")}</pre>${s.out ? `<div class="out">▶ ${s.out}</div>` : ""}</div>`).join("");
  document.getElementById("main").innerHTML = `
    <div class="kicker">${track().name} · ${l.stage}</div>
    <h2>${l.title}</h2>
    <div class="min">预计 ${l.min} 分钟 · 需要动手 · 完成后打勾</div>
    <div class="bookchips">${chips(l.id)}</div>
    <div class="hook">${l.hook}</div>
    <h3>这一关你会学会</h3>
    <ul class="goals">${l.goals.map(g => `<li>${g}</li>`).join("")}</ul>
    <h3>三个概念，够用了</h3>${cs}
    <h3>动手做</h3>${st}
    <h3>自测（先自己想，再点开）</h3>${q}
    ${readback(l.id)}
    <div class="can"><b>做完你应该能：</b>${l.can}</div>
    <div class="nav">
      <button id="prev">← 上一关</button>
      <div class="spacer"></div>
      <button id="mark" class="${done[l.id] ? "done" : "primary"}">${done[l.id] ? "✓ 已完成" : "完成这一关"}</button>
      <button id="next">下一关 →</button>
    </div>`;
  document.getElementById("prev").onclick = () => show(cur === 0 ? -1 : cur - 1);
  document.getElementById("next").onclick = () => { if (cur < ls.length - 1) show(cur + 1); };
  document.getElementById("mark").onclick = () => {
    if (done[l.id]) delete done[l.id]; else done[l.id] = true;
    save(); show(cur);
  };
  document.getElementById("main").scrollTop = 0;
  updateList();
}
document.getElementById("resume").onclick = () => {
  if (isBooks()) return;
  const ls = lessons();
  const i = ls.findIndex(l => !done[l.id]);
  show(i < 0 ? 0 : i);
};
if (location.hash === "#books") { ti = DATA.tracks.findIndex(t => t.kind === "books"); }
if (location.hash === "#read") { ti = DATA.tracks.findIndex(t => t.kind === "readlist"); }
const _lm = location.hash.match(/^#l=([a-z0-9]+)$/);
let _jump = -1;
if (_lm) { for (let k = 0; k < DATA.tracks.length; k++) {
  const ls0 = (DATA.tracks[k].stages || []).flatMap(s => s.lessons);
  const idx = ls0.findIndex(l => l.id === _lm[1]);
  if (idx >= 0) { ti = k; _jump = idx; break; }
} }
renderTabs(); show(_jump >= 0 ? _jump : (isBooks() ? 0 : -1));
</script></body></html>"""

WB = r"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<title>学习工作簿</title>
<style>
  @page{size:A4;margin:16mm 14mm}
  body{font-family:"Microsoft YaHei","PingFang SC",serif;color:#0f172a;line-height:1.75;font-size:11.5pt;margin:0}
  .page{page-break-after:always;padding:0 0 6mm}
  .page:last-child{page-break-after:auto}
  @media screen{.page{border-bottom:2px dashed #dbe3ee;margin-bottom:14mm;padding-bottom:10mm}
    body{max-width:820px;margin:0 auto;padding:16mm 10mm}}
  h1{font-size:22pt;margin:0 0 6mm}
  .cover{padding-top:34mm}
  .cover .rule{width:40mm;height:3px;background:#2563eb;margin:8mm 0}
  .cover .sub{color:#64748b;font-size:12pt}
  h2{font-size:14pt;margin:0 0 3mm;padding-bottom:2mm;border-bottom:1px solid #e2e8f0}
  .kicker{font-size:9pt;color:#2563eb;letter-spacing:1px;margin-bottom:2mm}
  .q{background:#f8fafc;border-left:3px solid #93c5fd;padding:3mm 4mm;font-size:10.8pt;margin-bottom:4mm}
  .label{font-size:9pt;color:#94a3b8;letter-spacing:.5px;margin:5mm 0 2mm}
  .lines div{border-bottom:1px dashed #cbd5e1;height:9mm}
  .codebox{border:1px solid #dbe3ee;border-radius:2mm;padding:3mm;margin:3mm 0;background:#fcfdff}
  .codebox .cap{font-size:9pt;color:#64748b;margin-bottom:1.5mm}
  pre{font-family:Consolas,monospace;font-size:9.4pt;line-height:1.55;margin:0;white-space:pre-wrap}
  .quiz{margin:2mm 0 3mm}.quiz .qq{font-size:11pt}.quiz .ans{border-bottom:1px dashed #cbd5e1;height:9mm}
  .toc td{padding:1.2mm 0;font-size:10.5pt}.toc td.n{color:#94a3b8;width:16mm}
  .trackhead{font-size:16pt;margin:0 0 6mm;padding:6mm 0;border-bottom:2px solid #0f172a}
  .anspage h3{font-size:11pt;margin:4mm 0 1mm;color:#047857}
  .anspage p{margin:0 0 2mm;font-size:10.5pt}
</style></head><body>
<div class="page cover">
  <h1>学习工作簿</h1>
  <div class="rule"></div>
  <div class="sub">__NTRACKS__ 条路线 · 共 __NTOTAL__ 关 · 每关 20–30 分钟</div>
  <p style="margin-top:8mm;color:#475569">每关一页：先写「我的问题」→ 跑代码 → 写「我的结果」→ 合上材料做自测。<br>
  答案在最后。</p>
  <div class="label">目录</div>
  <table class="toc">__TOC__</table>
</div>
__PAGES__
__ANSWERS__
</body></html>"""


def esc(t):
    return html.escape(str(t))


def build():
    toc, pages, answers = [], [], []
    for t in TRACKS:
        it = t.get("intro") or {}
        dots = "".join("<li>%s</li>" % esc(x) for x in it.get("do", []))
        pages.append(
            '<div class="page"><div class="trackhead">%s</div>'
            '<div style="color:#64748b;margin-bottom:6mm">%s</div>'
            '<div class="q">%s</div>'
            '<div class="label">学完能做的三件事</div><ul>%s</ul>'
            '<div class="label">适合谁 / 需要什么 / 多久</div>'
            '<p>%s<br>%s<br>%s</p>'
            '<div class="label">不包含</div><p>%s</p>'
            '<div style="margin-top:6mm;color:#2563eb">%s</div></div>'
            % (esc(t["name"]), esc(t["sub"]), esc(it.get("why", "")), dots,
               esc(it.get("who", "")), esc(it.get("need", "")), esc(it.get("time", "")),
               esc(it.get("not", "")), esc(it.get("first", ""))))
        idx = 0
        for s in t["stages"]:
            for l in s["lessons"]:
                idx += 1
                toc.append('<tr><td class="n">%s-%d</td><td>%s · %d 分钟</td></tr>'
                           % (esc(t["name"][:2]), idx, esc(l["title"]), l["min"]))
                steps = "".join(
                    '<div class="codebox"><div class="cap">练习 %d：%s</div><pre>%s</pre></div>'
                    % (k + 1, esc(st["text"]), esc(st["code"])) for k, st in enumerate(l["steps"]))
                quiz = "".join('<div class="quiz"><div class="qq">%d. %s</div><div class="ans"></div></div>'
                               % (k + 1, esc(q["q"])) for k, q in enumerate(l["quiz"]))
                rb = READBACK.get(l["id"])
                rbline = ("<div class=\"label\">回书指引</div><p>目的：%s —— %s</p>"
                          "<div class=\"lines\"><div></div><div></div></div>" % (esc(rb[0]), esc(rb[1]))) if rb else ""
                pages.append(f"""
<div class="page">
  <div class="kicker">{esc(t['name'])} · {esc(s['name'])} · 第 {idx} 关</div>
  <h2>{esc(l['title'])}</h2>
  <div class="q">{esc(l['hook'])}</div>
  <div class="label">我的问题（学之前先写一句）</div>
  <div class="lines"><div></div><div></div></div>
  <div class="label">我学到的方法 / 结论</div>
  <div class="lines"><div></div><div></div><div></div></div>
  {steps}
  <div class="label">我的结果（跑出来的数字，和预期差多少）</div>
  <div class="lines"><div></div></div>
  <div class="label">自测</div>
  {quiz}
  {rbline}
</div>""")
                answers.append("<h3>%s · 第 %d 关 · %s</h3>" % (esc(t["name"]), idx, esc(l["title"])) +
                               "".join("<p>%d. %s</p>" % (k + 1, esc(q["a"])) for k, q in enumerate(l["quiz"])))
    ans = '<div class="page anspage"><h2>答案</h2>' + "".join(answers) + "</div>"
    return "".join(toc), "".join(pages), ans


def main():
    books_track = {"id": "books", "name": "8 本书总表", "sub": "哪本在前、哪两本二选一", "kind": "books", "stages": []}
    read_track = {"id": "read", "name": "回书清单", "sub": "课程没覆盖的部分，去书里补", "kind": "readlist", "stages": []}
    data = {"tracks": TRACKS + [books_track, read_track]}
    html_out = (HTML.replace("__DATA__", json.dumps(data, ensure_ascii=False))
                    .replace("__BOOKS__", json.dumps(BOOKS, ensure_ascii=False))
                    .replace("__LB__", json.dumps({k: v for k, v in LESSON_BOOKS.items()}, ensure_ascii=False))
                    .replace("__READ__", json.dumps(READLIST, ensure_ascii=False))
                    .replace("__RB__", json.dumps(READBACK, ensure_ascii=False)))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(html_out)

    toc, pages, answers = build()
    total = sum(len(s["lessons"]) for t in TRACKS for s in t["stages"])
    wb = (WB.replace("__TOC__", toc).replace("__PAGES__", pages).replace("__ANSWERS__", answers)
            .replace("__NTRACKS__", str(len(TRACKS))).replace("__NTOTAL__", str(total)))
    open(os.path.join(HERE, "workbook.html"), "w", encoding="utf-8").write(wb)
    print("tracks:", [t["name"] for t in TRACKS], "lessons:", total)


if __name__ == "__main__":
    main()
