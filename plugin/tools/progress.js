import { content, orderedLessons, nextLessonFor, lesson as getLesson } from '../content.js'
import { load, save, mark, unmark, trackState } from '../progress.js'
import { textOutput, ok } from './common.js'

function summaryLine(trackDef, state) {
  const ls = orderedLessons(trackDef.id)
  const t = state.tracks?.[trackDef.id] || { done: [], current: null }
  const done = ls.filter(l => t.done.includes(l.id)).length
  const next = nextLessonFor(ls, t.done)
  return {
    id: trackDef.id,
    name: trackDef.name,
    done,
    total: ls.length,
    current: t.current,
    next: next ? { id: next.id, title: next.title, min: next.min } : null,
  }
}

export const progressTool = {
  name: 'study_progress',
  description:
    '查看或更新学习进度：show 看每条线学到哪、下一关是什么；mark 把某一关标记为已完成；unmark 取消。进度存在本机，跨会话保留。',
  parameters: {
    action: {
      type: 'string',
      required: true,
      description: 'show = 查看；mark = 标记完成；unmark = 取消标记。',
    },
    lesson_id: { type: 'string', description: 'mark / unmark 时的关卡 id，例如 l7、llm3。' },
    track: { type: 'string', description: '只显示某条线（llm / quant / nlp / cpp）；省略则全部显示。' },
  },
  output: textOutput,
  execute: async (args) => {
    const action = String(args.action || 'show').toLowerCase()
    const state = load()
    const all = content().tracks

    if (action === 'show') {
      const list = args.track ? all.filter(t => t.id === args.track) : all
      if (!list.length) return ok(`没有这条路线：${args.track}。可选：${all.map(t => t.id).join(' / ')}`)
      const rows = list.map(t => summaryLine(t, state))
      const lines = ['# 学习进度', '']
      for (const r of rows) {
        lines.push(`## ${r.name}：${r.done} / ${r.total}`)
        if (r.next) lines.push(`下一关：[${r.next.id}] ${r.next.title} · ${r.next.min} 分钟`)
        else lines.push('这条线已经全部完成。')
        if (r.current) {
          const cur = getLesson(r.current)
          if (cur) lines.push(`最近完成：${cur.title}（${cur.id}）`)
        }
        lines.push('')
      }
      lines.push(`进度文件：${state.updated ? '最后更新 ' + state.updated : '还没记录过任何一关'}`)
      return ok(lines.join('\n'))
    }

    const lessonId = String(args.lesson_id || '').trim()
    if (!lessonId) return ok('mark / unmark 需要 lesson_id，例如 study_progress action=mark lesson_id=l7')

    const l = getLesson(lessonId)
    if (!l) return ok(`没有这一关：${lessonId}。可以先用 study_catalog 看关卡 id。`)
    const trackId = l.track
    if (!trackId) return ok(`这一关不属于任何路线：${lessonId}`)

    const isMark = action === 'mark'
    const before = (state.tracks?.[trackId]?.done || []).includes(lessonId)
    if (isMark) mark(state, trackId, lessonId)
    else unmark(state, trackId, lessonId)

    const res = save(state)
    const s = summaryLine(content().tracks.find(t => t.id === trackId), state)
    const lines = []
    if (isMark) {
      lines.push(before ? `这一关之前就标过了：${l.title}` : `已标记完成：${l.title}（${lessonId}）`)
    } else {
      lines.push(`已取消标记：${l.title}（${lessonId}）`)
    }
    lines.push(`${s.name}：${s.done} / ${s.total}`)
    if (s.next) lines.push(`下一关：[${s.next.id}] ${s.next.title} · ${s.next.min} 分钟`)
    else lines.push('这条线全部完成了。')
    if (!res.ok) lines.push(`⚠ 进度没能写入磁盘（${res.error}），本次会话有效，重启会丢。写在 ${res.path}`)

    // 回书指引：完成一关后顺手给
    if (isMark) {
      const c = content()
      const refs = c.lesson_books?.[lessonId] || []
      const rb = c.readback?.[lessonId]
      if (refs.length || rb) {
        lines.push('', '## 回书')
        if (rb) lines.push(`目的：**${rb[0]}** —— ${rb[1]}`)
        for (const [code, ch] of refs) {
          const book = c.books.find(b => b.code === code)
          const secs = c.sections?.[code]?.[ch - 1] || []
          const page = secs.length ? `p.${secs[0][1]}–${secs[secs.length - 1][1]}` : ''
          lines.push(`- 《${code} ${book?.short || ''}》第 ${ch} 章 ${page}`)
        }
      }
    }
    return ok(lines.join('\n'))
  },
}

export { trackState }
