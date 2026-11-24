# 8 本书 · 学习路线（dsh-study）

把 8 本量化 / 机器学习 / LLM 的书，拆成**能跟着走的课程**：4 条路线、41 关、51 个概念、22 章必读清单。

不包含原书 PDF——那些请自行购买或借阅。本仓库只有我们自己的课程、卡片和索引。

## 在线访问（不用下载）

- 课程：<https://jacob0876.github.io/dsh-study/course/index.html>
- 目录树：<https://jacob0876.github.io/dsh-study/mindmap/books-mindmap.html>
- 概念图谱：<https://jacob0876.github.io/dsh-study/graph/index.html>

## 本地打开

下载后双击：

```
course/index.html      41 关课程（先看导言，再进第 1 关）
mindmap/books-mindmap.html   四层目录树（书 → 章 → 节 → 要点）
graph/index.html       51 个概念的关系图谱
```

不用装任何东西，浏览器打开即可。

## 四条路线

| 路线 | 关卡 | 覆盖的书 | 特点 |
|---|---|---|---|
| **LLM** | 8 + 3 关起步 | Hands-On LLM Serving, Blueprints NLP（部分） | 前 4 关调 API，后 4 关本地部署 |
| **量化** | 10 + 3 关起步 | PDSH, ML Cookbook, DLF, FTP, RLF | 算账 → 判断 → 回测 → 定价 → 决策 |
| **文本** | 5 + 3 关起步 | Blueprints for Text Analytics | 文本清洗、分类、主题、可解释 |
| **C++** | 6 + 3 关起步 | Learning Modern C++ for Finance | 编译 → 类 → 多态 → 并发 → Eigen |

三条零基础起步关（终端、变量、条件循环）四条线共享。

## 目录

```
course/          课程页面 + 工作簿（打印版）+ 内容 JSON + 构建脚本
mindmap/         目录树（交互版 + Mermaid 版 + 生成脚本）
graph/           概念图谱（单文件 HTML + 内容 JSON）
books/           每本书的导读卡（章节表、核心概念、怎么读）
docs/            学习路线、环境配置、进度表、插件设计
```

## 每关长什么样

一关 20–30 分钟，固定结构：

```
钩子（一个带数字的真实问题）
→ 三个概念（够用就行）
→ 三步代码（每步有预期输出）
→ 三道自测（先想再点开）
→ 回书指引（去书里哪一章、为什么去）
```

## 关于原书

仓库**不提供**这 8 本书的 PDF。课程里会写「《05 FTP》第 2 章 p.33–74」这种引用，你需要自己拿到书。

章节标题与页码属于事实性索引（和图书馆目录同类）；课程正文、概念卡片、图示均为原创。

## DSH 插件（已可安装）

`plugin/` 是一个 DeepSeek Harness 插件：装上后可以在任意对话里说「我想学 LLM」，agent 会逐关带你学。

四个工具：`study_catalog`（路线/关卡/进度）、`study_lesson`（一关的完整内容）、`study_search`（搜概念与章节）、`study_progress`（打勾与续学）。

**从 npm 安装**（推荐）：在 DSH 对话里让 agent 执行
`plugin_manager install_bundle  target: dsh-study`（自动装最新版）。

**从源码安装**：

```bash
git clone https://github.com/JACOB0876/dsh-study.git
cd dsh-study/plugin && pnpm install
# 然后在 DSH 里：Plugins → Add plugin → 选这个目录
```

详见 [`plugin/README.md`](plugin/README.md)，设计文档在 [`docs/PLUGIN-SPEC.md`](docs/PLUGIN-SPEC.md)。

## 许可

- 代码（`.py` / `.js` / 构建脚本）：MIT，见 [LICENSE](LICENSE)
- 文字内容（课程、卡片、JSON 数据）：CC BY 4.0，见 [CONTENT-LICENSE.md](CONTENT-LICENSE.md)

欢迎提 issue / PR 补充或纠正内容。
