# -*- coding: utf-8 -*-
"""Build the bilingual mind map (interactive HTML + Mermaid markdown).

Data:
  sections.json            chapter -> sections (English, pdf page)
  i18n/zh/bXX.json         Chinese translations (optional but expected)
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SEC = json.load(open(os.path.join(HERE, "sections.json"), encoding="utf-8"))

POINTS = {}
_pts_dir = os.path.join(HERE, "i18n", "points")
if os.path.isdir(_pts_dir):
    for fn in sorted(os.listdir(_pts_dir)):
        if not fn.endswith(".json"):
            continue
        try:
            d = json.load(open(os.path.join(_pts_dir, fn), encoding="utf-8"))
        except Exception:
            continue
        POINTS.setdefault(fn[1:3], {}).update(d)

ZH = {}
for i in range(1, 9):
    p = os.path.join(HERE, "i18n", "zh", "b%02d.json" % i)
    if os.path.exists(p):
        ZH["%02d" % i] = json.load(open(p, encoding="utf-8"))

TRACKS = [
    ("数据与 ML 底座", "Data & ML Foundations", "#2563eb", ["01", "02"]),
    ("金融理论", "Financial Theory", "#059669", ["05"]),
    ("策略与强化学习", "Strategy & RL", "#d97706", ["07", "06"]),
    ("文本与推理工程", "Text & Inference", "#7c3aed", ["03", "04"]),
    ("工程技能", "Engineering Craft", "#475569", ["08"]),
]

BOOKS = [
    ("01", "Python Data Science Handbook", "PDSH", 548, "VanderPlas", [
        ("IPython: Beyond Normal Python", 19, "查文档、魔法命令、计时与剖析", "快读"),
        ("Introduction to NumPy", 51, "ndarray、广播、索引、ufunc", "精读"),
        ("Data Manipulation with Pandas", 115, "Series/DataFrame、groupby、时间序列", "精读"),
        ("Visualization with Matplotlib", 235, "两套接口、子图、色条、Seaborn", "选读"),
        ("Machine Learning", 349, "估计器 API、验证、回归/森林/PCA/聚类", "精读"),
    ]),
    ("02", "Machine Learning with Python Cookbook (2e)", "MLCK", 404, "Gallatin & Albon", [
        ("Working with NumPy", 9, "向量矩阵、稀疏矩阵、点积求逆、随机数", "快读"),
        ("Loading Data", 27, "CSV/Excel/JSON/Parquet、SQL、S3", "选读"),
        ("Data Wrangling", 42, "筛选、缺失值、去重、分组聚合", "精读"),
        ("Handling Numerical Data", 77, "缩放、多项式特征、异常值、离散化", "精读"),
        ("Handling Categorical Data", 96, "名义/有序编码、类别不平衡", "精读"),
        ("Handling Text", 108, "分词、TF-IDF、情感分类", "选读"),
        ("Handling Dates and Times", 125, "时区、滞后特征、滚动窗口", "选读"),
        ("Handling Images", 138, "缩放裁剪、颜色直方图、预训练 embedding", "选读"),
        ("Dimensionality Reduction Using Feature Extraction", 168, "PCA、核 PCA、LDA、NMF、SVD", "选读"),
        ("Dimensionality Reduction Using Feature Selection", 180, "方差阈值、相关性、卡方、RFE", "选读"),
        ("Model Evaluation", 190, "交叉验证、指标、ROC、学习曲线", "精读"),
        ("Model Selection", 217, "网格/随机搜索、Pipeline 调参", "精读"),
        ("Linear Regression", 230, "交互效应、非线性、Ridge/Lasso", "精读"),
        ("Trees and Forests", 240, "决策树、随机森林、boosting、XGBoost", "精读"),
        ("K-Nearest Neighbors", 259, "KNN 分类、选 k、faiss", "快读"),
        ("Logistic Regression", 270, "二分类/多分类、SGD、不平衡", "精读"),
        ("Support Vector Machines", 276, "核技巧、预测概率、不平衡", "选读"),
        ("Naive Bayes", 286, "三种朴素贝叶斯、概率校准", "快读"),
        ("Clustering", 293, "K-Means、Mean Shift、DBSCAN、层次", "快读"),
        ("Tensors with PyTorch", 301, "张量创建、稀疏张量、索引", "选读"),
        ("Neural Networks", 312, "autograd、训练、早停、Dropout", "精读"),
        ("Neural Networks for Unstructured Data", 344, "图像/文本分类、微调预训练模型", "选读"),
        ("Saving, Loading, and Serving Trained Models", 354, "joblib、Flask、TF Serving、Seldon", "选读"),
    ]),
    ("03", "Blueprints for Text Analytics Using Python", "NLP", 422, "Albrecht 等", [
        ("Gaining Early Insights from Textual Data", 23, "EDA、分词、TF-IDF、词云、n-gram", "精读"),
        ("Extracting Textual Insights with APIs", 55, "GitHub API、Tweepy", "选读"),
        ("Scraping Websites and Extracting Data", 79, "robots.txt、RSS、Scrapy", "选读"),
        ("Preparing Textual Data", 111, "正则清洗、spaCy 词形与 NER", "精读"),
        ("Feature Engineering and Syntactic Similarity", 143, "手写 vectorizer、TF-IDF、余弦相似", "精读"),
        ("Text Classification Algorithms", 173, "四步分类流程、交叉验证、调参", "精读"),
        ("How to Explain a Text Classifier", 205, "预测概率、SVM 权重、LIME、Anchor", "精读"),
        ("Topic Modeling and Clustering", 229, "NMF/LSA/LDA、coherence、HDP", "精读"),
        ("Text Summarization", 265, "TF-IDF、TextRank、抽取式摘要", "选读"),
        ("Word Embeddings", 289, "词向量、Gensim 训练、降维可视化", "精读"),
        ("Sentiment Analysis", 317, "词典法、监督学习、BERT 微调", "精读"),
        ("Building a Knowledge Graph", 345, "NER、共指、实体链接、关系抽取", "选读"),
        ("Using Text Analytics in Production", 381, "Docker、FastAPI、云部署、CI", "选读"),
    ]),
    ("04", "Hands-On LLM Serving and Optimization", "LLM", 372, "Wang & Hu · 2026", [
        ("Introduction to Model Serving", 19, "模型生命周期、三种部署形态、vLLM 初体验", "精读"),
        ("Large Language Model Serving", 49, "自回归、KV cache、prefill/decode、流式", "精读"),
        ("Model Serving System Design", 83, "从零写服务、批处理、Triton", "选读"),
        ("Model Serving Best Practices", 125, "Agent/RAG/CAG、分层架构、云方案", "选读"),
        ("Challenges When Serving LLMs", 175, "显存估算、两阶段瓶颈", "精读"),
        ("Essential Optimization Techniques", 207, "连续批处理、FlashAttention、量化、PagedAttention", "精读"),
        ("Advanced Optimization Techniques", 251, "投机解码、张量/流水线/专家并行、PD 分离", "精读"),
        ("LLM Serving Frameworks", 289, "vLLM 调度器、TensorRT-LLM、SGLang、llama.cpp", "精读"),
        ("LLM Optimization in Practice", 311, "Qwen3-14B 八步优化实战", "精读"),
        ("Advancements in LLM Serving", 333, "语义缓存、多模态、边缘、Multi-LoRA", "快读"),
    ]),
    ("05", "Financial Theory with Python", "FTP", 204, "Hilpisch", [
        ("Finance and Python", 17, "环境与 Jupyter 起步", "快读"),
        ("Two-State Economy", 33, "复制→无套利→鞅测度→FTAP→均值方差", "精读"),
        ("Three-State Economy", 75, "不完备市场、超复制、CAPM", "精读"),
        ("Optimality and Equilibrium", 99, "期望效用最大、均衡定价", "选读"),
        ("Static Economy", 133, "一般静态经济、BSM、Merton 跳扩散", "精读"),
        ("Dynamic Economy", 163, "CRR 二叉树、GBM 模拟、LSM 美式", "精读"),
        ("Where to Go from Here?", 185, "延伸书单", "跳过"),
    ]),
    ("06", "Reinforcement Learning for Finance", "RLF", 215, "Hilpisch", [
        ("Learning Through Interaction", 17, "贝叶斯更新、RL 九大构件", "选读"),
        ("Deep Q-Learning", 33, "FHMDP、Bellman、DQN 打通 CartPole", "精读"),
        ("Financial Q-Learning", 51, "滞后特征预测游戏", "精读"),
        ("Simulated Data", 65, "白噪声、GBM/Vasicek 蒙特卡洛", "选读"),
        ("Generated Data", 81, "GAN 造时间序列、KS 检验", "选读"),
        ("Algorithmic Trading", 99, "交易环境、多空两动作", "精读"),
        ("Dynamic Hedging", 119, "把 BSM delta 对冲改成 RL", "精读"),
        ("Dynamic Asset Allocation", 143, "多资产配置、Sharpe 奖励", "精读"),
        ("Optimal Execution", 181, "Almgren-Chriss、actor-critic", "精读"),
        ("Concluding Remarks", 203, "总结与改进方向", "快读"),
    ]),
    ("07", "Deep Learning for Finance", "DLF", 362, "Kaabar", [
        ("Introducing Data Science and Trading", 17, "流程、资产类别、应用场景", "快读"),
        ("Essential Probabilistic Methods", 35, "概率、抽样检验、熵", "选读"),
        ("Descriptive Statistics and Data Analysis", 51, "分布、相关、平稳性、回归", "精读"),
        ("Linear Algebra and Calculus", 97, "矩阵、导数、优化", "选读"),
        ("Introducing Technical Analysis", 151, "形态、均线、RSI", "选读"),
        ("Introductory Python for Data Science", 167, "语法、pandas、MT5 取数", "快读"),
        ("ML Models for Time Series Prediction", 193, "滞后特征 + 八种回归器", "精读"),
        ("Deep Learning for Time Series I", 231, "反向传播、MLP/RNN/LSTM/TCN", "精读"),
        ("Deep Learning for Time Series II", 265, "分数阶差分、时序 CV、多期预测", "精读"),
        ("Deep RL for Time Series", 293, "Q 表、Bellman、DQN", "选读"),
        ("Advanced Techniques and Strategies", 307, "COT、波动率、训练可视化", "选读"),
        ("Market Drivers and Risk Management", 341, "宏观、新闻、风控与行为偏差", "快读"),
    ]),
    ("08", "Learning Modern C++ for Finance", "C++", 431, "Hanson", [
        ("An Overview of C++", 23, "语言与标准库、auto/lambda/enum class", "精读"),
        ("User-Defined Classes with Modern C++", 55, "BS 类、functor 求隐含波动率、移动语义", "精读"),
        ("Inheritance, Polymorphism, Smart Pointers", 85, "Payoff 继承体系、clone、unique/shared_ptr", "精读"),
        ("STL I: Containers and Iterators", 125, "函数模板、vector/map、迭代器", "选读"),
        ("STL II: Algorithms and Ranges", 165, "算法、ranges、数值算法、view", "选读"),
        ("Random Numbers and Concurrency", 199, "分布、蒙特卡洛障碍期权、并行/async", "精读"),
        ("Dates and Fixed Income", 247, "chrono、计息基准、收益率曲线、债券定价", "选读"),
        ("Linear Algebra", 299, "表达式模板、Eigen、mdspan、BLAS", "精读"),
        ("The Boost Libraries", 345, "数学分布、MultiArray 二叉树、累加器", "选读"),
        ("Modules and Concepts", 379, "module/import、concepts 约束", "快读"),
        ("Appendix A–E", 399, "虚析构、对象切片、移动语义实现、valarray", "参考"),
    ]),
]

TAG_COLOR = {"精读": "#ef4444", "选读": "#0ea5e9", "快读": "#94a3b8", "跳过": "#cbd5e1", "参考": "#a855f7"}


def build_data():
    zhbook = {k: v.get("book_title_zh", "") for k, v in ZH.items()}
    tree = {"id": "root", "title": "8 本书", "zh": "量化 · 机器学习 · LLM",
            "sub": "2960 页 · 5 个分支 · 1229 节", "kind": "root", "children": []}
    for tname, ten, tcolor, ids in TRACKS:
        t = {"id": "t-" + tname, "title": tname, "zh": ten, "kind": "track",
             "color": tcolor, "children": []}
        for bid, title, short, pages, meta, chs in BOOKS:
            if bid not in ids:
                continue
            z = ZH.get(bid, {})
            b = {"id": "b-" + bid, "title": "%s %s" % (bid, short),
                 "zh": zhbook.get(bid, ""), "sub": "%s · %d 页 · %d 章" % (meta, pages, len(chs)),
                 "kind": "book", "color": tcolor, "children": []}
            zchs = z.get("chapters_zh") or []
            zsecs = z.get("sections_zh") or []
            secs = SEC.get(bid, [])
            for i, (ctitle, page, gist, tag) in enumerate(chs, 1):
                kids = []
                rows = secs[i - 1] if i - 1 < len(secs) else []
                zrow = zsecs[i - 1] if i - 1 < len(zsecs) else []
                for j, (st, sp) in enumerate(rows, 1):
                    pts = POINTS.get(bid, {}).get("%d.%d" % (i, j)) or []
                    pkids = [{"id": "p-%s-%d-%d-%d" % (bid, i, j, k), "title": pt,
                              "zh": "", "kind": "point", "color": tcolor}
                             for k, pt in enumerate(pts, 1) if str(pt).strip()]
                    kids.append({"id": "s-%s-%d-%d" % (bid, i, j), "title": st,
                                 "zh": zrow[j - 1] if j - 1 < len(zrow) else "",
                                 "page": sp, "kind": "section", "color": tcolor,
                                 "children": pkids})
                b["children"].append({
                    "id": "c-%s-%d" % (bid, i),
                    "title": ("第 %d 章 · " % i if bid != "08" or i <= 10 else "") + ctitle,
                    "zh": zchs[i - 1] if i - 1 < len(zchs) else "",
                    "sub": gist, "page": page, "tag": tag, "kind": "chapter",
                    "color": tcolor, "children": kids,
                })
            t["children"].append(b)
        tree["children"].append(t)
    return tree


HTML = r"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<title>8 本书 · 中英对照思维导图</title>
<style>
  :root{--bg:#f7f9fc;--ink:#0f172a;--muted:#64748b;--line:#dbe4ee;}
  *{box-sizing:border-box}
  html,body{margin:0;height:100%;overflow:hidden;color:var(--ink);
    font-family:"Segoe UI","Microsoft YaHei","PingFang SC",system-ui,sans-serif;
    background:var(--bg) radial-gradient(circle at 1px 1px,#dce6f1 1px,transparent 0) 0 0/24px 24px;}
  #bar{position:fixed;top:0;left:0;right:0;height:60px;display:flex;align-items:center;gap:10px;
    padding:0 20px;background:#ffffffeb;border-bottom:1px solid var(--line);z-index:9;
    backdrop-filter:blur(10px);box-shadow:0 1px 12px #0f172a0a}
  #bar h1{font-size:16px;margin:0 6px 0 0;font-weight:700;letter-spacing:.4px;white-space:nowrap}
  #bar h1 small{font-weight:500;color:var(--muted);font-size:12px;margin-left:8px;letter-spacing:0}
  .hint{font-size:11.5px;color:var(--muted);margin-right:auto;white-space:nowrap;overflow:hidden;
    text-overflow:ellipsis;max-width:380px}
  button{font:inherit;font-size:12.5px;padding:7px 13px;border:1px solid #d3dde9;background:#fff;
    border-radius:9px;cursor:pointer;color:#334155;white-space:nowrap;transition:.15s}
  button:hover{background:#f1f5fb;border-color:#a9bcd2;transform:translateY(-1px)}
  input{font:inherit;font-size:12.5px;padding:7px 12px;border:1px solid #d3dde9;border-radius:9px;
    width:168px;outline:none}
  input:focus{border-color:#2563eb;box-shadow:0 0 0 3px #2563eb18}
  svg{width:100%;height:100%;display:block;cursor:grab}
  svg.drag{cursor:grabbing}
  .node rect.body{stroke-width:1.4;transition:stroke-width .15s,filter .15s}
  .node:hover rect.body{stroke-width:2.2}
  .node text{pointer-events:none}
  .edge{fill:none;stroke-linecap:round}
  .hit rect.body{stroke:#f59e0b!important;stroke-width:3!important}
  #filters{display:flex;gap:6px}
  #filters button{padding:6px 10px;font-size:12px;border-radius:8px}
  #filters button.on{background:#0f172a;color:#fff;border-color:#0f172a}
</style></head><body>
<div id="bar">
  <h1>8 本书 · 中英对照<small>__STAT__</small></h1>
  <button id="expand">全部展开</button>
  <button id="collapse">只看书名</button>
  <button id="fit">适配窗口</button>
  <span class="hint">滚轮缩放 · 拖动平移 · 点书看章 · 点章看小节</span>
  <span id="filters"></span>
  <input id="q" placeholder="搜索章节 / 小节（中英均可）">
</div>
<svg id="map"><g id="scene"></g></svg>
<script>
const DATA = __DATA__;
const NS="http://www.w3.org/2000/svg";
const svg=document.getElementById("map"), scene=document.getElementById("scene");
const collapsed=new Set(); let only=null;
function collapseAll(){
  collapsed.clear();
  DATA.children.forEach(t=>t.children.forEach(b=>{
    collapsed.add(b.id);
    (b.children||[]).forEach(c=>{ collapsed.add(c.id); (c.children||[]).forEach(x=>collapsed.add(x.id)); });
  }));
}
const W={root:250,track:210,book:360,chapter:470,section:400,point:330};
const PAD=20, GAP_X=150, GAP_Y=30;
const meas=document.createElement("canvas").getContext("2d");
const F_T="700 15px 'Microsoft YaHei',sans-serif";
const F_T2="700 14px 'Microsoft YaHei',sans-serif";
const F_Z="13px 'Microsoft YaHei',sans-serif";
const F_S="12px 'Microsoft YaHei',sans-serif";
const F_P="12.5px 'Microsoft YaHei',sans-serif";

function wrap(text,maxW,font){
  meas.font=font;
  const tokens=String(text).match(/[A-Za-z0-9][A-Za-z0-9\/\-\+\.%:'&]*|\s+|./gu)||[];
  const out=[]; let line="";
  for(const tk of tokens){
    if(meas.measureText(line+tk).width<=maxW || !line){ if(tk===" "&&!line) continue; line+=tk; continue; }
    out.push(line.trimEnd());
    if(meas.measureText(tk).width>maxW){
      let buf="";
      for(const ch of tk){ if(meas.measureText(buf+ch).width>maxW&&buf){out.push(buf);buf=ch;} else buf+=ch; }
      line=buf;
    } else line = tk===" " ? "" : tk;
  }
  if(line.trim()) out.push(line.trimEnd());
  return out.length?out:[""];
}

function layout(node,depth){
  node.depth=depth; node.w=W[node.kind];
  const isPt=node.kind==="point";
  const isSec=node.kind==="section";
  const ft=isPt?F_P:(isSec?F_T2:(node.kind==="root"||node.kind==="track"?F_T:F_T2));
  node.tl=wrap(node.title,node.w-PAD*2-(isPt?10:(isSec?54:16)),ft);
  node.zl=(node.zh&&!isPt)?wrap(node.zh,node.w-PAD*2-16,F_Z):[];
  node.sl=(node.sub&&!isSec&&!isPt)?wrap(node.sub,node.w-PAD*2-30,F_S):[];
  node.lh=isPt?18:(isSec?20:22); node.zh=node.zh||"";
  if(isPt){ node.h=14+node.tl.length*node.lh+12; }
  else{
    node.h=PAD+node.tl.length*node.lh+(node.zl.length?node.zl.length*19+2:0)
          +(node.sl.length?node.sl.length*17+4:0)+PAD+(isSec?0:10);
    node.h=Math.max(node.h,isSec?54:56);
  }
  const kids=collapsed.has(node.id)?[]:(node.children||[]).filter(k=>{
    if(node.kind!=="root"||!only) return true; return k.title===only; });
  node.visibleKids=kids;
  kids.forEach(k=>layout(k,depth+1));
}

function subtree(n,fn){fn(n);(n.visibleKids||[]).forEach(k=>subtree(k,fn));}
function computeBounds(){
  let x0=1e9,y0=1e9,x1=-1e9,y1=-1e9;
  subtree(DATA,n=>{x0=Math.min(x0,n.x);y0=Math.min(y0,n.y);x1=Math.max(x1,n.x+n.w);y1=Math.max(y1,n.y+n.h);});
  return {x0,y0,x1,y1,w:x1-x0,h:y1-y0};
}

function render(){
  layout(DATA,0);
  let cursor=0;
  (function walk(n){
    const kids=n.visibleKids||[];
    if(!kids.length){ n.y=cursor; cursor+=n.h; return; }
    kids.forEach((k,i)=>{ walk(k); if(i<kids.length-1) cursor+=GAP_Y; });
    n.y=(kids[0].y+kids[kids.length-1].y)/2;
  })(DATA);
  const widths={};
  (function collect(n){widths[n.depth]=Math.max(widths[n.depth]||0,n.w);(n.visibleKids||[]).forEach(collect);})(DATA);
  const xBy=[0];
  for(let d=1;d<8;d++){ if(widths[d]===undefined) break; xBy[d]=xBy[d-1]+(widths[d-1]||0)+GAP_X; }
  (function place(n){ n.x=xBy[n.depth]; (n.visibleKids||[]).forEach(place); })(DATA);

  scene.innerHTML="";
  const defs=document.createElementNS(NS,"defs");
  defs.innerHTML='<filter id="sh" x="-20%" y="-20%" width="150%" height="160%">'+
    '<feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#0f172a" flood-opacity="0.10"/></filter>';
  scene.appendChild(defs);
  const gE=document.createElementNS(NS,"g"), gN=document.createElementNS(NS,"g");
  scene.append(gE,gN);

  subtree(DATA,n=>{
    (n.visibleKids||[]).forEach(k=>{
      const x1=n.x+n.w, y1=n.y+n.h/2, x2=k.x, y2=k.y+k.h/2, mx=(x1+x2)/2;
      const p=document.createElementNS(NS,"path");
      p.setAttribute("d",`M${x1},${y1} C${mx},${y1} ${mx},${y2} ${x2},${y2}`);
      p.setAttribute("class","edge");
      const isLeaf=(k.kind==="section"||k.kind==="point");
      p.setAttribute("stroke",k.kind==="point"?"#e4edf6":(isLeaf?"#cfdae7":(k.color||"#cbd5e1")));
      p.setAttribute("stroke-width",k.kind==="point"?1:(isLeaf?1.3:(k.kind==="book"?2.6:2)));
      p.setAttribute("opacity",isLeaf?.85:.75);
      gE.appendChild(p);
    });
  });

  subtree(DATA,n=>{
    const g=document.createElementNS(NS,"g");
    g.setAttribute("class","node"); g.dataset.id=n.id;
    const r=document.createElementNS(NS,"rect");
    r.setAttribute("class","body");
    r.setAttribute("x",n.x); r.setAttribute("y",n.y); r.setAttribute("width",n.w); r.setAttribute("height",n.h);
    r.setAttribute("rx", n.kind==="section"?10:(n.kind==="chapter"?14:16));
    let fill="#fff", stroke="#dbe4ee", sh=false;
    if(n.kind==="root"){ fill="#0f172a"; stroke="#0f172a"; sh=true; }
    else if(n.kind==="track"){ fill=n.color; stroke=n.color; sh=true; }
    else if(n.kind==="book"){ fill="#fff"; stroke=n.color; sh=true; }
    else if(n.kind==="chapter"){ fill="#fff"; stroke="#e3ebf4"; sh=true; }
    else if(n.kind==="section"){ fill="#fcfdff"; stroke="#e6eef7"; sh=true; }
    else { fill="#ffffff"; stroke="#f1f5fa"; }
    r.setAttribute("fill",fill); r.setAttribute("stroke",stroke);
    if(sh) r.setAttribute("filter","url(#sh)");
    g.appendChild(r);

    // 左侧色条（书 / 章）
    if(n.kind==="book"||n.kind==="chapter"){
      const bar=document.createElementNS(NS,"rect");
      bar.setAttribute("x",n.x+1.5); bar.setAttribute("y",n.y+8);
      bar.setAttribute("width",4.5); bar.setAttribute("height",n.h-16);
      bar.setAttribute("rx",3); bar.setAttribute("fill",n.color);
      bar.setAttribute("opacity",n.kind==="book"?1:.55);
      g.appendChild(bar);
    }

    const tx=n.x+PAD, ty=n.y+PAD+10;
    const col=n.kind==="root"||n.kind==="track"?"#fff":"#0f172a";
    n.tl.forEach((ln,i)=>{
      const t=document.createElementNS(NS,"text");
      t.setAttribute("x",tx); t.setAttribute("y",ty+i*n.lh); t.setAttribute("fill",col);
      t.setAttribute("style",n.kind==="point"?F_P:F_T2);
      if(n.kind==="point") t.setAttribute("fill","#3f5063");
      t.textContent=ln; g.appendChild(t);
    });
    let y=ty+n.tl.length*n.lh;
    const zc=n.kind==="root"?"#cbd5e1":(n.kind==="track"?"#ffffffcc":(n.color||"#334155"));
    n.zl.forEach((ln,i)=>{
      const t=document.createElementNS(NS,"text");
      t.setAttribute("x",tx); t.setAttribute("y",y+12+i*19); t.setAttribute("fill",zc);
      t.setAttribute("style",F_Z); t.setAttribute("opacity",n.kind==="section"?"0.9":"0.95");
      t.textContent=ln; g.appendChild(t);
    });
    if(n.zl.length) y+=2+n.zl.length*19;
    const sc=n.kind==="track"?"#e0f2fe":"#7c8ba1";
    n.sl.forEach((ln,i)=>{
      const t=document.createElementNS(NS,"text");
      t.setAttribute("x",tx); t.setAttribute("y",y+14+i*17); t.setAttribute("fill",sc);
      t.setAttribute("style",F_S); t.textContent=ln; g.appendChild(t);
    });

    if((n.page||n.tag)&&n.kind!=="point"){
      let meta=(n.page?"p."+n.page:"")+(n.page&&n.tag?" · ":"")+(n.tag||"");
      if(n.kind==="chapter"&&n.children&&n.children.length) meta+=" · "+n.children.length+" 节";
      if(n.kind==="section"&&n.children&&n.children.length) meta+=" · "+n.children.length+" 点";
      const b=document.createElementNS(NS,"text");
      b.setAttribute("x",n.x+n.w-12); b.setAttribute("y",n.y+n.h-11);
      b.setAttribute("text-anchor","end");
      b.setAttribute("style","600 10.5px 'Microsoft YaHei',sans-serif");
      b.setAttribute("fill",TAGCOL[n.tag]||"#93a3b8"); b.textContent=meta; g.appendChild(b);
    }
    // 折叠指示
    if((n.children||[]).length){
      const open=!collapsed.has(n.id);
      const t=document.createElementNS(NS,"text");
      t.setAttribute("x",n.x+n.w-12); t.setAttribute("y",n.y+18);
      t.setAttribute("text-anchor","end");
      t.setAttribute("style","600 11px 'Microsoft YaHei',sans-serif");
      t.setAttribute("fill",n.kind==="track"?"#ffffff99":"#9aa9bd");
      t.textContent=open?"−":"+"; g.appendChild(t);
    }
    g.addEventListener("click",e=>{
      e.stopPropagation();
      if(!n.children||!n.children.length) return;
      const wasOpen=collapsed.has(n.id);
      if(n.kind==="book"){
        collapseAll();
        if(wasOpen) collapsed.delete(n.id);
      }else if(n.kind==="chapter"){
        (findNode(DATA,"b-"+n.id.split("-")[1])||{children:[]}).children.forEach(c=>collapsed.add(c.id));
        if(wasOpen) collapsed.delete(n.id);
      }else if(wasOpen) collapsed.delete(n.id);
      else collapsed.add(n.id);
      render(); focusNode(n.id);
    });
    gN.appendChild(g);
  });
  window.__bounds=computeBounds();
}
const TAGCOL=__TAGS__;

function findNode(n,id){ if(n.id===id) return n; for(const k of (n.children||[])){const r=findNode(k,id); if(r) return r;} return null; }

let scale=1,tx=20,ty=20,dragging=false,lx=0,ly=0;
function apply(){ scene.setAttribute("transform",`translate(${tx},${ty}) scale(${scale})`); }
function fit(){
  const b=window.__bounds||computeBounds();
  const vw=innerWidth-70, vh=innerHeight-120;
  const sW=vw/b.w, sH=vh/b.h;
  scale=Math.min(sW,sH,1.15);
  if(scale<0.12) scale=0.12;
  tx=(innerWidth-b.w*scale)/2-b.x0*scale;
  ty=Math.max(72,(innerHeight-b.h*scale)/2);
  apply();
}
function focusNode(id){
  const n=findNode(DATA,id); if(!n) return fit();
  let y0=1e9,y1=-1e9;
  (function w(m){y0=Math.min(y0,m.y);y1=Math.max(y1,m.y+m.h);(m.visibleKids||[]).forEach(w);})(n);
  const b=computeBounds();
  const vh=innerHeight-140, vw=innerWidth-140, hh=Math.max(1,y1-y0);
  let s=Math.min(1.0, vh/hh*0.92);           // 让子树高度大致占满
  s=Math.min(s, vw/Math.max(1,b.w)*1.6);
  s=Math.max(0.45, Math.min(s, 1.05));
  scale=s;
  tx=innerWidth*0.22-(n.x+n.w/2)*scale;      // 节点略偏左
  ty=innerHeight*0.46-(n.y+n.h/2)*scale;     // 节点近似居中
  apply();
}
svg.addEventListener("wheel",e=>{
  e.preventDefault();
  const f=e.deltaY<0?1.12:1/1.12, r=svg.getBoundingClientRect();
  const mx=e.clientX-r.left, my=e.clientY-r.top;
  tx=mx-(mx-tx)*f; ty=my-(my-ty)*f; scale*=f; apply();
},{passive:false});
svg.addEventListener("mousedown",e=>{dragging=true;lx=e.clientX;ly=e.clientY;svg.classList.add("drag");});
addEventListener("mousemove",e=>{if(!dragging)return;tx+=e.clientX-lx;ty+=e.clientY-ly;lx=e.clientX;ly=e.clientY;apply();});
addEventListener("mouseup",()=>{dragging=false;svg.classList.remove("drag");});
document.getElementById("fit").onclick=fit;
document.getElementById("expand").onclick=()=>{collapsed.clear();render();fit();};
document.getElementById("collapse").onclick=()=>{
  collapsed.clear();
  collapseAll();
  render();fit();
};
document.getElementById("q").addEventListener("keydown",e=>{
  if(e.key!=="Enter")return;
  const q=e.target.value.trim(); if(!q)return;
  collapsed.clear(); render();
  document.querySelectorAll(".node").forEach(g=>g.classList.remove("hit"));
  const hits=[...document.querySelectorAll(".node")].filter(g=>g.textContent.includes(q));
  hits.forEach(g=>g.classList.add("hit"));
  if(hits.length){
    const g=hits[0], r=g.getBoundingClientRect(), b=svg.getBoundingClientRect();
    tx-=(r.left-b.left-r.width/2); ty-=(r.top-b.top-r.height/2); apply();
  }
});
const fbar=document.getElementById("filters");
fbar.innerHTML=["全部"].concat(DATA.children.map(t=>t.title))
  .map((t,i)=>`<button data-t="${t}" class="${i===0?"on":""}">${t}</button>`).join("");
fbar.querySelectorAll("button").forEach(btn=>btn.onclick=()=>{
  fbar.querySelectorAll("button").forEach(x=>x.classList.remove("on"));
  btn.classList.add("on");
  only=btn.dataset.t==="全部"?null:btn.dataset.t;
  collapsed.clear();
  collapseAll();
  render(); fit();
});
collapseAll();
const _open=new URLSearchParams(location.search).get("open")||(location.hash?location.hash.slice(1):"");
if(_open){
  const [_bk,_ch,_sc]=_open.split("-");
  collapsed.delete("b-"+_bk);
  if(_ch) collapsed.delete("c-"+_bk+"-"+_ch);
  if(_sc) collapsed.delete("s-"+_bk+"-"+_ch+"-"+_sc);
  render();
  focusNode(_sc?("s-"+_bk+"-"+_ch+"-"+_sc):(_ch?("c-"+_bk+"-"+_ch):("b-"+_bk)));
}else{ render(); fit(); }
addEventListener("load",()=>setTimeout(()=>{ if(!_open) fit(); },120));
</script></body></html>"""


