# Hands-On LLM Serving and Optimization: Hosting LLMs at Scale（LLM 服务与优化实战）

> 从一次前向讲到多机多卡：把 LLM 推理的瓶颈、优化手段与四大框架串成一条工程路径。

## 基本信息

- 作者：Chi Wang、Peiheng Hu｜第 1 版（2026-05）｜372 页｜O'Reilly
- 难度：★★★★☆ —— 不推公式，但要同时掌握 Transformer、显存/带宽、调度与分布式，实验需真 GPU。
- 目标读者：平台与基础设施工程师、ML 工程师、技术负责人，及从"调 API"转向"自建推理"的团队。
- 建议投入：约 50 小时（概念 25 小时，第 9 章实验与环境 20–25 小时，不含等卡）。

## 章节结构

| 章 | 英文标题 | PDF 起始页 | 内容要点（一句） | 精读建议 |
| --- | --- | --- | --- | --- |
| 1 | Introduction to Model Serving and Optimization | 19 | 模型生命周期、serving 定义、三种部署形态与 vLLM 初体验 | 精读 |
| 2 | Large Language Model Serving | 49 | 自回归 Transformer、KV cache、prefill/decode、vLLM 对比 HF、流式与批 | 精读 |
| 3 | Model Serving System Design: A Deep Dive | 83 | 从零实现单模型服务（请求、批处理、流式），再扩多模型与 Triton | 选读 |
| 4 | Model Serving Best Practices | 125 | Agent/RAG/CAG、企业分层架构、六种云上方案、性能指标 | 选读 |
| 5 | Challenges When Serving LLMs | 175 | GPU 规格、模型与 KV cache 显存估算、两阶段瓶颈 | 精读 |
| 6 | Essential LLM Optimization Techniques | 207 | 连续批处理/chunked prefill、FlashAttention、量化、PagedAttention、前缀缓存 | 精读 |
| 7 | Advanced LLM Optimization Techniques | 251 | 投机解码、张量/流水线/专家并行、PD 分离、LMCache | 精读 |
| 8 | LLM Serving Frameworks | 289 | vLLM 架构与调度器、TensorRT-LLM、SGLang、llama.cpp 选型 | 精读 |
| 9 | LLM Optimization in Practice | 311 | Qwen3-14B + vLLM 八步优化：造流量、定指标、量化、分布式 | 精读 |
| 10 | Advancements in LLM Serving | 333 | 语义缓存、性能剖析、多模态、边缘、Multi-LoRA、RL serving | 快读 |

取舍理由：5–9 章（瓶颈→优化→框架→实战）不可替代，必须精读；3、4 章的生产内容可用现成方案替代，10 章是方向性展望。

## 核心概念（15 条）

- **Model serving** — 把模型部署成可调用服务；第 1 章分端侧、单模型、多模型。
- **Prefill / Decode** — 前者并行处理 prompt（算力密集），后者逐 token 生成（带宽受限）；第 2、5 章。
- **KV cache** — 缓存历史 K/V 免重算；第 2 章引入，第 5 章教估算显存。
- **TTFT / ITL (TPOT)** — 首 token 与 token 间延迟；第 4 章定义、第 9 章实测。
- **Continuous batching** — 每步动态换入换出请求；第 6 章，PDF p.210。
- **Chunked prefill** — 长 prompt 切块与 decode 混批，压 ITL 抖动；第 6 章，PDF p.213。
- **PagedAttention** — 像 OS 分页一样管理 KV cache 块；第 6 章，PDF p.222。
- **Kernel fusion / FlashAttention** — 减少 HBM 往返的融合注意力算子；第 6 章，PDF p.220。
- **Quantization** — FP16 降到 FP8/INT8/INT4，权重量化最实用；第 6 章，PDF p.224。
- **Prefix caching / RadixAttention** — 复用相同前缀的 KV；第 6 章，RadixAttention 见第 8 章。
- **Speculative decoding** — 小模型起草、大模型并行验证，降 ITL；第 7 章，PDF p.251。
- **Tensor / pipeline / expert parallelism** — 模型切分与 MoE 并行；第 7 章，PDF p.263–268。
- **Prefill-decode disaggregation** — 两阶段拆到不同实例分别扩缩容；第 7 章，PDF p.269。
- **vLLM / TensorRT-LLM / SGLang / llama.cpp** — 第 8 章四大框架：vLLM 架构与调度器（PDF p.291 起）、TensorRT-LLM（p.303）、SGLang 的 RadixAttention（p.304）、llama.cpp/GGUF（p.305）。
- **Semantic caching / Multi-LoRA** — 按语义命中缓存、单基座挂多适配器；第 10 章。

## 代码与数据

- 依赖：PyTorch、Transformers、vLLM（`vllm==0.8.5.post1`）、FlashInfer（`flashinfer-python==0.2.2`）、NVIDIA Triton Inference Server、SGLang、TensorRT-LLM、llama.cpp（GGUF）、LMCache；模型为 Qwen 系列（第 9 章 Qwen3-14B）。
- 代码：`https://github.com/orca3/llm-model-serving`（正文给出），含第 4 章 KnowledgeAgent。
- 数据：无公开数据集，第 9 章基准流量由脚本生成；需至少一块 GPU，分布式实验需多卡。

## 怎么读这本书

- 推荐路径：1 → 2 → 5 → 6 → 7 → 8 → 9；自研服务把 3 插在 2 后，企业选型或 Agent 平台把 4 插在 5 前，10 最后扫。
- 可跳过：第 3 章手写服务、第 4 章云上选项逐条操作、第 10 章前瞻，不影响主干。
- 常见坑：① vLLM 0.8.5.post1 与 FlashInfer 0.2.2 绑定，注意力后端环境变量跨版本会改名；② FlashAttention3 主要面向 Hopper，A100 走 FlashInfer，单卡 24GB 跑 14B 必须量化；③ Triton（GPU 编译器）≠ NVIDIA Triton Inference Server（模型服务器），正文专门提醒；④ GPU 规格与云价格按 2026 年春写，半年即过期；⑤ 分布式实验要 NVLink 多卡。

## 与其他书的关系

- **Python Data Science Handbook / Machine Learning with Python Cookbook 2e**：基础前置，本书不教 Python、NumPy、sklearn。
- **Blueprints for Text Analytics**：上游应用侧；那本用 BERT 做情感分类，本书接"怎么高效托管"。
- **Deep Learning for Finance**：补 Transformer 与训练细节；本书只讲推理，默认你懂 attention。
- **Reinforcement Learning for Finance**：第 10 章 RL serving（rollout 吞吐、确定性）与 RL 训练循环衔接。
- **Financial Theory with Python / Learning Modern C++ for Finance**：几乎无重叠；后者仅当读 llama.cpp 源码时相邻。

## 自测（4 题）

- 第 2/5 章：70B FP16、batch=8、4k 上下文，权重与 KV cache 各占多少 GB？为何 decode 是带宽瓶颈？
- 第 6 章：连续批处理与 chunked prefill 各解决什么？为何后者拉长 TTFT 却提升吞吐？
- 第 7 章：张量并行与流水线并行的通信模式、适用规模有何不同？PD 分离为何能降 TPOT 抖动？
- 第 8/9 章：短请求延迟敏感与离线吞吐优先两种负载，四个框架怎么选？给出两条依据。
