// dsh-study：把 8 本书的学习路线接进对话。
//
// 刻意不 import '@deepseek-ai/dsh-tools'：
// 该包是宿主内置的核心包，若写进 dependencies，pnpm(hoisted) 会把它提到 profile 的
// node_modules 顶层，顶掉宿主自带版本 → include:tools 无法激活 → DSH 启动失败。
// （0.2.0 / 0.2.1 的崩溃原因）
// ToolsService.register 接受普通对象定义，不需要 defineTool 包装。
import { catalogTool } from './tools/catalog.js'
import { lessonTool } from './tools/lesson.js'
import { searchTool } from './tools/search.js'
import { progressTool } from './tools/progress.js'
import { content } from './content.js'

export const inject = ['tools']

export function apply(ctx) {
  const c = content()
  const count = Object.keys(c.lessons).length

  for (const def of [catalogTool, lessonTool, searchTool, progressTool]) {
    ctx.tools.register(def)
  }

  ctx.logger?.info?.(`dsh-study loaded: ${count} lessons, ${c.concepts.nodes.length} concepts, v${c.version}`)
}
