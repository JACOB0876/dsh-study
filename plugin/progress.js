// 学习进度：存在 ~/.dsh/study-progress.json，每个用户一份。
import { readFileSync, writeFileSync, mkdirSync, renameSync, existsSync } from 'node:fs'
import { homedir } from 'node:os'
import { join, dirname } from 'node:path'

const FILE = () => {
  const home = process.env.DSH_HOME || join(homedir(), '.dsh')
  return join(home, 'study-progress.json')
}

const EMPTY = () => ({ version: 1, updated: null, tracks: {}, notes: {} })

export function load() {
  try {
    const p = FILE()
    if (!existsSync(p)) return EMPTY()
    const d = JSON.parse(readFileSync(p, 'utf8'))
    return { ...EMPTY(), ...d, tracks: d.tracks || {}, notes: d.notes || {} }
  } catch {
    return EMPTY()
  }
}

export function save(state) {
  const p = FILE()
  try {
    mkdirSync(dirname(p), { recursive: true })
    const tmp = p + '.tmp'
    state.updated = new Date().toISOString()
    writeFileSync(tmp, JSON.stringify(state, null, 1), 'utf8')
    renameSync(tmp, p)
    return { ok: true, path: p }
  } catch (e) {
    return { ok: false, path: p, error: String(e && e.message || e) }
  }
}

export function trackState(state, trackId) {
  if (!state.tracks[trackId]) state.tracks[trackId] = { done: [], current: null }
  return state.tracks[trackId]
}

export function mark(state, trackId, lessonId) {
  const t = trackState(state, trackId)
  if (!t.done.includes(lessonId)) t.done.push(lessonId)
  t.current = lessonId
  return t
}

export function unmark(state, trackId, lessonId) {
  const t = trackState(state, trackId)
  t.done = t.done.filter(x => x !== lessonId)
  if (t.current === lessonId) t.current = t.done[t.done.length - 1] || null
  return t
}

export function isDone(state, trackId, lessonId) {
  return (state.tracks?.[trackId]?.done || []).includes(lessonId)
}

export function storePath() {
  return FILE()
}
