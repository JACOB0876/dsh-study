# -*- coding: utf-8 -*-
"""Build the concept graph (single self-contained HTML) from concepts.json."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(open(os.path.join(HERE, "concepts.json"), encoding="utf-8"))

# 各书章的 PDF 起始页（与 build_mindmap.py 的 BOOKS 一致），用于把 refs 页码映射成 #书-章
CHAPTER_STARTS = {
    "01": [19, 51, 115, 235, 349],
    "02": [9, 27, 42, 77, 96, 108, 125, 138, 168, 180, 190, 217, 230, 240, 259, 270, 276, 286, 293, 301, 312, 344, 354],
    "03": [23, 55, 79, 111, 143, 173, 205, 229, 265, 289, 317, 345, 381],
    "04": [19, 49, 83, 125, 175, 207, 251, 289, 311, 333],
    "05": [17, 33, 75, 99, 133, 163, 185],
    "06": [17, 33, 51, 65, 81, 99, 119, 143, 181, 203],
    "07": [17, 35, 51, 97, 151, 167, 193, 231, 265, 293, 307, 341],
    "08": [23, 55, 85, 125, 165, 199, 247, 299, 345, 379],
}


def chapter_of(bid, page):
    starts = CHAPTER_STARTS.get(bid) or []
    best = None
    for i, p in enumerate(starts, 1):
        if page >= p:
            best = i
    return best


# 白话改写（子智能体产出）覆盖原字段
PLAIN = {}
_pdir = os.path.join(HERE, "i18n", "plain")
if os.path.isdir(_pdir):
    for _fn in sorted(os.listdir(_pdir)):
        if not _fn.endswith(".json"):
            continue
        try:
            PLAIN.update(json.load(open(os.path.join(_pdir, _fn), encoding="utf-8")))
        except Exception as _e:
            print("skip", _fn, _e)
for _n in DATA["nodes"]:
    _ov = PLAIN.get(_n["id"])
    if _ov:
        for _k in ("hook", "plain", "why", "myth", "ex"):
            if _ov.get(_k):
                _n[_k] = _ov[_k]

for _n in DATA["nodes"]:
    for _r in _n.get("refs", []):
        m = re.match(r"(\d{2})", str(_r.get("b", "")))
        pg = re.sub(r"[^0-9]", "", str(_r.get("p", ""))[:4])
        if m and pg and m.group(1) in CHAPTER_STARTS:
            ch = chapter_of(m.group(1), int(pg))
            if ch:
                _r["link"] = "../mindmap/books-mindmap.html#%s-%d" % (m.group(1), ch)

HTML = r"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<title>8 本书 · 概念关系图谱</title>
<style>
  :root{--bg:#f6f8fc;--ink:#0f172a;--muted:#64748b;--line:#e2e8f0}
  *{box-sizing:border-box}
  html,body{margin:0;height:100%;overflow:hidden;background:var(--bg);color:var(--ink);
    font-family:"Segoe UI","Microsoft YaHei","PingFang SC",system-ui,sans-serif}
  body{background:var(--bg) radial-gradient(circle at 1px 1px,#dde6f1 1px,transparent 0) 0 0/26px 26px}
  #bar{position:fixed;top:0;left:0;right:0;height:58px;display:flex;align-items:center;gap:9px;padding:0 18px;
    background:#fffdfa;border-bottom:1px solid var(--line);z-index:20;box-shadow:0 1px 10px #0f172a0a}
  #bar h1{font-size:15.5px;margin:0 6px 0 0;font-weight:700;white-space:nowrap}
  #bar h1 small{font-weight:500;color:var(--muted);font-size:11.5px;margin-left:7px}
  .hint{font-size:11.5px;color:var(--muted);margin-right:auto;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  button{font:inherit;font-size:12.5px;padding:7px 12px;border:1px solid #d7e0ec;background:#fff;border-radius:9px;
    cursor:pointer;color:#334155;white-space:nowrap;transition:.15s}
  button:hover{background:#f1f5fb;border-color:#a9bcd2;transform:translateY(-1px)}
  button.on{background:#0f172a;color:#fff;border-color:#0f172a}
  input{font:inherit;font-size:12.5px;padding:7px 12px;border:1px solid #d7e0ec;border-radius:9px;width:150px;outline:none}
  input:focus{border-color:#2563eb;box-shadow:0 0 0 3px #2563eb18}
  #chips{position:fixed;left:18px;bottom:16px;display:flex;gap:7px;flex-wrap:wrap;max-width:60vw;z-index:15}
  .chip{font-size:11.5px;padding:5px 10px;border-radius:20px;background:#fff;border:1px solid #e2e8f0;color:#475569;
    cursor:pointer;display:flex;align-items:center;gap:6px;user-select:none}
  .chip i{width:8px;height:8px;border-radius:50%;display:inline-block}
  .chip.off{opacity:.35}
  svg{width:100%;height:100%;display:block;cursor:grab}
  svg.drag{cursor:grabbing}
  .link{stroke-linecap:round;fill:none}
  .node circle{cursor:pointer;transition:r .15s,opacity .15s}
  .node text{pointer-events:none;text-anchor:middle;font-size:12px;fill:#334155}
  .node.dim{opacity:.15}
  .link.dim{opacity:.05}
  .node.hot circle{stroke:#0f172a;stroke-width:2.2}
  .node.hot text{font-weight:700;fill:#0f172a}
  #panel{position:fixed;top:58px;right:0;bottom:0;width:392px;background:#fff;border-left:1px solid var(--line);
    transform:translateX(100%);transition:transform .22s ease;z-index:18;display:flex;flex-direction:column;
    box-shadow:-8px 0 30px #0f172a0d}
  #panel.open{transform:none}
  #panel .head{padding:20px 22px 14px;border-bottom:1px solid #eef2f7}
  #panel .head .cz{font-size:19px;font-weight:700;letter-spacing:.3px}
  #panel .head .en{font-size:12.5px;color:var(--muted);margin-top:3px;font-style:italic}
  #panel .tags{display:flex;gap:6px;margin-top:10px;flex-wrap:wrap}
  .tag{font-size:10.5px;padding:3px 8px;border-radius:20px;background:#f1f5f9;color:#475569}
  .knowtag{border:none;cursor:pointer;background:#ecfdf5;color:#047857;font-weight:600;font-size:11px}
  .knowtag:hover{background:#d1fae5}
  #panel .body{padding:16px 22px 40px;overflow:auto;font-size:13.4px;line-height:1.78}
  #panel h4{font-size:11.5px;color:#94a3b8;letter-spacing:1.2px;margin:20px 0 6px;font-weight:600}
  #panel p{margin:0 0 6px}
  #panel .ex{font-family:Consolas,ui-monospace,monospace;font-size:12px;background:#f8fafc;border:1px solid #eef2f7;
    border-radius:8px;padding:9px 11px;color:#0f172a;overflow:auto;white-space:pre-wrap}
  #panel .hook{font-size:14.6px;line-height:1.85;color:#0f172a;background:#f8fafc;
    border-left:3px solid #93c5fd;border-radius:0 9px 9px 0;padding:12px 14px;margin:0 0 4px}
  #panel .myth{background:#fff7ed;border:1px solid #fed7aa;border-radius:8px;padding:9px 11px;color:#9a3412;font-size:12.8px}
  #panel .rel{display:flex;flex-wrap:wrap;gap:6px;margin-top:4px}
  #panel .rel span{font-size:12px;padding:4px 9px;border-radius:7px;background:#eff6ff;color:#1d4ed8;cursor:pointer}
  #panel .rel span:hover{background:#dbeafe}
  #close{position:absolute;top:14px;right:16px;border:none;background:none;font-size:19px;color:#94a3b8;cursor:pointer}
  #legend{position:fixed;top:70px;left:18px;background:#fff;border:1px solid var(--line);border-radius:12px;
    padding:10px 13px;font-size:11px;color:#475569;z-index:12;display:none}
  #legend div{display:flex;align-items:center;gap:7px;margin:3px 0}
  #legend i{width:9px;height:9px;border-radius:50%}
  #tip{position:fixed;right:18px;bottom:16px;font-size:11px;color:#94a3b8;z-index:12}
  #prog{font-size:12px;padding:6px 11px;border-radius:20px;background:#ecfdf5;color:#047857;
    border:1px solid #a7f3d0;white-space:nowrap;cursor:pointer;user-select:none}
  #prog:hover{background:#d1fae5}
  .knowbtn{width:100%;margin-top:16px;padding:11px;border-radius:10px;border:1px solid #a7f3d0;
    background:#ecfdf5;color:#047857;font-weight:600;cursor:pointer}
  .knowbtn.on{background:#047857;color:#fff;border-color:#047857}
  .knowbtn:hover{filter:brightness(.97)}
  .reflink{display:flex;align-items:center;justify-content:space-between;gap:8px;margin:6px 0;
    padding:8px 11px;border:1px solid #e2e8f0;border-radius:9px;background:#fff;color:#1e293b;
    text-decoration:none;font-size:12.8px;transition:.15s}
  .reflink:hover{border-color:#93c5fd;background:#f8fbff;transform:translateX(2px)}
  .reflink b{font-weight:600;color:#2563eb;font-size:11.5px;white-space:nowrap}
  .reflink.disabled{opacity:.6;cursor:default;transform:none}
  .node .done{stroke:#10b981;stroke-width:2.2}
  #barwrap{display:flex;align-items:center;gap:9px}
</style></head><body>
<div id="bar">
  <h1>概念关系图谱<small>__STAT__</small></h1>
  <button id="start">从哪开始</button>
  <button id="path">按学习阶段看</button>
  <button id="reset">复位</button>
  <button id="fit">适配</button>
  <span id="prog" title="点一下清除进度">已懂 0/50</span>
  <input id="q" placeholder="搜概念…">
  <span class="hint">滚轮缩放 · 拖动平移 · 点节点看解释 · 边上箭头表示「先学这个才能学那个」</span>
</div>
<svg id="map"><g id="scene">
  <g id="links"></g>
  <g id="nodes"></g>
</g></svg>
<div id="chips"></div>
<div id="legend"></div>
<div id="tip">节点越大 = 它被越多概念依赖（地基）</div>
<aside id="panel">
  <button id="close">×</button>
  <div class="head"><div class="cz"></div><div class="en"></div><div class="tags"></div></div>
  <div class="body"></div>
</aside>
<script>
const DATA = __DATA__;
const SVG = document.getElementById("map");
const scene = document.getElementById("scene");
const gLinks = document.getElementById("links");
const gNodes = document.getElementById("nodes");
const NS = "http://www.w3.org/2000/svg";

const nodes = DATA.nodes.map((n, i) => Object.assign({}, n, {ix: i}));
const byId = {}; nodes.forEach(n => byId[n.id] = n);
const links = [];
nodes.forEach(n => (n.pre || []).forEach(p => { if (byId[p]) links.push({ s: p, t: n.id }); }));
nodes.forEach(n => { n.deg = 0; });
links.forEach(l => { byId[l.s].deg++; byId[l.t].deg++; });
const maxDeg = Math.max(...nodes.map(n => n.deg));

/* ---------- layout ---------- */
const CL = DATA.clusters, CLK = Object.keys(CL);
const R = 430;
const centers = {};
CLK.forEach((k, i) => {
  const a = -Math.PI / 2 + i * 2 * Math.PI / CLK.length;
  centers[k] = { x: Math.cos(a) * R, y: Math.sin(a) * R };
});
nodes.forEach((n, i) => {
  const c = centers[n.c] || { x: 0, y: 0 };
  const a = Math.random() * Math.PI * 2, r = 60 + Math.random() * 120;
  n.x = c.x + Math.cos(a) * r; n.y = c.y + Math.sin(a) * r;
});

function simulate(iters) {
  const k = 1;
  for (let it = 0; it < iters; it++) {
    const alpha = 1 - it / iters;
    // repulsion
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const a = nodes[i], b = nodes[j];
        let dx = b.x - a.x, dy = b.y - a.y;
        let d2 = dx * dx + dy * dy || 1, d = Math.sqrt(d2);
        const f = Math.min(1500 / d2, 6) * alpha * k;
        dx /= d; dy /= d;
        a.x -= dx * f; a.y -= dy * f; b.x += dx * f; b.y += dy * f;
      }
    }
    // springs
    links.forEach(l => {
      const a = byId[l.s], b = byId[l.t];
      let dx = b.x - a.x, dy = b.y - a.y;
      let d = Math.sqrt(dx * dx + dy * dy) || 1;
      const f = (d - 120) * 0.020 * alpha;
      dx /= d; dy /= d;
      a.x += dx * f; a.y += dy * f;
      b.x -= dx * f; b.y -= dy * f;
      a.y += 0; b.y += 0;
    });
    // cluster + center gravity
    nodes.forEach(n => {
      const c = centers[n.c] || { x: 0, y: 0 };
      n.x += (c.x - n.x) * 0.022 * alpha;
      n.y += (c.y - n.y) * 0.022 * alpha;
      n.x += (0 - n.x) * 0.002 * alpha;
      n.y += (0 - n.y) * 0.002 * alpha;
    });
  }
}
simulate(900);

/* ---------- bounds (center the graph) ---------- */
let bx0 = 1e9, by0 = 1e9, bx1 = -1e9, by1 = -1e9;
nodes.forEach(n => { bx0 = Math.min(bx0, n.x); by0 = Math.min(by0, n.y); bx1 = Math.max(bx1, n.x); by1 = Math.max(by1, n.y); });
const gcx = (bx0 + bx1) / 2, gcy = (by0 + by1) / 2;
nodes.forEach(n => { n.x -= gcx; n.y -= gcy; });
nodes.forEach(n => { n.x *= 1.85; });   // 横向拉宽，避免图偏竖
// 归一化到目标画布，避免个别离群点把整体缩小
const w0 = Math.max(1, bx1 - bx0), h0 = Math.max(1, by1 - by0);
const kk = Math.min(1360 / w0, 700 / h0);
nodes.forEach(n => { n.x *= kk; n.y *= kk; });
let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
nodes.forEach(n => { x0 = Math.min(x0, n.x); y0 = Math.min(y0, n.y); x1 = Math.max(x1, n.x); y1 = Math.max(y1, n.y); });

/* ---------- draw ---------- */
const defs = document.createElementNS(NS, "defs");
defs.innerHTML = '<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#b7c6d8"/></marker>';
scene.insertBefore(defs, scene.firstChild);

function radius(n) { return 9 + 9 * Math.min(1, n.deg / Math.max(2, maxDeg)); }

links.forEach(l => {
  const a = byId[l.s], b = byId[l.t];
  const line = document.createElementNS(NS, "line");
  line.setAttribute("class", "link");
  line.setAttribute("x1", a.x); line.setAttribute("y1", a.y);
  line.setAttribute("x2", b.x); line.setAttribute("y2", b.y);
  line.setAttribute("stroke", CL[a.c].color);
  line.setAttribute("stroke-width", 1.15);
  line.setAttribute("opacity", .30);
  line.dataset.s = l.s; line.dataset.t = l.t;
  gLinks.appendChild(line);
});

const nodeEls = {};
nodes.forEach(n => {
  const g = document.createElementNS(NS, "g");
  g.setAttribute("class", "node");
  g.dataset.id = n.id;
  const c = document.createElementNS(NS, "circle");
  c.setAttribute("cx", n.x); c.setAttribute("cy", n.y); c.setAttribute("r", radius(n));
  c.setAttribute("fill", CL[n.c].color); c.setAttribute("fill-opacity", .92);
  c.setAttribute("stroke", "#fff"); c.setAttribute("stroke-width", 2);
  g.appendChild(c);
  const t = document.createElementNS(NS, "text");
  t.setAttribute("x", n.x); t.setAttribute("y", n.y + radius(n) + 15);
  t.setAttribute("style", "paint-order:stroke;stroke:#f6f8fc;stroke-width:3.2px;stroke-linejoin:round");
  t.textContent = n.zh;
  g.appendChild(t);
  gNodes.appendChild(g);
  nodeEls[n.id] = g;
  g.addEventListener("click", e => { e.stopPropagation(); openPanel(n.id); });
  g.addEventListener("mouseenter", () => highlight(n.id));
  g.addEventListener("mouseleave", () => highlight(null));
});

/* ---------- label collision ---------- */
(function resolveLabels(){
  const list = nodes.map(n => { const el = nodeEls[n.id].querySelector("text");
    return { el, x: n.x, y: n.y + radius(n) + 15, w: n.zh.length * 12.6 + 6 }; });
  list.sort((a, b) => a.y - b.y);
  const placed = [];
  list.forEach(it => {
    let y = it.y, guard = 0;
    while (guard++ < 60 && placed.some(p =>
      Math.abs(p.y - y) < 15.5 && Math.abs(p.x - it.x) < (p.w + it.w) / 2 - 4)) y += 15.5;
    it.el.setAttribute("y", y);
    placed.push({ x: it.x, y, w: it.w });
  });
})();

/* ---------- progress (localStorage) ---------- */
const PKEY = "concept-progress-v1";
let progress = {};
try { progress = JSON.parse(localStorage.getItem(PKEY) || "{}") || {}; } catch (e) { progress = {}; }
(function mergeKnowParam(){
  const raw = new URLSearchParams(location.search).get("know") ||
              (location.hash.startsWith("#know=") ? location.hash.slice(6) : "");
  if (!raw) return;
  raw.split(",").map(x => x.trim()).filter(Boolean).forEach(id => { if (byId[id]) progress[id] = true; });
  try { localStorage.setItem(PKEY, JSON.stringify(progress)); } catch (e) {}
})();
function saveProgress() { try { localStorage.setItem(PKEY, JSON.stringify(progress)); } catch (e) {} }
function updateProgPill() {
  const n = Object.keys(progress).filter(k => progress[k]).length;
  document.getElementById("prog").textContent = "已懂 " + n + "/" + nodes.length;
}
function paintNode(id) {
  const g = nodeEls[id]; if (!g) return;
  const c = g.querySelector("circle");
  const done = !!progress[id];
  c.setAttribute("stroke", done ? "#10b981" : "#fff");
  c.setAttribute("stroke-width", done ? 3.4 : 2);
  let badge = g.querySelector(".badge");
  if (done) {
    if (!badge) {
      badge = document.createElementNS(NS, "g");
      badge.setAttribute("class", "badge");
      badge.innerHTML = '<circle r="7.5" fill="#10b981" stroke="#fff" stroke-width="1.6"></circle>' +
                        '<text text-anchor="middle" dy="3.6" style="font-size:9.5px;font-weight:700" fill="#fff">✓</text>';
      g.appendChild(badge);
    }
    const r = +c.getAttribute("r");
    const cx = +c.getAttribute("cx"), cy = +c.getAttribute("cy");
    badge.setAttribute("transform", `translate(${cx + r * 0.78 + 3.5},${cy - r * 0.78 - 3.5})`);
  } else if (badge) badge.remove();
}
function toggleKnow(id) {
  progress[id] = !progress[id];
  if (!progress[id]) delete progress[id];
  saveProgress(); paintNode(id); updateProgPill();
}

nodes.forEach(n => paintNode(n.id));
updateProgPill();

/* ---------- interaction ---------- */
let scale = 1, tx = 0, ty = 0, dragging = false, lx = 0, ly = 0;
function apply() { scene.setAttribute("transform", `translate(${tx},${ty}) scale(${scale})`); }
function fit() {
  const w = innerWidth - 90, h = innerHeight - 190;
  const bw = (x1 - x0) + 180, bh = (y1 - y0) + 170;
  scale = Math.min(w / bw, h / bh, 1.6);
  tx = innerWidth / 2 - ((x0 + x1) / 2) * scale;
  ty = 58 + (innerHeight - 58) / 2 - ((y0 + y1) / 2) * scale;
  apply();
}
fit();
SVG.addEventListener("wheel", e => {
  e.preventDefault();
  const f = e.deltaY < 0 ? 1.12 : 1 / 1.12;
  const r = SVG.getBoundingClientRect();
  const mx = e.clientX - r.left, my = e.clientY - r.top;
  tx = mx - (mx - tx) * f; ty = my - (my - ty) * f; scale *= f; apply();
}, { passive: false });
SVG.addEventListener("mousedown", e => { dragging = true; lx = e.clientX; ly = e.clientY; SVG.classList.add("drag"); });
addEventListener("mousemove", e => { if (!dragging) return; tx += e.clientX - lx; ty += e.clientY - ly; lx = e.clientX; ly = e.clientY; apply(); });
addEventListener("mouseup", () => { dragging = false; SVG.classList.remove("drag"); });
document.getElementById("fit").onclick = fit;
function focusNode(id){
  const n = byId[id]; if(!n) return;
  tx = innerWidth/2 - (n.x*scale) - (panel.classList.contains("open")?196:0);
  ty = (innerHeight+58)/2 - n.y*scale;
  apply(); highlight(id);
}
document.getElementById("start").onclick = () => { openPanel("py"); focusNode("py"); };

function highlight(id) {
  document.querySelectorAll(".node").forEach(el => el.classList.remove("dim", "hot"));
  document.querySelectorAll(".link").forEach(el => el.classList.remove("dim"));
  if (!id) return;
  const nb = new Set([id]);
  links.forEach(l => { if (l.s === id) nb.add(l.t); if (l.t === id) nb.add(l.s); });
  document.querySelectorAll(".node").forEach(el => {
    if (!nb.has(el.dataset.id)) el.classList.add("dim");
  });
  document.querySelectorAll(".link").forEach(el => {
    if (el.dataset.s !== id && el.dataset.t !== id) el.classList.add("dim");
  });
  nodeEls[id].classList.add("hot");
}

/* ---------- panel ---------- */
const panel = document.getElementById("panel");
document.getElementById("close").onclick = () => { panel.classList.remove("open"); shiftForPanel(false); };
function stageName(lv) { const s = DATA.stages.find(x => x.id === lv); return s ? s.zh : ""; }
let panelShifted = false;
function shiftForPanel(on) {
  if (on === panelShifted) return;
  if (innerWidth < 1150) return;
  tx += on ? -210 : 210;
  panelShifted = on;
  apply();
}
function openPanel(id) {
  const n = byId[id];
  panel.querySelector(".cz").textContent = n.zh;
  panel.querySelector(".en").textContent = n.en;
  const knowLabel = () => progress[id] ? "✓ 已懂" : "标记已懂";
  panel.querySelector(".tags").innerHTML =
    `<span class="tag" style="background:${CL[n.c].color}1a;color:${CL[n.c].color}">${CL[n.c].zh}</span>` +
    `<span class="tag">阶段 ${n.lvl} · ${stageName(n.lvl)}</span>` +
    `<button class="tag knowtag" id="knowhead">${knowLabel()}</button>`;
  const body = panel.querySelector(".body");
  const next = links.filter(l => l.s === id).map(l => byId[l.t]);
  const pre = (n.pre || []).map(p => byId[p]).filter(Boolean);
  const refs = (n.refs || []).map(r => {
    if (r.link) return `<a class="reflink" href="${r.link}" target="_blank" rel="noopener"><span>《${r.b}》 ${r.p}</span><b>打开导图 →</b></a>`;
    return `<div class="reflink disabled"><span>《${r.b}》 ${r.p}</span><b>无图表</b></div>`;
  }).join("");
  body.innerHTML = `
    ${n.hook ? `<h4>先说人话</h4><div class="hook">${n.hook}</div>` : ""}
    <h4>正经定义</h4><p>${n.plain}</p>
    <h4>为什么重要</h4><p>${n.why}</p>
    <h4>常见误解</h4><div class="myth">${n.myth}</div>
    ${n.ex ? `<h4>最小例子</h4><div class="ex">${n.ex.replace(/</g, "&lt;")}</div>` : ""}
    <h4>先学</h4><div class="rel">${pre.length ? pre.map(p => `<span data-go="${p.id}">${p.zh}</span>`).join("") : "<span style='background:#f8fafc;color:#94a3b8'>无（可以从这里开始）</span>"}</div>
    <h4>学完可以看</h4><div class="rel">${next.length ? next.map(p => `<span data-go="${p.id}">${p.zh}</span>`).join("") : "<span style='background:#f8fafc;color:#94a3b8'>暂无</span>"}</div>
    <h4>在哪本书（点一下跳到导图）</h4>${refs || "<p>· 见 09-环境与代码.md</p>"}
    <button class="knowbtn" id="knowbtn">标记为已懂</button>`;
  body.querySelectorAll("[data-go]").forEach(s => s.onclick = () => openPanel(s.dataset.go));
  const kh = panel.querySelector("#knowhead");
  if (kh) kh.onclick = () => { toggleKnow(id); kh.textContent = knowLabel();
    const kb2 = body.querySelector("#knowbtn");
    if (kb2) { kb2.classList.toggle("on", !!progress[id]);
      kb2.textContent = progress[id] ? "✓ 已懂（点一下取消）" : "标记为已懂"; } };
  const kb = body.querySelector("#knowbtn");
  if (kb) {
    kb.classList.toggle("on", !!progress[id]);
    kb.textContent = progress[id] ? "✓ 已懂（点一下取消）" : "标记为已懂";
    kb.onclick = () => { toggleKnow(id); kb.classList.toggle("on", !!progress[id]);
      kb.textContent = progress[id] ? "✓ 已懂（点一下取消）" : "标记为已懂"; };
  }
  panel.classList.add("open");
  shiftForPanel(true);
}

/* ---------- chips ---------- */
const chips = document.getElementById("chips");
CLK.forEach(k => {
  const el = document.createElement("div");
  el.className = "chip";
  el.innerHTML = `<i style="background:${CL[k].color}"></i>${CL[k].zh}`;
  el.onclick = () => { el.classList.toggle("off"); applyFilter(); };
  chips.appendChild(el);
});
function applyFilter() {
  const off = [...document.querySelectorAll(".chip.off")].map(c => c.textContent.trim());
  const map = {}; CLK.forEach(k => map[CL[k].zh] = true);
  off.forEach(nm => { map[nm] = false; });
  let anyHidden = false;
  document.querySelectorAll(".node").forEach(el => {
    const n = byId[el.dataset.id];
    const on = map[CL[n.c].zh] !== false;
    if (!on) anyHidden = true;
    el.style.display = on ? "" : "none";
  });
  document.querySelectorAll(".link").forEach(el => {
    const a = byId[el.dataset.s];
    el.style.display = map[CL[a.c].zh] === false ? "none" : "";
  });
}

/* ---------- stage mode ---------- */
let stageMode = false;
const STAGE_COLORS = ["#94a3b8", "#0ea5e9", "#0891b2", "#7c3aed", "#059669", "#9333ea"];
document.getElementById("path").onclick = e => {
  stageMode = !stageMode;
  e.target.classList.toggle("on", stageMode);
  const legend = document.getElementById("legend");
  if (!stageMode) {
    legend.style.display = "none";
    document.querySelectorAll(".node circle").forEach(c => { const n = byId[c.parentNode.dataset.id]; c.setAttribute("fill", CL[n.c].color); });
    document.querySelectorAll(".node text").forEach(t => t.setAttribute("opacity", 1));
  } else {
    legend.style.display = "block";
    legend.innerHTML = DATA.stages.map(s => `<div><i style="background:${STAGE_COLORS[s.id]}"></i>阶段 ${s.id} · ${s.zh}</div>`).join("");
    document.querySelectorAll(".node circle").forEach(c => { const n = byId[c.parentNode.dataset.id]; c.setAttribute("fill", STAGE_COLORS[n.lvl]); });
  }
};

/* ---------- search ---------- */
document.getElementById("q").addEventListener("input", e => {
  const q = e.target.value.trim().toLowerCase();
  document.querySelectorAll(".node").forEach(el => {
    const n = byId[el.dataset.id];
    const hit = !q || n.zh.includes(q) || n.en.toLowerCase().includes(q) || (n.plain || "").includes(q);
    el.classList.toggle("dim", !hit);
  });
});

document.getElementById("prog").onclick = () => {
  if (!Object.keys(progress).length) return;
  if (!confirm("清除全部「已懂」标记？")) return;
  progress = {}; saveProgress(); nodes.forEach(n => paintNode(n.id)); updateProgPill();
};

/* ---------- reset ---------- */
document.getElementById("reset").onclick = () => {
  document.querySelectorAll(".chip").forEach(c => c.classList.remove("off"));
  applyFilter();
  if (stageMode) document.getElementById("path").click();
  document.getElementById("q").value = "";
  document.querySelectorAll(".node").forEach(el => el.classList.remove("dim"));
  panel.classList.remove("open");
  fit();
};
addEventListener("resize", () => setTimeout(fit, 80));
if (location.hash.startsWith("#know=")) { /* 仅标记进度 */ }
else if (location.hash && byId[location.hash.slice(1)]) setTimeout(() => openPanel(location.hash.slice(1)), 120);
</script></body></html>"""

def main():
    n_nodes = len(DATA["nodes"])
    n_edges = sum(len([p for p in n.get("pre", []) if p]) for n in DATA["nodes"])
    stat = "%d 个概念 · %d 条前置关系 · 按「零基础 + 两端都要」设计" % (n_nodes, n_edges)
    html = HTML.replace("__DATA__", json.dumps(DATA, ensure_ascii=False)).replace("__STAT__", stat)
    out = os.path.join(HERE, "index.html")
    open(out, "w", encoding="utf-8").write(html)
    print("wrote", out, len(html) // 1024, "KB")


if __name__ == "__main__":
    main()