def mermaid_safe(s):
    s = str(s)
    for a, b in (("(", "（"), (")", "）"), ("[", "【"), ("]", "】"),
                 ("{", "｛"), ("}", "｝"), ('"', "”"), ("#", "＃")):
        s = s.replace(a, b)
    return s


def _book_md(bid, title, short, pages, meta, chs, tname):
    z = ZH.get(bid, {})
    zhb = z.get("book_title_zh", "")
    L = ["# %s %s\n" % (bid, title), "`%s · %s · %d 页 · %d 章`\n" % (meta, zhb, pages, len(chs)),
         "路径：%s → %s" % (tname, short), "", "```mermaid", "mindmap", "  root((%s))" % mermaid_safe(short)]
    zchs = z.get("chapters_zh") or []
    zsecs = z.get("sections_zh") or []
    secs = SEC.get(bid, [])
    for i, (ctitle, page, gist, tag) in enumerate(chs, 1):
        zhc = zchs[i - 1] if i - 1 < len(zchs) else ""
        L.append("    %s" % mermaid_safe("%s %s · p%d · %s" % (ctitle, "／" + zhc if zhc else "", page, tag)))
        rows = secs[i - 1] if i - 1 < len(secs) else []
        zrow = zsecs[i - 1] if i - 1 < len(zsecs) else []
        for j, (st, sp) in enumerate(rows[:14]):
            zs = zrow[j] if j < len(zrow) else ""
            L.append("      %s" % mermaid_safe("%s %s · p%d" % (st, "／" + zs if zs else "", sp)))
            for pt in (POINTS.get(bid, {}).get("%d.%d" % (i, j + 1)) or [])[:3]:
                L.append("        %s" % mermaid_safe("· " + pt))
        if len(rows) > 14:
            L.append("      %s" % mermaid_safe("…另 %d 节" % (len(rows) - 14)))
    L.append("```")
    return "\n".join(L)


