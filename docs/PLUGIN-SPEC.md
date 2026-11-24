# dsh-study · 插件规格 v0.1

> 一句话：把「4 条学习路线 + 51 个概念 + 8 本书的章节索引」装进 DSH，
> 任何人在自己的会话里说一句「我想学 LLM」，agent 就能按固定套路带着学、出题、判分、记进度。

状态：**设计稿 v0.2**（未实现）。已拍板：公开发布到 npm；v0.1 的 HTML 只给路径。

---

## 一、目标与非目标

### 目标

1. 用户装一次插件，**在任意会话里**都能开始学习，不依赖某个特定对话的历史。
2. agent 知道「现在该学哪一关、这关讲什么、学完该回书哪一章」。
3. 学习进度可跨会话、跨天延续。
4. 内容与代码分离：以后加一关只改 JSON。

### 非目标（v0.1 明确不做）

- 不做账号体系、不做多人进度同步。
- 不做考试/证书/排行榜。
- 不做模型训练类的实操环境（只给代码，用户自己跑）。
- 不做内容编辑器（改内容直接改 JSON 再重打包）。

---

## 二、三个用户旅程（验收就按这三个走）

### 旅程 A：第一次使用

```
用户：我装了学习插件，怎么开始？
agent：（调用 study_catalog）你有 4 条路线：LLM / 量化 / 文本 / C++。
       LLM 线 11 关，前 3 关是零基础起步。想从哪条开始？
用户：LLM
agent：（调用 study_lesson llm1）开始第 1 关「从打开终端开始」…
```

### 旅程 B：学一关（核心循环）

```
agent：（调用 study_lesson l7）
  1. 抛钩子：「一份合约：一年后股价高于 100 就付你差价…你愿意出多少钱？」
  2. 讲 3 个概念（复制的说法，不照抄术语）
  3. 给 3 步代码，要求用户跑完贴回输出
  4. 用户贴回结果 → agent 对照预期输出判断
  5. 出 3 道自测题 → 用户答 → agent 判分并解释
  6. 达标 → （调用 study_progress mark）→ 提示「回书：FTP 第 2 章 p.33–74，目的是推导」
```

### 旅程 C：跨天继续

```
用户：我昨天学到哪了？
agent：（调用 study_progress）你停在量化线第 6 关「第一次回测」，已完成 5/13。
       继续的话，先说说上次那个「扣费后年化 35%」你怎么理解？
```

---

## 三、内容资产（现成的，只需打包）

| 现有文件 | 内容 | 约体积 |
|---|---|---|
| `course/llm_lessons.json` 等 4 个 | 41 关的正文 | 110 KB |
| `course/starter_*.json` | 3 关公共起步 | 7 KB |
| `graph/concepts.json` | 51 个概念（含白话/定义/误解/例子） | 28 KB |
| `mindmap/sections.json` | 1229 节的章节-页码索引 | 73 KB |
| `mindmap/i18n/zh/*.json` | 章/节中文名 | 30 KB |
| `course/build_course.py` 里的 `READLIST` / `READBACK` | 8 本书 + 22 章回书清单 + 每关回书目的 | 导出为 JSON |

**打包决策**：合并成一个 `content.json`（约 250 KB），插件启动时一次读进内存。理由：工具实现只需读一个文件，不依赖工作区路径，方便分发。

打包脚本 `pack_content.py` 的职责：
- 读取上述来源
- 校验：每关 3 概念 / 3 步骤 / 3 自测；章节号存在；页码单调
- 输出 `content.json` + 一份 `content.md5`

---

## 四、插件结构

```
dsh-study/
├─ package.json
│   { "name": "@local/dsh-study", "type": "module",
│     "exports": { ".": "./index.js", "./locale/*.json": "./locale/*.json", "./icon": "./icon.svg" },
│     "dsh": { "bundle": { "patch": "./cordis.patch.yml" } },
│     "files": ["index.js", "cordis.patch.yml", "tools", "content", "skills", "locale", "docs", "icon.svg"] }
├─ cordis.patch.yml        insert: dsh-study（id/name/config）
├─ index.js                export function apply(ctx, config)；inject: ['tools']
├─ tools/
│   ├─ catalog.js          study_catalog
│   ├─ lesson.js           study_lesson
│   ├─ search.js           study_search
│   ├─ book.js             study_book
│   └─ progress.js         study_progress
├─ content/content.json    打包产物
├─ skills/study-tutor/SKILL.md   教学协议（见第六节）
├─ locale/zh.json, en.json       meta.title / description / detail
├─ docs/DETAIL.md          插件详情页
└─ icon.svg                原创图标
```

