import { content } from '../content.js'
import { textOutput, ok } from './common.js'

function score(hay, q) {
  const h = hay.toLowerCase()
  let n = 0
  let i = h.indexOf(q)
  while (i !== -1) { n += 1; i = h.indexOf(q, i + 1) }
  return n
}

export const searchTool = {
  name: 'study_search',
  description:
    '在课程、概念、书的章节里搜索关键词（中英均可）。返回命中的关卡/概念/书章，附带 id 与出处，供继续调用 study_lesson。',
  parameters: {
    query: { type: 'string', required: true, description: '关键词，例如「鞅测度」「回测」「PagedAttention」' },
    limit: { type: 'number', description: '最多返回几条，默认 8' },
  },
  output: textOutput,
  execute: async (args) => {
    const q = String(args.query || '').trim().toLowerCase()
    if (!q) return ok('请给一个关键词。')
    const limit = Math.min(Math.max(Number(args.limit) || 8, 1), 20)
    const c = content()
    const hits = []

    for (const l of Object.values(c.lessons)) {
      const hay = [l.title, l.hook, l.can, ...l.concepts.map(x => x.t + ' ' + x.en + ' ' + x.d)].join(' ')
      const s = score(hay, q)
      if (s) hits.push({ kind: 'lesson', id: l.id, title: l.title, score: s * 2, note: l.hook.slice(0, 60) })
    }

    for (const n of c.concepts.nodes) {
      const s = score([n.zh, n.en, n.plain, n.why].join(' '), q)
      if (s) hits.push({ kind: 'concept', id: n.id, title: `${n.zh}（${n.en}）`, score: s * 3, note: n.plain.slice(0, 60) })
    }

    for (const b of c.readlist) {
      for (const ch of b.need) {
        const s = score(ch.t + ' ' + ch.why, q)
        if (s) hits.push({ kind: 'chapter', id: `${b.code}-${ch.ch}`, title: `《${b.code} ${b.short}》第 ${ch.ch} 章 ${ch.t}`, score: s, note: `p.${ch.p} · ${ch.why}` })
      }
    }

    hits.sort((a, b) => b.score - a.score)
    const top = hits.slice(0, limit)
    if (!top.length) return ok(`没有找到「${args.query}」。换个关键词，或先用 study_catalog 看有哪些路线。`)

    const lines = [`# 搜索「${args.query}」：${hits.length} 条命中，显示前 ${top.length} 条`, '']
    for (const h of top) {
      const tag = h.kind === 'lesson' ? '关卡' : h.kind === 'concept' ? '概念' : '书章'
      lines.push(`- [${tag}] **${h.title}**（${h.id}）`)
      lines.push(`  ${h.note}`)
    }
    lines.push('', '关卡用 study_lesson；书章属于回书清单，可直接告诉用户章节与页码。')
    return ok(lines.join('\n'))
  },
}
