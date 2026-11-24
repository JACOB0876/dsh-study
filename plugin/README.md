# dsh-study 插件

把 8 本书的学习路线接进 DeepSeek Harness：在任意对话里说「我想学 LLM」，agent 就会逐关带你学。

## 三个工具

| 工具 | 作用 |
|---|---|
| `study_catalog` | 列出 4 条路线，或某条线的关卡清单 |
| `study_lesson` | 取一关的完整内容（可用 `section` 只取一部分） |
| `study_search` | 搜关卡 / 概念 / 书章 |
| `study_progress` | 查看进度 / 标记完成（写 `~/.dsh/study-progress.json`） |

## 设计约束（重要）

本插件**不声明任何 `dependencies`**，尤其不依赖 `@deepseek-ai/*` 这类宿主内置包。

原因：目标 profile 使用 `nodeLinker: hoisted`，若把宿主核心包写进 dependencies，
pnpm 会把它提升到 `~/.dsh/profiles/<profile>/node_modules/@deepseek-ai/dsh-tools`，
**顶掉宿主自带的版本**，导致加载器解析 `include:tools` 失败、DSH 启动直接打不开
（`2 required plugins did not activate`）。

工具用 `ctx.tools.register(普通对象)` 注册，不需要 `defineTool` 包装；
参数与输出都用标准 JSON Schema（`type/properties/required/additionalProperties`）。

## 安装

### 从 npm（推荐，已验证）

在 DSH 对话里让 agent 安装：

```
plugin_manager install_bundle  target: dsh-study      # 自动装最新版
```

### 从源码（当前可用）

```bash
git clone https://github.com/JACOB0876/dsh-study.git
cd dsh-study/plugin
pnpm install            # 关键：链接安装不会自动装依赖
```

然后在 DSH 里装这个目录：

```
plugin_manager install_bundle  →  target: <你克隆的路径>/plugin
```

或图形界面：**Plugins → Add plugin**，选这个目录。

> 0.2.2 起插件是零依赖的：`pnpm install` 只是让 pnpm 建立链接，不会装任何包。

## 用法

装好后新开一个会话：

```
你：我想学 LLM，但完全没基础
```

agent 会调用 `study_catalog` 列出路线，选定后 `study_lesson` 逐关带学。
想看某一关，可以说「学第 7 关」或「学 l7」；想找概念，说「鞅测度在哪」。

## 内容

- 4 条路线 41 关（3 关零基础起步，四条线共享）
- 51 个概念、8 本书、22 章必读清单
- 内容版本在 `content/content.json` 的 `version`，工具返回时带上

改内容：编辑仓库根目录的 `course/`、`graph/`、`mindmap/`，然后

```bash
python scripts/pack_content.py
```

## 限制

- 不提供原书 PDF
- 进度只存本机，不跨设备同步
- 不能替用户跑代码

## 开发

```
index.js           apply()，注册工具
content.js         读 content.json，做索引
tools/             三个工具 + common.js（输出契约）
scripts/pack_content.py   打包 content.json 并校验
content/content.json      打包产物（已入库）
```
