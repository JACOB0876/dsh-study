# 学习包：8 本量化 / ML / LLM 书怎么用

这个文件夹不是书摘，是**使用说明**：告诉你 8 本书各自解决什么问题、按什么顺序读、哪些章可以跳过、
每本书最少读多少页、以及读完拿什么验收。

## 两套图怎么分工

- **`graph/index.html`（概念图谱）**：回答「这些概念是什么关系、我先学哪个」。零基础从它开始，点「从哪开始」。
  每张卡开头是「先说人话」的生活类比，往下才是专业定义——看不懂先读第一段。
  学完一个概念点卡片顶部「标记已懂」，圆点变绿、右上角出现 ✓，顶部显示 `已懂 n/51`（存在浏览器本地，
  点那个徽章可清空）。卡片底部「在哪本书」是个链接，**点一下直接跳到底图对应章节**。
- **`mindmap/books-mindmap.html`（目录树）**：回答「这个概念在哪本书第几页」。读书时定位用。

先在图谱里建骨架，再去目录树里找页码读原文。

## 从这里开始（3 步）

1. 读 `00-学习路线.md` 的**第三节**，选一条路线（A 量化策略 / B LLM 工程 / C 量化开发）。
2. 按 `09-环境与代码.md` 配好 conda——**Anaconda 已装**（`C:\Users\LENOVO\anaconda3`，base 是 Python 3.14），
   差的是 PATH、以及给深度学习单独建一个 Python 3.12 环境。
3. 打开 `10-进度表.md`，把第 0 周那一行填上日期。

## 文件清单

| 文件 | 作用 |
|---|---|
| `00-学习路线.md` | 总览：8 本书定位、依赖关系、三条路线、16 周日程、必读集、6 个里程碑 |
| `09-环境与代码.md` | 本机实测环境、Python 安装、每本书的依赖、GPU 注意事项、踩坑清单 |
| `10-进度表.md` | 周进度 / 分书进度 / 里程碑，打勾用 |
| `course/` | **关卡式课程**（从这里开始）：`index.html`，4 条路线共 41 关（含公共 3 关零基础起步），每条线先有一页导言（干什么/学完能做什么/多久/往哪走），另有 8 本书总表与「回书清单」（22 章必读，可勾选）；`workbook.html` 是打印版 |
| `graph/` | **概念关系图谱**（推荐先看）：`index.html`，51 个概念、57 条前置关系；点节点出「人话 + 定义 + 例子」卡片，可标记已懂、可跳导图。文字在 `graph/i18n/plain/*.json` |
| `mindmap/` | 五层目录树：`books-mindmap.html`（查页码用）、`books-mindmap.md` + `md/*.md`（Obsidian 分册版） |
| `books/01`–`08` | 每本书一份导读卡：章节表（含 PDF 页码）、核心概念、公式、代码仓库、怎么读、自测题 |

## 思维导图怎么用

打开 `mindmap/books-mindmap.html`（双击即可，不需要联网）：

完整五层：**分支 → 书 → 章 → 小节 → 要点**。

- 默认显示 **5 个分支 → 8 本书**；**点书**展开章节（一次一本，互斥）。
- **点章**展开小节清单；**点小节**展开该节的要点/概念（第 5 层）。
- **每个节点都是中英对照**：英文原标题在上，中文译名在下。
- 节点右侧是 `p.页码 · 精读/选读/快读 · N 节 / N 点`。
- 深链：`#02` 书、`#05-2` 章、`#03-1-2` 小节（打开即展开对应层级）。
- 顶部可切换分支（数据 / 金融 / 策略 / 文本 / 工程），也可搜索章节名。
- 滚轮缩放、拖动平移；「适配窗口」回到全局。
- 深链：`books-mindmap.html#02` 打开第 2 本；`books-mindmap.html#05-2` 打开第 5 本第 2 章并展开小节。

Obsidian 用户看 `mindmap/books-mindmap.md`：1 张总览 + 8 个分册链接，分册在 `mindmap/md/`。
每个分册是一张 Mermaid 图，层级写作
`Chapter ／章节中文 · p页码` → `Section ／小节中文 · p页码` → `· 要点`。

译名与要点都是数据文件，改完重跑 `build_mindmap.py` 即可：

