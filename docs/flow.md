# 插件工作流程（v0.1）

图见 [flow.png](flow.png)（GitHub 可直接看 Mermaid 版，见下）。

```mermaid
flowchart TD
  U1["用户：我想学 LLM"] --> A1["Agent → study_catalog()"]
  A1 --> P1["插件：content.js 读 content.json"]
  P1 --> D1[("content.json · 321 KB<br/>41 关 / 51 概念 / 8 本书")]
  P1 --> P2["返回 4 条路线 + 关卡数"]
  P2 --> A2["Agent：让用户选路线"]
  A2 --> U2["用户：LLM，零基础"]
  U2 --> A3["Agent → study_lesson(id)"]
  A3 --> P3["返回一关的五段内容"]
  P3 --> D2[("lesson_books + readback<br/>哪本书第几章、为什么去")]
  P3 --> LOOP

  subgraph LOOP["教学循环（一次只推进一格）"]
    B1["① 抛钩子 + 三个概念"] --> B2["② 给代码，要求贴输出"]
    B2 --> U3["用户：跑代码、贴结果"]
    U3 --> B3["③ 对照预期输出定位问题"]
    B3 --> B4["④ 一次一题地自测"]
    B4 --> U4["用户答题"]
    U4 --> B5["⑤ 收尾 + 回书指引"]
  end

  B5 --> END1["用户：去翻书 / 下一关"]
  A1 -.-> S["study_search（可选）<br/>搜概念与章节"]
  B5 -.-> GAP["缺口（M2）：进度不落盘<br/>学完不打勾、跨会话不连续"]
```

## 两条离线链路

**内容构建**（改完内容要重跑）：

```
course/*.json + graph/concepts.json + mindmap/sections.json + readlist/readback
   → scripts/pack_content.py（校验：每关 3 概念 / 页码存在性）
   → plugin/content/content.json
```

**安装**（一次即生效，重启后仍在）：

```
git clone → plugin/ pnpm install → DSH Plugins → Add plugin → 工具注入所有会话
```
