// dsh-study：把 8 本书的学习路线接进对话。
// 只读内容，不写任何用户数据（M1 阶段）。
import { defineTool } from '@deepseek-ai/dsh-tools'
import { catalogTool } from './tools/catalog.js'
import { lessonTool } from './tools/lesson.js'
import { searchTool } from './tools/search.js'
import { content } from './content.js'

export const inject = ['tools']

export function apply(ctx) {
  const c = content()
  const count = Object.keys(c.lessons).length

  for (const def of [catalogTool, lessonTool, searchTool]) {
    ctx.tools.register(defineTool(def))
  }

  ctx.logger?.info?.('dsh-study loaded: %d lessons, %d concepts, v%s', count, c.concepts.nodes.length, c.version)
}
