// dsh-study：把 8 本书的学习路线接进对话。
//
// 刻意不 import '@deepseek-ai/dsh-tools'：
// 该包是宿主内置的核心包，若写进 dependencies，pnpm(hoisted) 会把它提到 profile 的
// node_modules 顶层，顶掉宿主自带版本 → include:tools 无法激活 → DSH 启动失败。
// （0.2.0 / 0.2.1 的崩溃原因）
// ToolsService.register 接受普通对象定义，不需要 defineTool 包装。
import { readFileSync } from 'node:fs'
import { catalogTool } from './tools/catalog.js'
import { lessonTool } from './tools/lesson.js'
import { searchTool } from './tools/search.js'
import { progressTool } from './tools/progress.js'
import { content } from './content.js'

export const inject = ['tools']

/** 读教学协议正文（去掉 YAML frontmatter）。文件缺失时返回空串，不影响工具。 */
function readProtocol() {
  try {
    const raw = readFileSync(new URL('./skills/study-tutor/SKILL.md', import.meta.url), 'utf8')
    return raw.replace(/^---[\s\S]*?---\s*/, '').trim()
  } catch {
    return ''
  }
}

export function apply(ctx) {
  const c = content()
  const count = Object.keys(c.lessons).length

  for (const def of [catalogTool, lessonTool, searchTool, progressTool]) {
    ctx.tools.register(def)
  }

  // 把「教学协议」注册成一个 runtime skill（可选：宿主没有 skills 服务就跳过）。
  const protocol = readProtocol()
  if (protocol) {
    try {
      const skills = ctx.get?.('skills')
      if (skills && typeof skills.register === 'function') {
        skills.register({
          name: 'study-tutor',
          description: '用 dsh-study 的 41 关课程教一个零基础的人：一次只推进一个环节，先动手再讲解，学完打勾并给回书章节。',
          whenToUse: '用户想学某个主题、想继续上次的学习、或提到课程/关卡/概念时。',
          content: protocol,
          source: 'runtime',
        })
      }
    } catch (error) {
      ctx.logger?.warn?.(`dsh-study: 技能注册跳过（${error?.message ?? error}）`)
    }
  }

  ctx.logger?.info?.(`dsh-study loaded: ${count} lessons, ${c.concepts.nodes.length} concepts, v${c.version}`)
}
