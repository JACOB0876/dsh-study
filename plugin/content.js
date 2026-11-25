// 读取打包好的 content.json，做一层索引。
import { readFileSync } from 'node:fs'

let cache = null

export function content() {
  if (cache) return cache
  const url = new URL('./content/content.json', import.meta.url)
  cache = JSON.parse(readFileSync(url, 'utf8'))
  return cache
}

export function trackList() {
  return content().tracks.map(t => ({
    id: t.id,
    name: t.name,
    sub: t.sub,
    count: t.stages.reduce((n, s) => n + s.lessons.length, 0),
    minutes: t.stages.reduce((n, s) => n + s.lessons.reduce((m, l) => m + l.min, 0), 0),
  }))
}

export function orderedLessons(trackId) {
  const t = content().tracks.find(x => x.id === trackId)
  if (!t) return []
  return t.stages.flatMap(s => s.lessons.map(l => ({ ...l, stage: s.name, track: trackId })))
}

export function lesson(id) {
  const l = content().lessons[id]
  if (!l) return null
  const track = content().tracks.find(t => t.stages.some(s => s.lessons.some(x => x.id === id)))
  const stage = track?.stages.find(s => s.lessons.some(x => x.id === id))
  return { ...l, track: track?.id, trackName: track?.name, stage: stage?.name }
}

export function nextLesson(trackId, afterId) {
  const ls = orderedLessons(trackId)
  if (!afterId) return ls[0] || null
  const i = ls.findIndex(l => l.id === afterId)
  return i >= 0 ? ls[i + 1] || null : null
}

export function findLessonByTitle(text) {
  const q = String(text || '').toLowerCase()
  const all = Object.values(content().lessons)
  return all.find(l => l.id.toLowerCase() === q)
    || all.find(l => l.title.toLowerCase().includes(q))
    || null
}

// 下一关：以「最后完成的那一关」为锚点往后找，避免总把人送回第一关
export function nextLessonFor(list, doneIds) {
  const done = new Set(doneIds || [])
  let last = -1
  list.forEach((l, i) => { if (done.has(l.id)) last = i })
  return list.slice(last + 1).find(l => !done.has(l.id)) || list.find(l => !done.has(l.id)) || null
}

// 下一关推荐：优先补「前面的缺口」（比如后来新增的基础关），否则取最后一关之后的第一关
export function recommendNext(list, doneIds) {
  const done = new Set(doneIds || [])
  let last = -1
  list.forEach((l, i) => { if (done.has(l.id)) last = i })
  for (let i = 0; i < last; i += 1) {
    if (!done.has(list[i].id)) {
      return { lesson: list[i], gap: true, learned: last + 1 }
    }
  }
  const after = list.slice(last + 1).find(l => !done.has(l.id)) || list.find(l => !done.has(l.id)) || null
  return { lesson: after, gap: false, learned: last + 1 }
}