> 注意：`files` 必须列全，否则打包后缺文件；本地目录安装是软链，不校验 `files`，但发布时必须对。

---

## 五、工具契约（5 个，全部有界输出）

### 1. `study_catalog`

| 项 | 值 |
|---|---|
| 参数 | `track?`（llm/quant/nlp/cpp，缺省返回全部） |
| 返回 | 每条线：名称、关卡数、总时长、当前进度、下一关 id |
| 用途 | 开场、让用户选路线 |

### 2. `study_lesson`

| 项 | 值 |
|---|---|
| 参数 | `id`（如 `l7`、`llm3`）；`section?`（intro/concepts/steps/quiz/readback，缺省全部） |
| 返回 | 该关的 hook、goals、3 概念、3 步骤（含预期输出）、3 自测（含答案）、回书指引 |
| 用途 | 教这一关 |
| 注意 | 答案默认**放在最后并标注**，agent 应先出题再引用答案 |

### 3. `study_search`

| 项 | 值 |
|---|---|
| 参数 | `query`；`limit?`（默认 8） |
| 返回 | 命中列表：`{kind: lesson\|concept\|chapter, id, title, snippet, ref}` |
| 用途 | 「鞅测度在哪」「回测在哪一关」 |

### 4. `study_book`

| 项 | 值 |
|---|---|
| 参数 | `code`（01–08） |
| 返回 | 书信息 + 必读章（页码/理由/回书目的）+ 可跳章 + 对应关卡 |
| 用途 | 「这本书要不要读」「这章是拓展还是佐证」 |

### 5. `study_progress`

| 项 | 值 |
|---|---|
| 参数 | `action`：`show` / `mark` / `unmark`；`lesson_id`（mark 时必填）；`track?` |
| 返回 | 当前进度：每条线 x/y、最近完成、下一关 |
| 存储 | `~/.dsh/study-progress.json`，schema 见第七节 |

---

## 六、教学协议（skill: `study-tutor`）

这是插件和"一堆 JSON"的本质区别。技能文件规定 agent 怎么教：

### 开场

- 先调 `study_catalog`，让用户选路线，**不超过 3 句话**。
- 用户没选就默认 LLM 线（最轻，不需要显卡）。

### 每关的六步循环

1. **钩子**：原文抛出，不加解释，问一句「你觉得答案大概是多少」。
2. **三个概念**：每个一句话，允许打比方，不许一次讲超过 3 个。
3. **动手**：给代码，**要求用户跑完贴回输出**。没贴就不判分。
4. **对照**：用户输出与预期不符时，先问「你看到什么」，再定位问题（编码/路径/版本）。
5. **自测**：一次只出一题，答完再下一题；答错先给提示，不直接给答案。
6. **收尾**：达标 → `study_progress mark` → 说清「回书哪一章、为什么去」→ 问是否继续。

### 硬性约束

- 一次回复**只推进一个环节**，不要一口气把 3 概念 + 3 步代码 + 3 题全倒出来。
- 用户没跑代码，就不许说「你应该看到 265.33」。
- 自测答错 2 次以上，退回上一关的概念，不要继续往下推。
- 涉及书的内容，必须给章节 + 页码，不给页码就等于没给。

---

## 七、进度模型

```json
{
  "version": 1,
  "updated": "2026-11-22T19:30:00+08:00",
  "tracks": {
    "llm": { "done": ["llm1", "llm2"], "current": "llm3" },
    "quant": { "done": [], "current": "start" }
  },
  "notes": { "l7": "第 2 次自测错在 2FTAP" }
}
```

- 路径：`~/.dsh/study-progress.json`（每用户一份，天然隔离）
- 写失败（权限/磁盘）→ 工具返回 warning，不阻塞教学
- 不写 DSH 的 profile 配置

---

## 八、里程碑与验收

### M1（0.5 天）内容 + 两个只读工具

交付：`content.json`、`study_catalog`、`study_lesson`
验收：
- 新会话说「有哪些路线」→ 返回 4 条线、关卡数正确
- 说「学第 7 关」→ 返回「什么叫公平的价格」的完整内容

### M2（0.5 天）搜索 + 进度 + 教学协议

交付：`study_search`、`study_progress`、`skills/study-tutor/SKILL.md`
验收：
- 说「鞅测度」→ 命中概念 + 《05 FTP》第 2 章 + 量化第 7 关
- 说「我学完第 6 关了」→ 打勾，返回下一关
- 说「我昨天学到哪」→ 返回进度摘要

### M3（1 天）书本工具 + 展示资源

交付：`study_book`、locale、icon、DETAIL.md、HTML 页面入口
验收：
- 说「这本书要读哪几章」→ 返回必读章 + 页码 + 目的
- Plugins 页能看到标题、图标、详情

