import { content, trackList, orderedLessons, nextLessonFor, recommendNext } from '../content.js'
import { load } from '../progress.js'
import { textOutput, ok } from './common.js'

export const catalogTool = {
  name: 'study_catalog',
  description:
    '列出学习插件的所有路线与当前进度，或某条路线下的关卡清单（已完成的打勾）。先用它让用户选路线，再逐关教学。',
  parameters: {
    type: 'object',
    properties: {
      track: { type: 'string', description: '路线 id：llm / quant / nlp / cpp / eng。省略时返回全部路线概览。' },
    },
    required: [],
    additionalProperties: false,
  },
  output: textOutput,
  execute: async (args) => {
    const tracks = trackList()
    const state = load()

    if (!args.track) {
      const lines = tracks.map(t => {
        const ls = orderedLessons(t.id)
        const done = (state.tracks?.[t.id]?.done || []).filter(id => ls.some(l => l.id === id)).length
        const next = recommendNext(ls, state.tracks?.[t.id]?.done || []).lesson
        const prog = done ? `已学 ${done}/${ls.length}，下一关 ${next ? next.id : '（完成）'}` : '还没开始'
        return `- ${t.name}（${t.id}）：${ls.length} 关，约 ${Math.round(t.minutes / 60 * 10) / 10} 小时 · ${prog} —— ${t.sub}`
      })
      const doneTips = []
      for (const t of content().tracks) {
        const ls = orderedLessons(t.id)
        const doneIds = state.tracks?.[t.id]?.done || []
        const finished = doneIds.filter(id => ls.some(l => l.id === id)).length >= ls.length
        if (finished && t.next) {
          const nx = content().tracks.find(x => x.id === t.next.id)
          doneTips.push(`## ✅ ${t.name} 已全部学完`, `建议下一步：**${nx ? nx.name : t.next.id}**（${t.next.id}）—— ${t.next.why}`, `用 study_catalog track=${t.next.id} 查看关卡。`, '')
        }
      }
      const started = tracks.some(t => (state.tracks?.[t.id]?.done || []).length)
      return ok([
        `# ${content().books.length} 本书 · 学习路线（内容版本 ${content().version}）`,
        '',
        ...lines,
        '',
        ...doneTips,
        started
          ? '用户有进度：先问「继续上次那关，还是换一条线」。'
          : '问用户想从哪条线开始；没有偏好就建议 llm（不需要显卡，前 4 关只调 API）。',
        '选定后用 study_lesson 取关卡。',
        '',
        '## 教学规则（必须遵守）',
        '1. 一次回复只推进一个环节：钩子 → 概念 → 动手 → 对照 → 自测（一题）→ 收尾。',
        '2. 用户没贴真实输出，不许说「你应该看到 X」。',
        '3. 自测连错两次，退回上一关的概念，不许硬推。',
        '4. 收尾必须调 study_progress mark，并给出回书章节 + 页码 + 目的。',
      ].join('\n'))
    }

    const t = content().tracks.find(x => x.id === args.track)
    if (!t) {
      return ok(`没有这条路线：${args.track}。可选：${tracks.map(x => x.id).join(' / ')}`)
    }

    const doneSet = new Set(state.tracks?.[t.id]?.done || [])
    const rows = []
    let n = 0
    for (const st of t.stages) {
      rows.push(`## ${st.name}${st.hint ? '（' + st.hint + '）' : ''}`)
      for (const l of st.lessons) {
        n += 1
        rows.push(`${doneSet.has(l.id) ? '✅' : '☐'} ${n}. [${l.id}] ${l.title} · ${l.min} 分钟`)
      }
    }
    const total = t.stages.reduce((k, s) => k + s.lessons.length, 0)
    return ok([
      `# ${t.name} · ${t.sub}`,
      '',
      t.intro?.why ? `一句话：${t.intro.why}` : '',
      `进度：${[...doneSet].filter(id => t.stages.some(s => s.lessons.some(l => l.id === id))).length} / ${total}`,
      '',
      ...rows,
      '',
      '开始某一关用 study_lesson，参数 id 用方括号里的值；学完用 study_progress mark。',
    ].filter(x => x !== '').join('\n'))
  },
}