def build_md():
    idx = ["# 8 本书 · 中英对照思维导图（Mermaid）\n",
           "> 交互版（可缩放、五层折叠）见 `books-mindmap.html`。下面每本书单独一页，避免单文件过大。\n",
           "## 总览\n```mermaid\nmindmap\n  root((8 本书))"]
    for tname, ten, _, ids in TRACKS:
        idx.append("    %s" % mermaid_safe(tname))
        for bid, title, short, pages, meta, chs in BOOKS:
            if bid not in ids:
                continue
            zn = ZH.get(bid, {}).get("book_title_zh", "")
            idx.append("      %s" % mermaid_safe("%s %s · %s" % (bid, short, zn)))
    idx.append("```\n")
    idx.append("## 分册\n")
    files, rows = {}, []
    for tname, ten, _, ids in TRACKS:
        for bid, title, short, pages, meta, chs in BOOKS:
            if bid not in ids:
                continue
            fn = "md/%s-%s.md" % (bid, {"C++": "Cpp"}.get(short, short))
            files[fn] = _book_md(bid, title, short, pages, meta, chs, tname)
            rows.append((bid, fn, short, ZH.get(bid, {}).get("book_title_zh", title)))
    for bid, fn, short, zhb in sorted(rows):
        idx.append("- [[%s|%s %s]] — %s" % (fn[:-3], bid, short, zhb))
    return "\n".join(idx), files


def main():
    data = build_data()
    nch = sum(len(b[5]) for b in BOOKS)
    nsec = sum(len(r) for v in SEC.values() for r in v)
    npt = sum(len(pts) for v in POINTS.values() for pts in v.values())
    stat = "2960 页 · %d 章 · %d 节 · %d 要点" % (nch, nsec, npt)
    html = (HTML.replace("__DATA__", json.dumps(data, ensure_ascii=False))
                .replace("__TAGS__", json.dumps(TAG_COLOR, ensure_ascii=False))
                .replace("__STAT__", stat))
    open(os.path.join(HERE, "books-mindmap.html"), "w", encoding="utf-8").write(html)
    idx, files = build_md()
    open(os.path.join(HERE, "books-mindmap.md"), "w", encoding="utf-8").write(idx)
    os.makedirs(os.path.join(HERE, "md"), exist_ok=True)
    for fn, body in files.items():
        open(os.path.join(HERE, fn), "w", encoding="utf-8").write(body)
    print("html + md written; books with zh:", sorted(ZH))


if __name__ == "__main__":
    main()
