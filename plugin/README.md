# dsh-study 插件

把 8 本书的学习路线接进 DeepSeek Harness：在任意对话里说「我想学 LLM」，agent 就会逐关带你学。

## 三个工具

| 工具 | 作用 |
|---|---|
| `study_catalog` | 列出 4 条路线，或某条线的关卡清单 |
| `study_lesson` | 取一关的完整内容（可用 `section` 只取一部分） |
| `study_search` | 搜关卡 / 概念 / 书章 |
| `study_progress` | 查看进度 / 标记完成（写 `~/.dsh/study-progress.json`） |

## 安装

### 从 npm（发布后）

```bash
dsh plugin add dsh-study
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

> 为什么要 `pnpm install`：这一版从 `@deepseek-ai/dsh-tools` 导入 `defineTool`，
> 依赖写在 `package.json` 里，但本地目录安装是软链，不会替你装依赖。

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
