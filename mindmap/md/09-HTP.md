# 09 Large Language Models: The Hard Parts

`Souza & Regenstein · 大语言模型的硬骨头 · 341 页 · 9 章`

路径：文本与推理工程 → HTP

```mermaid
mindmap
  root((HTP))
    First Principles ／第一性原理：动手之前要想清楚的事 · p1 · 快读
      First Principles: What to Consider Before We Start Building with LLMs ／第一性原理：动手之前该想清楚的事 · p23
      Why Open Source? ／为什么要用开源 · p24
      Stakeholder Requirements ／干系人需求 · p25
      Operational Requirements ／运维需求 · p26
      Organizational AI Frameworks ／组织级 AI 框架 · p27
      Federated Framework ／联邦式框架 · p28
      The Importance of Data ／数据的重要性 · p29
      Model Types ／模型类型 · p30
      Instruction Fine-Tuned Models ／指令微调模型 · p31
      Domain Adapted Models ／领域适配模型 · p32
      Model Features ／模型特性 · p33
      Caching ／缓存 · p34
      Licensing ／许可 · p36
      Small Language Models ／小语言模型 · p37
    The Evals Gap ／评估的缺口 · p17 · 精读
      The Evals Gap ／评估的缺口 · p39
      Nondeterministic Nature of LLMs ／LLM 的非确定性本质 · p40
      Temperature ／温度 · p41
      10-K LLMBA Temperature Tests ／10-K 报告的温度实验 · p42
      The Evals Challenge ／评估的难点 · p45
      Designing an LLMBA Evaluation Framework ／设计评估框架 · p46
      Conceptual Design: Multiple LLMBAs ／概念设计：多个 LLMBA · p47
      Methodologies for Evaluation ／评估方法论 · p48
      Quantitative Metrics ／量化指标 · p49
      Coding BLEU and ROUGE ／写 BLEU 与 ROUGE · p50
      Coding an LLM-as-a-Judge ／写一个 LLM 裁判 · p58
      Limitations of LLM-as-a-Judge ／LLM 裁判的局限 · p64
      A Brief Tour of LLM Benchmarks ／LLM 基准测试巡览 · p69
      ARC-AGI and the Prize ／ARC-AGI 与它的奖金 · p70
    Evaluation Tools ／评估工具链 · p53 · 选读
      Evaluation Tools for LLM-Based Applications ／面向 LLM 应用的评估工具 · p75
      BLEU with LangSmith ／用 LangSmith 做 BLEU · p76
      Scaling LLM-as-a-Judge with LangSmith ／用 LangSmith 扩展 LLM 裁判 · p85
      Promptfoo ／Promptfoo · p88
      Evaluating Models with Promptfoo ／用 Promptfoo 评测模型 · p89
      Evaluating Prompts ／评测提示词 · p93
      LightEval ／LightEval · p96
      LightEval Setup ／LightEval 环境搭建 · p97
      Econometric Evaluation with MMLU ／用 MMLU 做计量经济学评估 · p100
      Frameworks Comparison ／框架对比 · p103
    From Data to Context ／从数据到上下文 · p83 · 精读
      From Data to Context ／从数据到上下文 · p105
      Preprocessing Documents ／文档预处理 · p107
      MarkItDown ／MarkItDown · p108
      RAG ／RAG · p109
      RAG Process ／RAG 流程 · p110
      Chunking Documents ／文档切块 · p111
      Chunking Case Study ／切块案例研究 · p112
      Vector Embeddings ／向量嵌入 · p130
      Reranking ／重排 · p137
      Report Generation ／报告生成 · p138
      RAG Challenges and Limitations ／RAG 的挑战与局限 · p140
      Long-Context Models: RAG Killer? ／长上下文模型：RAG 的终结者？ · p142
      LCM Case Study: Quiz Generation with Citations ／长上下文案例：带引用的出题 · p144
      Implementation ／实现 · p146
      …另 2 节
    Structured Data Output ／结构化输出 · p133 · 精读
      Structured Data Output ／结构化数据输出 · p155
      Why Structured Output Matters ／为什么结构化输出重要 · p156
      Improving Developer Efficiency and Workflow ／提升开发效率与工作流 · p157
      Training-Time Constraint Techniques ／训练阶段的约束技术 · p159
      Inference-Time Constraint Techniques ／推理阶段的约束技术 · p160
      JSON Mode （Fine-Tuned） ／JSON 模式（微调实现） · p163
      Combining JSON Mode with Pydantic ／JSON 模式结合 Pydantic · p165
      Logit Postprocessing ／logit 后处理 · p166
      Outlines ／Outlines · p171
      Ollama ／Ollama · p176
      Ollama with Pydantic ／Ollama 结合 Pydantic · p178
      LangChain ／LangChain · p179
      Comparing Tools ／工具对比 · p181
    LLM Safety Considerations ／LLM 安全考量 · p161 · 选读
      LLM Safety Considerations ／LLM 安全考量 · p183
      General AI Safety Risks ／通用 AI 安全风险 · p184
      LLM-Specific Safety Risks ／LLM 特有的安全风险 · p185
      Addressing LLMBA Safety Risks ／应对 LLMBA 的安全风险 · p187
      Bias Detection ／偏见检测 · p188
      Privacy Protection ／隐私保护 · p189
      OpenAI ／OpenAI 的规范 · p190
      Anthropic ／Anthropic 的规范 · p191
      Google ／Google 的规范 · p192
      MLCommons AI Safety Benchmark ／MLCommons AI 安全基准 · p193
      Centre for the Governance of AI Rubric ／AI 治理中心的评分表 · p195
      Two Specific Approaches to LLM Safety ／两种具体的 LLM 安全做法 · p196
      Constitutional AI ／宪法式 AI · p198
    Evaluating LLMs for Safety ／安全评估 · p179 · 选读
      Evaluating LLMs for Safety ／安全维度的 LLM 评估 · p201
      Safety Evaluation with Benchmark Datasets ／用基准数据集做安全评估 · p203
      TruthfulQA ／TruthfulQA · p209
      HarmBench ／HarmBench · p217
      Runtime Guardrails and Moderation ／运行时护栏与内容审核 · p222
      NeMo Guardrails ／NeMo Guardrails · p224
      TruLens Guardrails ／TruLens 护栏 · p225
      Llama Guard ／Llama Guard · p227
      Mistral’s Moderation API ／Mistral 的内容审核 API · p230
      OpenAI’s Moderation API ／OpenAI 的内容审核 API · p231
      Custom Moderation with LLM-as-a-Judge ／用 LLM 裁判做自定义审核 · p232
      Case Study: Implementing a Safety Filter for K–12 Students ／案例：给 K–12 学生做安全过滤 · p233
      Safety Filters ／安全过滤器 · p239
      Benchmarking ／基准测试 · p243
    LLM Alignment: A Case Study ／对齐实战：一个完整案例 · p227 · 选读
      LLM Alignment: A Case Study ／LLM 对齐：一个完整案例 · p249
      Why Is Alignment Necessary? ／为什么需要对齐 · p250
      RLHF: The Breakthrough That Made LLMs Trustworthy ／RLHF：让 LLM 值得信任的突破 · p251
      Proximal Policy Optimization ／近端策略优化（PPO） · p253
      DPO ／直接偏好优化（DPO） · p254
      Case Study: Aligning an LLM to a Policy ／案例：让模型符合一份政策 · p256
      Acme’s Educational Policy ／Acme 的教育政策 · p257
      Preference Dataset—Synthetic Dataset Generation ／偏好数据集——合成数据生成 · p260
      Fine-Tuning ／微调 · p274
      Alignment Evaluation: LLM-as-a-Judge ／对齐评估：用 LLM 当裁判 · p281
      DPO Dataset Composition ／DPO 数据集构成 · p289
      Our Choice of Base Model ／基座模型的选择 · p290
      The Evaluation Methodology ／评估方法 · p291
      Phase 1: Policy Definition ／第 1 阶段：定义政策 · p292
      …另 5 节
    Epilogue ／尾声：成本下降时代的 LLM 应用 · p279 · 快读
      Epilogue: LLMBAs in the Era of Falling Costs ／尾声：成本下降时代的 LLM 应用 · p301
      Appendix. Tools for Local LLM Deployment … ／附录：本地 LLM 部署工具 · p305
```