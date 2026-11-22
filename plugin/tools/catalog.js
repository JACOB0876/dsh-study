import { content, trackList } from '../content.js'
import { textOutput, ok } from './common.js'

export const catalogTool = {
  name: 'study_catalog',
  description:
    '列出学习插件的所有路线，或某条路线下的关卡清单。先用它让用户选路线，再逐关教学。',
  parameters: {
    track: {
      type: 'string',
      description: '路线 id：llm / quant / nlp / cpp。省略时返回全部路线概览。',
    },
  },
  output: textOutput,
  execute: async (args) => {
    const tracks = trackList()

    if (!args.track) {
      const lines = tracks.map(
        t => `- ${t.name}（${t.id}）：${t.count} 关，约 ${Math.round(t.minutes / 60 * 10) / 10} 小时 —— ${t.sub}`,
      )
      return ok([
        `# 8 本书 · 学习路线（内容版本 ${content().version}）`,
        '',
        ...lines,
        '',
        '问用户想从哪条线开始；没有偏好就建议 llm（不需要显卡，前 4 关只调 API）。',
        '选定后用 study_lesson 取第一关。',
      ].join('\n'))
    }

    const t = content().tracks.find(x => x.id === args.track)
    if (!t) {
      return ok(`没有这条路线：${args.track}。可选：${tracks.map(x => x.id).join(' / ')}`)
    }

    const rows = []
    let n = 0
    for (const st of t.stages) {
      rows.push(`## ${st.name}${st.hint ? '（' + st.hint + '）' : ''}`)
      for (const l of st.lessons) {
        n += 1
        rows.push(`${n}. [${l.id}] ${l.title} · ${l.min} 分钟`)
      }
    }
    return ok([
      `# ${t.name} · ${t.sub}`,
      '',
      t.intro?.why ? `一句话：${t.intro.why}` : '',
      '',
      ...rows,
      '',
      '开始某一关时调用 study_lesson，参数 id 用方括号里的值。',
    ].filter(x => x !== '').join('\n'))
  },
}