- 中文译名：`mindmap/i18n/zh/b01.json`–`b08.json`
- 章节要点：`mindmap/i18n/points/bXX-cNN.json`（每节 2–3 条，格式 `{"3.2": ["…","…"]}`）

## 8 本书速查

| # | 书 | 页 | 难度 | 一句话 | 什么时候读 |
|---|---|---|---|---|---|
| 01 | Python Data Science Handbook | 548 | ★★☆ | NumPy/Pandas/sklearn 底座 | 第 1 周开始 |
| 02 | ML with Python Cookbook (2e) | 404 | ★★☆ | 配方集，按需查 | 第 9 周起当手册 |
| 03 | Blueprints for Text Analytics | 422 | ★★★ | 文本→模型的工程闭环 | 路线 B |
| 04 | Hands-On LLM Serving (2026) | 372 | ★★★★ | 推理部署与优化 | 路线 B/C |
| 05 | Financial Theory with Python | 204 | ★★★ | 无套利→鞅定价 | 第 5 周（**先读它**） |
| 06 | RL for Finance | 215 | ★★★★ | DQN 做交易/对冲/配置 | 第 14 周 |
| 07 | Deep Learning for Finance | 362 | ★★★ | 指标 + DL 策略流水线 | 第 10 周 |
| 08 | Learning Modern C++ for Finance | 431 | ★★★★ | C++11→23 写定价代码 | 路线 C |

## 跨书概念对照（同一个概念在哪几本出现）

学的时候合并成一张卡，不要每本书记一遍。

| 概念 | 出现处 |
|---|---|
| 交叉验证 / 网格搜索 | PDSH 第 5 章；MLCK 第 11–12 章；NLP 第 6 章；DLF 第 7、9 章 |
| 特征工程（滞后/滚动/交互） | MLCK 第 4、7 章；DLF 第 7 章；RLF 第 3 章 |
| 蒙特卡洛 | FTP 第 5–6 章；C++ 第 6 章；RLF 第 4 章 |
| 风险中性测度 / 鞅 | FTP 第 2–3、5 章（RLF 第 7 章用它做对冲环境） |
| BSM 与希腊字母 | FTP 第 5–6 章；C++ 第 2 章；RLF 第 7 章；DLF 第 10 章 |
| 神经网络训练（反向传播/优化器） | PDSH 第 5 章；MLCK 第 21 章；DLF 第 4、8 章；RLF 第 2 章 |
| 序列模型（RNN/LSTM/TCN） | DLF 第 8–9 章；NLP 第 11 章（BERT 对照） |
| 强化学习（Bellman、DQN、actor-critic） | RLF 第 2–3、9 章；DLF 第 10 章（仅 14 页）；LLM 第 10 章（RL serving） |
| 文本表示（TF-IDF → embedding） | NLP 第 5、10–11 章；MLCK 第 6 章 |
| Transformer / 注意力 | NLP 第 11 章（BERT）；LLM 第 2 章（KV cache）；DLF 第 9 章 |
| 模型部署 | MLCK 第 23 章；NLP 第 13 章；LLM 全书 |
| 性能优化（缓存/批处理/并行） | LLM 第 5–8 章；C++ 第 6、8 章（并发与表达式模板） |

## 三本 Hilpisch / Kaabar 的关系（容易混）

- **FTP**：价格为什么是这个数（理论，几乎不碰真实数据）。
- **DLF**：用历史数据预测方向（工程，技术指标 + ML/DL + 回测）。
- **RLF**：把决策写成序贯问题（方法论，交易/对冲/配置/执行各一个环境）。
  三者不重复，但 RLF 第 7 章需要 FTP 第 5–6 章的 BSM 与蒙特卡洛。

## 原始材料

- **8 本书 PDF 已归档**到 `../pdfs/`，按本学习包编号重命名（`01-Python-Data-Science-Handbook.pdf` 等），
  与 `books/01`–`08` 一一对应。微信缓存目录会被清理，**以后只认这个副本**。
- 全文转录：`../extracted/*.txt`（每页前有 `=== PAGE n ===`，可直接全文搜索）。
- 转录工具：`C:\Users\LENOVO\.agents\tools\pdfx\pdfx.py`，以后收到新的 PDF 直接：
  ```powershell
  & 'C:\Users\LENOVO\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe' `
    C:\Users\LENOVO\.agents\tools\pdfx\pdfx.py "D:\新书.pdf" -o "D:\新书.txt"
  ```
