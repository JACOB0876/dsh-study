// 所有工具共用的输出契约：execute 返回 { text }，render 把它变成对话内容块。
export const textOutput = {
  schema: {
    type: 'object',
    properties: {
      text: { type: 'string' },
    },
    required: ['text'],
    additionalProperties: false,
  },
  render: (_args, value) => [{ type: 'text', text: String(value?.text ?? '') }],
}

export function ok(text) {
  return { text: String(text) }
}