### M4（可选）客户端页面

侧边栏「学习」页，内嵌 `course/index.html`，与工具共享进度。

---

## 九、发布到 npm（已拍板：公开）

### 名称与账号

- 实测：`dsh-study` **可用**（404）；`dsh-learning` 可用；`dsh-tutor` 已被占用。
- 建议名字：`dsh-study`（无 scope，用户搜索/安装最直观）。
- 备选：`@<你的npm账号>/dsh-study`（scope 包天然不重名，但安装时要打全名）。

### 发布前必须补齐

| 项 | 要求 |
|---|---|
| `package.json` | 去掉 `private: true`；`version` 从 `0.1.0` 起；加 `description`、`keywords`（dsh, plugin, learning, course）、`license`、`repository`、`engines.dsh` |
| `README.md` | 装什么、怎么用、三个示例对话、截图（可选） |
| `locale/en.json` | 英文标题与描述——公开包不给英文，非中文用户看到的是模板文案 |
| `files` | 列全：index.js / patch / tools / content / skills / locale / docs / icon.svg |
| `content.json` | 带 `version` 字段，工具返回时暴露，排查「内容旧了」用 |

### 发布步骤（需要你本人做的事标 ⚠️）

```powershell
# ⚠️ 需要你登录一次（会开浏览器，或给 token）
npm.cmd login

# 我这边准备 + 校验
npm.cmd pack --dry-run          # 看实际打进去的文件
npm.cmd publish --access public
```

**注意**：你机器上 `npm.ps1` 被执行策略拦了（`Restricted`），必须用 `npm.cmd` 而不是 `npm`。这和之前 conda 的坑是同一个原因。

### 发版规则

- 内容更新（加一关）→ 改 `content.json` 的 version + patch 版本号（`0.1.0 → 0.1.1`）
- 工具行为变化 → minor（`0.1.x → 0.2.0`）
- 每次发版前跑一遍三个验收旅程

## 十、风险与开放问题

| 风险 | 影响 | 对策 |
|---|---|---|
| 内容散在多个目录 | 打包易漏文件 | `pack_content.py` 统一产出 + md5 |
| 41 关内容进单文件 | 内存/启动 | 250 KB 可忽略 |
| 教学协议写太松 | agent 一口气倒完 | skill 里写死「一次一步」 |
| 多人分发时内容更新 | 版本不一致 | `content.json` 带 version，工具返回版本号 |
| 有人没装 Python | 第 1 关就卡 | 开场先问「你机器上有 python 吗」 |
| npm 名称被抢注 | 以后换名要改文档 | 先注册 `dsh-study`，或直接用 scope |
| `npm.ps1` 被执行策略拦 | 发布命令失败 | 一律用 `npm.cmd` |

**开放问题（需要拍板）**

1. 分发范围：只自己用（本地目录装）/ 给同事（内网包）/ 公开（npm）？
2. HTML 要不要进插件：v0.1 只给路径让人用浏览器打开，还是 M4 做内嵌页面？
3. 内容语言：先中文，英文版以后再说？

---

## 十二、缺陷记录（0.2.0 / 0.2.1 → 0.2.2）

**现象**：安装后 DSH 重启直接打不开，报 `2 required plugins did not activate`。

**根因**：`package.json` 的 `dependencies` 里钉了 `@deepseek-ai/dsh-tools@0.2.2-rc.5`。
目标 profile 是 `nodeLinker: hoisted`，该包被提升到 profile 的 `node_modules/@deepseek-ai/dsh-tools`，
顶掉宿主内置版本；加载器解析 `include:tools` 时版本不符 → 该行 disabled → `tools` 服务永不激活
→ `tool-executor-native` 与 `agent-loop` 两个 required 插件不激活 → 启动致命失败。

**修复**：删除全部 dependencies 与 engines；`ctx.tools.register` 直接接受普通对象定义，
参数/输出改为标准 JSON Schema，不再 import `@deepseek-ai/dsh-tools`。

**规则（以后所有 DSH 插件都适用）**：
- 永不在 `dependencies` 里钉 `@deepseek-ai/*` 宿主内置包；
- 确需类型时用 `peerDependencies` 且不锁版本；
- 发版前在干净 profile 装一次并重启，检查 `crash-*-host.log` 里没有 `include:tools ... disabled`。

## 十一、交接给「创造模式」的一句话

> 读 `C:\Users\LENOVO\Downloads\新建文件夹\study\PLUGIN-SPEC.md`，
> 按 M1 先做出可安装的 v0.1：打包 content.json + 两个只读工具，装到当前 profile 并验证。
