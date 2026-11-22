import { content, lesson as getLesson } from '../content.js'
import { textOutput, ok } from './common.js'

function fmtList(items) {
  return items.map((x, i) => `${i + 1}. ${x}`).join('\n')
}

function fmtConcepts(cs) {
  return cs.map(c => `**${c.t}**（${c.en}）\n${c.d}`).join('\n\n')
}

function fmtSteps(steps) {
  return steps.map((s, i) => [
    `### 步骤 ${i + 1}`,
    s.text,
    '```',
    s.code,
    '```',
    s.out ? `预期输出：${s.out}` : '',
  ].filter(Boolean).join('\n')).join('\n\n')
}

function fmtQuiz(quiz) {
  const qs = quiz.map((q, i) => `${i + 1}. ${q.q}`).join('\n')
  const as = quiz.map((q, i) => `${i + 1}. ${q.a}`).join('\n')
  return `先只出第一题，等用户回答再判。\n\n${qs}\n\n答案（不要一次给出）：\n${as}`
}

function fmtReadback(id) {
  const c = content()
  const refs = c.lesson_books?.[id] || []
  const rb = c.readback?.[id]
  if (!refs.length && !rb) return ''
  const lines = ['## 回书指引']
  if (rb) lines.push(`目的：**${rb[0]}** —— ${rb[1]}`)
  for (const [code, ch] of refs) {
    const book = c.books.find(b => b.code === code)
    const secs = c.sections?.[code]?.[ch - 1] || []
    const page = secs.length ? `p.${secs[0][1]}–${secs[secs.length - 1][1]}` : ''
    lines.push(`- 《${code} ${book?.short || ''}》第 ${ch} 章 ${page}`)
  }
  return lines.join('\n')
}

export const lessonTool = {
  name: 'study_lesson',
  description:
    '取一关的完整内容：钩子、目标、三个概念、动手步骤（含预期输出）、自测题与答案、回书指引。一次只讲一个环节。',
  parameters: {
    id: {
      type: 'string',
      required: true,
      description: '关卡 id，例如 start / vars / llm2 / l7 / nlp3 / cpp5。可由 study_catalog 或 study_search 获得。',
    },
    section: {
      type: 'string',
      description: '只取某一部分：intro / concepts / steps / quiz / readback。省略返回全部。',
    },
  },
  output: textOutput,
  execute: async (args) => {
    const l = getLesson(String(args.id || '').trim())
    if (!l) {
      const ids = Object.keys(content().lessons).slice(0, 12).join(', ')
      return ok(`没有这一关：${args.id}。可用 id 例如：${ids}…（用 study_catalog 看全量）`)
    }
    const part = String(args.section || '').trim()
    const head = `# ${l.title}（${l.id}）\n${l.trackName} · ${l.stage} · 预计 ${l.min} 分钟`

    if (part === 'intro') {
      return ok([head, '', `## 钩子\n${l.hook}`, '', `## 学完你应该能\n${fmtList(l.goals)}`].join('\n'))
    }
    if (part === 'concepts') {
      return ok([head, '', '## 三个概念', fmtConcepts(l.concepts)].join('\n'))
    }
    if (part === 'steps') {
      return ok([head, '', '## 动手', fmtSteps(l.steps), '', '要求用户把真实输出贴回来再往下。'].join('\n'))
    }
    if (part === 'quiz') {
      return ok([head, '', '## 自测', fmtQuiz(l.quiz)].join('\n'))
    }
    if (part === 'readback') {
      return ok([head, '', fmtReadback(l.id) || '这一关没有回书指引。'].join('\n'))
    }

    return ok([
      head,
      '',
      `## 钩子\n${l.hook}`,
      '',
      `## 学完你应该能\n${fmtList(l.goals)}`,
      '',
      `## 三个概念\n${fmtConcepts(l.concepts)}`,
      '',
      `## 动手\n${fmtSteps(l.steps)}`,
      '',
      `## 自测\n${fmtQuiz(l.quiz)}`,
      '',
      fmtReadback(l.id),
      '',
      `## 收尾\n学完这关你应该能：${l.can}`,
      '',
      '教学节奏：钩子 → 概念 → 动手（等用户贴输出）→ 自测（一次一题）→ 收尾。一次只推进一个环节。',
    ].join('\n'))
  },
}
