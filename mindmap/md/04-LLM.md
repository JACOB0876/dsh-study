# 04 Hands-On LLM Serving and Optimization

`Wang & Hu · 2026 · LLM 服务与优化实战 · 372 页 · 10 章`

路径：文本与推理工程 → LLM

```mermaid
mindmap
  root((LLM))
    Introduction to Model Serving ／模型服务入门 · p19 · 精读
      Anatomy of a Model ／模型的构成 · p20
        · 入门服务需先懂模型训练，且缺系统学习路径
        · 无论何种角色，AI 从业者都应懂模型服务
      Model Architecture ／模型架构 · p22
        · 架构文件是训练代码中模型类的拷贝
        · 模型类定义各层结构与 forward 计算
      Model Data ／模型数据 · p22
        · 模型数据是网络权重，与架构分文件保存
        · 分开存便于灵活替换与跨版本迭代
      Model Execution Code ／模型执行代码 · p22
        · 执行代码是模型包里的 Python 类与 forward
        · 服务时需同时加载架构代码与权重数据
      Model Lifecycle: From Training to Serving ／模型生命周期：从训练到服务 · p23
        · 架构与权重分存，改版后可部分加载（partial loading）
        · 架构微调会产生不匹配键（nonmatching keys）
      What Is Model Serving? ／什么是模型服务 · p24
        · 服务三步：部署（deployment）→服务（serving）→优化迭代
        · 模型成为软件制品，须版本化、测试与集成
        · 推理（inference）经 API 处理实时或批量请求
      Why Study Model Serving? ／为何研究模型服务 · p26
        · 成本（cost-to-serve）是评估服务方案的决定性因素
        · 服务更靠系统工程与全栈优化，而非新算法
        · 服务目标：满足 SLA 并交付业务价值
      Why Optimize Model Serving （Especially for LLMs）? ／为何优化模型服务（尤其是 LLM） · p29
        · 外包可作起点，自建则在成本、安全、灵活性上占优
        · 无万能方案，选型看项目规模与运维能力
      （vLLM） to Improve LLM Throughput ／（vLLM）提升 LLM 吞吐 · p30
        · 服务优化三目标：降延迟、提吞吐、提资源利用率
        · vLLM 开 FP8 MLA 内核并加大 batch，吞吐 38→600 TPS
        · 单次 LLM 请求成本可达传统查询 10 倍
      Model Serving Paradigms ／模型服务范式 · p33
        · 按部署形态分端侧、单模型、多模型与平台范式
        · 范式选择取决于模型数、流量与硬件独占程度
      On-Device （Edge） Serving ／端侧（边缘）服务 · p33
        · 端侧受算力、存储与功耗限制，难跑大模型
        · 端侧可用小模型（Gemma 3 270M），必要时转云端
      Single-Model Service ／单模型服务 · p37
        · 单模型服务：一个模型一个实例，隔离简单
        · 模型多时实例爆炸（100×10=1000），运维不可扩展
      Multi-Model Service ／多模型服务 · p42
        · 多模型共享资源池、按需加载，提高利用率
        · 需权衡卸载换入的加载开销与冷启动
      Model Serving Platforms ／模型服务平台 · p46
        · 超大模型难共享：换入换出带来加载开销与冷启动
        · 高流量低延迟模型需常驻，不宜放进共享池
    Large Language Model Serving ／大语言模型服务 · p49 · 精读
      Inside the Mind of a Transformer ／Transformer 内部机制 · p50
        · 看清 Transformer 内部，才能推断其瓶颈与优化点
        · 理解行为与限制，是后续批处理与缓存优化的前提
      LLM Evolution ／LLM 演进 · p50
        · 本章打基础：先建直觉，再谈系统设计与调优
        · 生产中流式（streaming）与批处理（batching）必备
      The Autoregressive Nature of Transformers ／Transformer 的自回归特性 · p53
        · token 由分词器（tokenizer）切分，可为词、子词或标点
        · 英文平均 1 token ≈ 0.75 个词
      Decoder-Only Transformer Architecture ／纯解码器 Transformer 架构 · p55
        · 自回归逐 token 生成，遇最大长度或停止词（stop token）止
        · 主流 LLM 采用纯解码器（decoder-only）架构
      Capture Token Context by Calculating Attention ／用注意力捕捉词元上下文 · p61
        · 注意力（attention）依上下文消解指代歧义
        · 解码层含 Q/K/V 投影、MLP 与 RMSNorm
        · 注意力密集层宜用融合内核（fused attention kernel）
      Executing LLM Generation: A Step-by-Step Walkthrough ／LLM 生成执行全流程 · p64
        · 本书刻意简化张量形状细节，聚焦服务与优化
        · 一次生成＝嵌入→注意力→MLP→输出，逐 token 循环
      Model Prediction, Line by Line ／逐行解读模型预测 · p65
        · 单请求单序列示例仅作演示，生产需批流与优化
        · 沿时间看执行：逐 token、prefill/decode、缓存状态
      Enable the KV Cache to Boost Performance ／启用 KV cache 提升性能 · p69
        · 无缓存时每生成一个 token 都要重算整段序列
        · KV cache 存各层历史 key/value，只算新增 token
      The Prefill and Decode Phases ／预填充与解码阶段 · p72
        · 预填充（prefill）处理整段提示并建立 KV cache
        · 解码（decode）每步仅算新 token，速度更稳定
      Run the LLM with a Serving Framework ／用服务框架运行 LLM · p75
        · 生产应用依赖服务框架，而非自建推理管线
        · 框架以 REST 或 gRPC API 提供实时、批量推理
      Serve the LLM （Qwen） with vLLM ／用 vLLM 服务 Qwen 模型 · p75
        · vLLM 加载预训练模型并直接对外提供 API
        · 训练框架重开发，服务框架重高效低延迟推理
      Performance Comparison: vLLM Versus Hugging Face Transformers ／性能对比：vLLM 与 Transformers · p77
        · vLLM 吞吐可达 Hugging Face Transformers 的 10–20 倍
        · vLLM 沿用 OpenAI 文本补全 API 的参数约定
      LLM Streaming Serving Basics ／LLM 流式服务基础 · p78
        · 同步 generate 要等整段输出，首字延迟长
        · 流式（streaming）逐 token 返回，改善聊天体验
      LLM Batch Serving Basics ／LLM 批处理服务基础 · p79
        · AsyncLLMEngine 返回异步流，async for 逐个取 token
        · 批处理合并多请求推理，以提高吞吐
    Model Serving System Design ／模型服务系统设计 · p83 · 选读
      Build an Online LLM Serving Service from Scratch ／从零构建在线 LLM 服务 · p84
        · 手写简化服务，才能看清框架抽象掉了什么
        · 自建部分涵盖 API、批处理、流式与并发处理
      Design Goals ／设计目标 · p84
        · 目标：能评估、改造并扩展开源或云服务方案
        · 示例代码已简化，完整实现见 GitHub 仓库
      Service Architecture ／服务架构 · p85
        · 架构要让批处理（batching）与流式（streaming）共存
        · 重点关注请求处理流程与性能瓶颈的位置
      Implement Single Generation Request Handling ／实现单次生成请求处理 · p87
        · 模型跑在绑定 GPU 的独立进程，Web 服务留在 CPU
        · GPU 昂贵，须避免空等 CPU 做分词与前后处理
      Batching ／批处理 · p90
        · 单请求串行处理，吞吐很低
        · 批处理把并发请求合并成一批送 GPU
      Streaming with Batching ／流式与批处理结合 · p95
        · 连续批处理（continuous batching）让新请求加入解码批次
        · 动态调度需同时守住 GPU 利用率与延迟
      Batch Serving with vLLM ／用 vLLM 做批处理服务 · p101
        · 生产级涉及线程管理、事件队列与进程间通信
        · 先手写批处理懂机制，再看 vLLM 怎么做
      A General Design for Single-Model LLM Serving ／单模型 LLM 服务通用设计 · p103
        · 单模型服务分层：API 层与模型后端解耦
        · 模型执行隔离在后端，业务逻辑与推理分离
      Requirements for Single-Model Serving ／单模型服务需求 · p103
        · 框架可作库嵌入，也可作独立 Web 服务器
        · 嵌入式集成紧、控制强；独立式便于外部调用
      General Design ／总体设计 · p105
        · LLM 服务需求随架构演进持续变化，需模型感知
        · 输入长度与注意力类型影响 KV cache 行为
      Build a Multi-Model Serving Service from Scratch ／从零构建多模型服务 · p108
        · 单模型方案仅适合流量可预测、独占硬件的场景
        · 应用增长后必须同时托管多个模型
      Design Goals ／设计目标 · p109
        · 示例托管 3 个模型（2 语言 + 1 图像），全跑 CPU
        · 设计目标：跨框架支持 + 统一 API 接口
      Service Architecture ／服务架构 · p109
        · 文本与视觉模型共用一套 REST 接口
        · 同时支持 PyTorch 与 ONNX 等异构框架
      Core Implementation ／核心实现 · p111
        · 模型缓存满时按 LRU（least recently used）淘汰
        · 流程：注册元数据→建 worker 加载→推理→返回
      …另 5 节
    Model Serving Best Practices ／模型服务最佳实践 · p125 · 选读
      Model Serving in an Agentic World ／Agent 时代的模型服务 · p126
        · 企业级服务不止推理：编排、治理、可观测与成本控制
        · 自建与上云是连续谱（spectrum），不是二选一
      Defining Agents ／定义 Agent · p127
        · 一次交互触发多次 LLM 调用，token 与链路延迟放大
        · 多 Agent 分层增强自主性，却增加服务设计挑战
      A Sample Knowledge Agent ／一个知识 Agent 示例 · p128
        · Agent 与传统助手的根本区别是自主性（autonomy）
        · 能力：理解指令、规划、调用工具、依反馈调整
      The Agent’s Design ／Agent 的设计 · p129
        · 知识 Agent 组件：编排器、RAG、规划器、动作执行器
        · 以本地 PDF 文件集为知识源做检索问答
      The Agent’s Internal Workflow ／Agent 的内部工作流 · p130
        · 流程：规划→执行动作→检索→LLM 总结
        · RAG 子系统充当语义搜索（semantic search）
      Agent Autonomy ／Agent 自主性 · p132
        · 动作按规划顺序执行，首个常是带上下文的 RAG 查询
        · RAG 先检索相关文档，再由 LLM 归纳
      Retrieval-Augmented Generation （RAG） ／检索增强生成（RAG） · p134
        · MCP 解耦工具定义与 Agent 逻辑，调用更可靠
        · 规划交给 LLM，而非写死规则
      Cache-Augmented Generation （CAG） ／缓存增强生成（CAG） · p137
        · 生产级 RAG 需分块、排序、去重与多源检索
        · 上下文窗口（context window）受限，故须分块（chunking）
      LLM Serving in Enterprise Systems: An Overview ／企业系统中的 LLM 服务概览 · p140
        · 工具调用（tool calling）四步：推理→JSON→执行→回传迭代
        · 模型与工具统一经 HTTP/gRPC 服务按需调用
      Public API Layer ／公共 API 层 · p141
        · 公共 API 层管网络、鉴权、计费、限流与路由
        · 要撑百万级并发连接与全球低延迟（geo-routing）
      Resource Management Layer ／资源管理层 · p142
        · 资源层管 CPU/GPU/内存/网络，并做成本分摊
        · 挑战：容量规划、异构 GPU 利用率、客户优先级
      Model Selection and Orchestration Layer ／模型选择与编排层 · p142
        · 延迟敏感请求路由到小模型或投机解码（speculative decoding）
        · 编排层决定用哪个模型、开哪套优化
      Distributed Serving Layer ／分布式服务层 · p143
        · 分布式层＝大模型分布式托管＋分布式缓存
        · 缓存含 KV cache、提示缓存（prompt caching）、语义缓存
        · 多 GPU/多节点须高效共享请求上下文
      Core Inference Layer ／核心推理层 · p143
        · 推理层执行前向计算，直接决定延迟与 GPU 利用
        · 由 GPU worker 执行前向，调度器决定批次
      …另 21 节
    Challenges When Serving LLMs ／LLM 服务的挑战 · p175 · 精读
      Why Optimizing LLM Serving is Important ／优化 LLM 服务为何重要 · p176
        · 优化服务关乎应用与商业成败，先要懂硬件约束
        · 本章桥接基础概念与后续优化技术
      Customer Experience ／客户体验 · p177
        · 首 token 等 20 秒会劝退用户，优化到 1 秒即质变
        · 同硬件下优化延迟可保持吞吐不变
        · 延迟收益有上限，0.1 秒再压缩意义不大
      Cost Efficiency ／成本效率 · p178
        · 推理（inference）是 AI 总成本中最贵的一环
        · 同硬件跑 70B 比 8B 质量更高，但成本也更高
      Scalability, Peak Load Handling, and Feasibility ／可扩展性、峰值负载与可行性 · p180
        · 优化后同硬件同延迟可服务更多客户，省扩容费
        · 优化后可换低端芯片，延迟吞吐相近更便宜
        · GPU 需求随客户增长，优化直接压 GPU 成本
      The Role of Accelerator Chips in LLM Serving ／加速芯片在 LLM 服务中的作用 · p180
        · 加速器的显存细节、算力与互连共同决定服务能力
        · GPU 是 LLM 服务的核心加速芯片
      Reading GPU specs ／读懂 GPU 规格 · p181
        · 读 GPU 规格只看四项：算力、显存、带宽、互连
        · 规格繁杂，只关注与 LLM 相关的属性
      Comparing the Specs of Popular GPUs ／主流 GPU 规格对比 · p188
        · 选卡要同时比较规格与成本（Table 5-4）
        · 更强 GPU 通常更贵，须按场景取舍
      Bottlenecks in LLM Model Loading ／LLM 模型加载瓶颈 · p189
        · 模型加载受显存容量限制，大模型须多卡切分
        · DeepSeek-R1 671B 需 8×H200、FP8 精度运行
      The Model Loading Process ／模型加载流程 · p189
        · 权重从磁盘或内存搬入显存，传输速度决定可行性
        · 带宽对比：SSD 0.5–14、CPU 内存 50–200、显存 300 GB/s–3 TB/s
      Estimating Model Size ／估算模型大小 · p190
        · 模型大小 ≈ 参数量 × 每参数字节数
        · 显存只够放模型还不够，要为 KV cache 留空间
      Estimating KV Cache Size ／估算 KV cache 大小 · p193
        · 显存刚够装模型不理想，KV cache 还要额外占
        · KV cache 随批量与序列长度线性增长
      Boundaries of GPU Compute and Memory Bandwidth ／GPU 算力与显存带宽边界 · p196
        · 瓶颈分两界：显存带宽受限与算力受限
        · 算术强度＝运算量除以访问字节数
      Arithmetic Intensity in Matrix Multiplications ／矩阵乘法的算术强度 · p199
        · 矩阵越大算术强度越高：512 时 170、4096 时 1365 FLOPS/B
        · L40S 拐点为 419 FLOPS/B，低于即受带宽限制
      the LLM Prefill and Decode Phases ／LLM 预填充与解码阶段 · p201
        · prefill 的 M＝序列长度，decode 的 M＝1
        · 长序列 prefill 计算受限，decode 恒受显存带宽限制
        · decode 的算术强度仅 0.5 FLOPS/B
      …另 1 节
    Essential Optimization Techniques ／基础优化技术 · p207 · 精读
      Why Do We Need Batching in Real-Time Serving? ／实时服务为何需要批处理 · p208
        · 批处理提高吞吐，代价是单请求响应变慢
        · prefill 可并行、算术强度高，属计算受限
        · decode 逐 token 自回归，算术强度低
      Dynamic Batching in Online Inference ／在线推理中的动态批处理 · p209
        · 客户端批处理：攒够预设批量再一起发
        · 服务端静态批处理：凑满批量才处理，白等
      Continuous Batching for LLM Online Inference ／LLM 在线推理的连续批处理 · p210
        · 批处理像渡船：满船省成本，等客伤体验
        · 无批处理＝一人一船，体验好但极不经济
        · 静态批处理等满员才开船，慢客被拖累
      Continuous Batching with Chunked Prefill ／连续批处理与分块预填充 · p213
        · 调度双约束：最大批量（max batch size）与最大 token 数
        · 长请求吃满 token 上限后，新请求被拒绝入批
      Scaling Attention and Kernel Optimization ／注意力扩展与内核优化 · p217
        · Transformer 块两大件：注意力与 FFN（MLP）
        · 扩展注意力两条路：缩小 KV cache 与自写 GPU 内核
      Scalable Attention Mechanisms ／可扩展注意力机制 · p217
        · 多头注意力（MHA）已非唯一高效的 Q/K/V 用法
        · 生产负载催生 GQA、MLA 等注意力变体
      Kernel Fusion and Custom Attention Kernels ／内核融合与自定义注意力内核 · p219
        · MLA 不只减 KV 数量，而是压缩其表示
        · DeepSeek 称 MLA 的 KV≈GQA 2.25 组，效果强于 MHA
        · 自写 GPU 内核可优化注意力计算与访存
      Model Compression ／模型压缩 · p224
        · 压缩不是取巧，而是保性能的成熟生产策略
        · 三大压缩类别：量化、蒸馏、剪枝
      Quantization ／量化 · p224
        · 量化（quantization）把参数从高比特降到低比特
        · 低比特让更多参数挤进显存，并提升速度
      Distillation ／蒸馏 · p240
        · 蒸馏（distillation）换掉模型本身，而非压缩原模型
        · 作者认为蒸馏对延迟与吞吐提升潜力最大
      Pruning ／剪枝 · p241
        · 蒸馏 70B 略降：MATH-500 97.3→94.5、GPQA 71.5→65.2
        · 优先试现成蒸馏模型，成本低、见效快
        · 2:4 结构化稀疏可让矩阵乘提速 2 倍
      Prefix Caching ／前缀缓存 · p242
        · 前缀缓存（prefix caching）匹配提示前缀而非整段
        · 请求级哈希命中率低，因同一问题问法多变
        · 存储比计算便宜，命中即省一次重算
      RadixAttention ／RadixAttention · p243
        · RadixAttention 用基数树（radix tree）组织共享前缀
        · 前缀只支持精确匹配，差一个词就回退重算
      Use Cases ／应用场景 · p244
        · 第二个问句可复用第一个的前缀 KV cache
        · 缺共同前缀（少个 Hi）就得整段重算
        · 多轮聊天开头固定，复用收益随上下文增长
      …另 2 节
    Advanced Optimization Techniques ／高级优化技术 · p251 · 精读
      Detailed Steps ／详细步骤 · p252
        · 投机解码（speculative decoding）：草稿模型猜 token，目标模型验证
        · 验证通过即接受并跳跃前进，加速 decode 阶段
      Tuning and Usage ／调优与使用 · p253
        · 被拒 token 之后全部作废，由目标模型重新生成
        · 投机解码不损精度，输出与原始解码一致
        · 理论依据：Leviathan 2022、Chen 2023 两篇论文
      Hands-on Speculative Decoding ／投机解码实战 · p258
        · vLLM 可配三种模式：基线、n-gram、EAGLE-3
        · n-gram 投机配置：候选 6 个 token、lookup 4–6
        · 改进版 n-gram 目标是提高接受率（acceptance rate）并降开销
      Multi-GPU and Multi-Node Inferencing ／多 GPU 与多节点推理 · p260
        · EAGLE-3 的 ITL 更优，但多出投机头使 TTFT 变长
        · 在 TTFT 与 ITL 间按 SLA/SLO 取舍
        · 需按数据集多轮实测接受率再定参数
      Data Parallelism ／数据并行 · p261
        · 数据并行（DP）复制多份模型实例，用于提吞吐
        · TP/PP 装下大模型，DP 扩吞吐，EP 服 MoE
        · 请求量大时先水平扩展副本
      Tensor Parallelism and Pipeline Parallelism ／张量并行与流水线并行 · p263
        · LLM 路由比传统 Web 更关键：硬件贵、负载差异大
        · 路由信号：KV cache 命中率、显存占用、队列长度、输入长度
      Expert Parallelism ／专家并行 · p268
        · TP=4、PP=2 可在单台 8 卡节点内跑 7B 模型
        · 跨节点推理受网络瓶颈限制，需 Ray 编排
        · 专家并行（EP）把 MoE 专家分散到多块 GPU
      Prefill-Decode Disaggregation ／预填充解码分离 · p269
        · prefill 计算密集、decode 访存密集，同卡部署互相干扰
        · PD 分离（PD disaggregation）把两阶段拆到不同实例
      Overall Architecture ／整体架构 · p271
        · PD 分离可对两阶段做非对称、独立扩缩
        · prefill 突发性强宜激进扩容，decode 平稳可预测
        · DistServe 由控制器（controller）统一路由请求
      KV Cache Transfer ／KV cache 传输 · p272
        · PD 分离成败取决于 KV cache 能否高效传到 decode 实例
        · 分离收益必须大于 KV cache 传输开销
      When to Use ／使用时机 · p274
        · KV cache 可分块（chunk）流式传输，边算边传
        · 异步非阻塞传输让通信与计算重叠
        · KV cache 按层切分，可逐层传以尽早启动 decode
      Advanced KV Caching ／进阶 KV 缓存 · p276
        · 进阶 KV 缓存面向超长上下文（如代码 copilot）
        · 前文三招：投机解码、并行、PD 分离
      Cost and Latency Calculations ／成本与延迟计算 · p277
        · KV cache 可卸载到 CPU 内存、SSD 或远端存储
        · 跨副本路由（cross-replica routing）让缓存可复用
        · 长上下文 CAG 省掉实时检索，但也带来成本
      Self-Hosting LLMs ／自托管 LLM · p279
        · CAG 缓存 10 万 token，成本近 RAG（5 千 token）两倍
        · RAG 的索引与检索成本远低于 LLM 调用，总体更便宜
        · 自托管可用 KV cache 卸载（offloading）压成本
      …另 1 节
    LLM Serving Frameworks ／LLM 服务框架 · p289 · 精读
      vLLM ／vLLM · p290
        · 传统 DL 服务：短输入、定长张量，主靠批处理
        · LLM 逐 token 自回归生成，服务难题与图像模型不同
      vLLM’s Architecture ／vLLM 架构 · p291
        · vLLM 两大招牌：分页 KV 缓存（paged KV caching）＋连续批处理
        · 还支持量化、投机解码、流式与多 GPU 分布式
        · 直击长提示、高显存、多用户并发的痛点
      Model Initialization Workflow （with Multi-Process Worker） ／模型初始化流程（多进程 worker） · p294
        · 三层组件：ModelExecutor、GPUWorker、GPUModelRunner
        · ModelExecutor 编排多 worker，ModelRunner 跑网络
        · 每个模型独立进程，靠分层隔离关注点
      Generation-Request Execution Workflow ／生成请求执行流程 · p296
        · LLM 主进程初始化引擎、调度器、KV 管理器与执行器
        · MultiProcessExecutor 起 4 个 worker，用消息队列下发指令
      Scheduler Deep Dive ／调度器深入剖析 · p297
        · GPUWorker 负责实际前向计算与模型级优化
        · Scheduler 负责通用服务规划与调度优化
      vLLM’s Layered Optimization Strategy ／vLLM 分层优化策略 · p302
        · 分层优化：调度器管全局、执行器懂架构、层内做融合
        · 调度器与模型无关，架构优化独立演进
        · 层内优化：KV 复用、FlashAttention、算子融合
      TensorRT-LLM ／TensorRT-LLM · p303
        · TensorRT-LLM 目标是榨干 NVIDIA GPU 与 Tensor Core
        · 适合已标准化在 NVIDIA 栈、追求极致效率的组织
      SGLang ／SGLang · p304
        · SGLang 硬件覆盖广：NVIDIA、AMD、CPU、TPU、Jetson、昇腾
        · 性能与 vLLM 相当，某些负载更好，但社区更小
        · 强项：结构化生成与多步 Agent 提示
      Llama.cpp ／Llama.cpp · p305
        · Llama.cpp 可在 CPU、Apple Silicon 与小 GPU 上直接跑
        · 暴露 OpenAI 兼容接口，本地零云费部署
      Selecting the Right Framework ／选择合适的框架 · p307
        · 低并发、重延迟隐私时，选轻量本地方案
        · 选框架先看负载：吞吐型才需要复杂调度与大批次
    LLM Optimization in Practice ／LLM 优化实战 · p311 · 精读
      LLM Serving Optimization Plan ／LLM 服务优化计划 · p312
        · 实验目标：优化 Qwen3-14B 的 token 吞吐
        · 需 L40S 级 GPU，附 Jupyter 记录各步输出
      Optimize Qwen3-14B serving with vLLM ／用 vLLM 优化 Qwen3-14B 服务 · p314
        · 按 8 步走：硬件→流量→指标→服务→基准→量化→调优→分布式
        · 代码在 model_optimization_in_practice.ipynb
      Step 1: Examine the GPU hardware ／第1步：检查 GPU 硬件 · p314
        · 实验机为 AWS EC2 g6e.2xlarge，显存约 46 GB
        · nvidia-smi 可查型号、算力（compute cap）与显存占用
      Step 2: Generate Benchmark Traffic ／第2步：生成基准流量 · p315
        · 用 ShareGPT 抽 2000 条提示、每秒 10 请求造流量
        · bench serve 可调请求速率、爬坡（ramp-up）与并发上限
      Step 3: Define Evaluation Metrics ／第3步：定义评估指标 · p318
        · 吞吐看总 TPS 与输出 TPS，后者决定解码成本
        · TTFT 衡量 prefill 效率，含加载、分词与调度延迟
      Step 4: Set Up the Model Serving Server ／第4步：搭建模型服务器 · p319
        · 显存不足会频繁换入换出，解码期重算、吞吐下降
        · 量化省下的显存可扩大 KV cache，抬高批并发
      Step 5: Benchmark the Qwen3 Model with vLLM ／第5步：用 vLLM 基准测试 Qwen3 · p320
        · 先测原生 Qwen3-14B，留作吞吐与延迟基线
        · 对比前提：同流量、同模型、同硬件
      Step 6: Benchmark the Quantized Qwen3 Model with vLLM ／第6步：基准测试量化 Qwen3 · p322
        · 量化选 AWQ 4 比特版 Qwen3-14B-AWQ
        · 量化腾出显存给 KV cache，换来更高并发
      Step 7: Apply Additional Optimization Techniques ／第7步：应用更多优化技术 · p324
        · AWQ 主要省权重搬运与显存，不减少计算量
        · 再按流量模式与 GPU 特性微调 vLLM 配置
      Step 8: Benchmark the Qwen3 Model with Distributed Serving ／第8步：分布式服务基准测试 · p326
        · 实验聚焦单机多卡，最贴近常见非超大规模场景
        · 多节点场景建议用 PD 分离（prefill-decode disaggregation）
      Common Optimization Trade-0ffs ／常见优化权衡 · p329
        · g6e 的 L40S 无 NVLink，只能走 PCIe，通信开销大
        · 分布式不必然更快：单卡有时吞吐与延迟都更好
        · p4d 四卡配置总体吞吐最佳
    Advancements in LLM Serving ／LLM 服务新进展 · p333 · 快读
      Semantic Caching ／语义缓存 · p334
        · 语义缓存（semantic caching）用向量检索匹配同意图提示
        · 不再按精确提示匹配，改比较嵌入（embedding）相似度
        · 路由结合前缀缓存与 KV 使用率做负载均衡
      Performance Profiling Strategies ／性能分析策略 · p336
        · PII 网关用小 NER 模型识别人名、邮箱等敏感实体
        · 按位置与标签把实体替换成 <NAME_1> 占位符
        · 正则常用来补 NER 做 PII 掩码
      Multimodal Serving ／多模态服务 · p340
        · 多模态服务要处理异构输入、大图像张量与跨模态注意力
        · 本书只讲多模态输入、文本输出，不含生成图像/视频
      Multimodal Input Processing ／多模态输入处理 · p340
        · 视觉编码器（vision encoder）把图像切成小块（patch）
        · 每块投影到 LLM 隐维度，互相注意后得视觉嵌入
        · 文本与视觉走双流处理（dual-stream）
      Architectural and System Implications ／架构与系统影响 · p341
        · 缓存、批处理、流式原则要扩展到图像等多模态输入
        · vLLM v1 双进程：Process 0 预处理，Process 1 发射 GPU 内核
        · 分离后预处理再重也不阻塞内核发射，吞吐更高
      Edge AI: Drivers and Enablers ／边缘 AI：驱动与使能 · p342
        · 边缘 AI 靠低功耗硬件才可行
        · 早年移动端推理受慢 CPU、小内存与电池拖累
      Specialized Low-Power Hardware ／专用低功耗硬件 · p344
        · NPU 是 SoC 内专攻低精度张量运算的加速块
        · 专用加速器取代通用 CPU 承担重负载
      Heterogeneous Compute ／异构计算 · p344
        · CPU 负责图像缩放、色彩转换等分支与内存操作
        · NPU 跑计算密集层，GPU 做后处理与实时渲染
        · 先进运行时支持子图切分（subgraph partitioning）
      Thermal-Aware Scheduling ／热感知调度 · p345
        · 热感知调度（thermal-aware scheduling）按温度调节负载
        · 端侧持续满载会降频，调度需避开过热
      Edge–Cloud Hybrid Compute ／边云混合计算 · p345
        · 边缘先过滤、提特征并压缩嵌入，再交云端大模型
        · 端侧预处理降低云端资源消耗，整体更快
        · 自适应卸载（adaptive offloading）按带宽、电量、温度选端或云
      Multi-LoRA Serving ／多 LoRA 服务 · p346
        · 多 LoRA 服务适合每适配器流量低、单跑不饱和的场景
        · 适配器流量大时，应把 LoRA 合并进主模型独立服务
      Model Serving in Reinforcement Learning ／强化学习中的模型服务 · p348
        · RL 中服务系统负责策略采样，不再只是推理
        · 训练与采样解耦，服务侧要能撑住大量并发采样
      LLM Serving in RL ／RL 中的 LLM 服务 · p348
        · RLHF 中 actor 权重定期同步回服务副本
        · 服务系统为训练提供千级并发的低延迟采样
      Determinism in RL Serving ／RL 服务中的确定性 · p349
        · RL 采样需可复现，须控制随机性与批组成
        · 固定种子与温度，便于复现同一策略采样
      …另 1 节
```