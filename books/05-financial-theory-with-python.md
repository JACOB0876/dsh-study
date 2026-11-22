# Financial Theory with Python：用 Python 讲金融理论

> 两状态 → 三状态 → 一般静态 → 动态，四个玩具经济体把复制、无套利、鞅测度、均衡定价推到 BSM 与蒙特卡洛。

## 基本信息
- Yves Hilpisch / O'Reilly 第一版（2022，2021-10 首印）/ PDF 204 页（正文 176 页）
- 难度：★★☆☆☆ — 只用线性代数与初等概率，推导不跳步；但第 2 章一口气推到 2FTAP，第 5 章记号会突然变密。
- 目标读者：会 Python 想补理论骨架的人；或金融出身想把公式写成代码的人。
- 建议投入：约 26 小时 — 7 章，每章 3 小时读 + 1 小时敲码；只读不敲约 12 小时。

## 章节结构

| 章 | 英文标题 | PDF 起始页 | 内容要点（一句） | 精读建议 |
|---|---|---|---|---|
| 1 | Finance and Python | 17 | 四种语言、conda 与 Jupyter 起步 | 快读——工具可跳 |
| 2 | Two-State Economy | 33 | 复制→无套利→鞅测度→FTAP→均值方差 | 精读——定价原型 |
| 3 | Three-State Economy | 75 | 加状态不加资产→不完备；超复制、CAPM | 精读——全书转折 |
| 4 | Optimality and Equilibrium | 99 | 期望效用最大化，价格转为均衡内生 | 选读——只读两节 |
| 5 | Static Economy | 133 | 一般静态经济；BSM 蒙特卡洛、Merton 跳扩散 | 精读——交出公式 |
| 6 | Dynamic Economy | 163 | CRR 二叉树、GBM 模拟、LSM 美式期权 | 精读——唯一讲时间 |
| 7 | Where to Go from Here? | 185 | 延伸书单与作者其他著作 | 跳过——纯书目 |

取舍理由：2、3、6 章是骨架，第 5 章交公式。

## 核心概念（12 条）
- **state-contingent payoff** — 各状态的钱数写成向量，全书先把资产向量化（第 2 章 p26）。
- **replication portfolio** — 解 Mφ=C1 得 (b\*,s\*)，定价即算复制成本（第 2 章 p43）。
- **arbitrage** — V0=0 而 V1 非负不恒为零，模型即不可用（第 2 章 p41）。
- **martingale measure Q** — 使贴现价格过程成为鞅的概率测度（第 2 章 p49）。
- **risk-neutral probability** — q=(S0(1+i)−S1^d)/(S1^u−S1^d)，由鞅条件解出（第 2 章 p49）。
- **1FTAP / 2FTAP** — 有鞅测度 ⇔ 无套利；唯一 ⇔ 完备（第 2 章 p50–51）。
- **market completeness** — 两资产未来价格向量线性无关即张成 R²，任何 C1 都可复制（第 3 章 p61）。
- **MVP / 均值方差** — 组合波动率 σ_p=s·σ_S，只用一阶矩与二阶矩，第 2 章收尾（p53）。
- **Arrow-Debreu security** — 单状态付 1 单位，价格 γ0=q/(1+i) 即状态价格（第 2 章 p48）。
- **super-/approximate replication** — 不完备时求最便宜的上界组合或用最小二乘（第 3 章 p67–71）。
- **CAPM** — μ_T=i+λσ_ST，只靠与市场组合的协方差定价（第 3 章 p79）。
- **LSM** — 多项式回归估继续价值，倒推是否提前行权（第 6 章 p164）。

## 数学与公式
- 复制解：s\*=(C1^u−C1^d)/(S1^u−S1^d)，b\*=(C1^d·S1^u−C1^u·S1^d)/[B1(S1^u−S1^d)]——第 2 章 p43。
- 无套利定价：C0=b\*B0+s\*S0=10/3−50/33=1.81818——第 2 章 p40–42。
- 鞅定价：C0=[q·C1^u+(1−q)·C1^d]/(1+i)——第 2 章 p51。
- CAPM：μ_T=i+λσ_ST，λ=(μ_S−i)/σ_S²，T0=E[T1]/(1+i+λσ_ST)——第 3 章 p79。
- 效用最大化：max E[u(bB1+sS1)] s.t. bB0+sS0=w——第 4 章 p94–96。
- 代表性个体：对数效用下 S0_i=P(ω_i)——第 5 章 p143。
- BSM：S_T=S0·exp((r−σ²/2)T+σ√T·z)，C0=e^(−rT)·mean(max(S_T−K,0))——第 5 章 p133–134。
- Merton：S_T=S0[exp((r−r_j−σ²/2)T+σ√T·z1)+(exp(μ+δz2)−1)·y]，r_j=λ(exp(μ+δ²/2)−1)——第 5 章 p139。
- CRR：u=e^(σ√Δt)，d=1/u，q=(e^(rΔt)−d)/(u−d)——第 6 章 p150。
- CRR 倒推：V_t=df·[q·V_(t+1)^u+(1−q)·V_(t+1)^d]，df=e^(−rΔt)——第 6 章 p152。
- LSM：V_t=max(h_t, df·V_{t+1})，df·V 对 S_t 做 deg=5 回归——第 6 章 p164。

## 代码与数据
- 依赖 NumPy、pandas、SciPy（minimize）、SymPy（第 4 章）、matplotlib、JupyterLab；conda 建 `finpy` 环境。
- 配套：https://finp.pqp.io（前言 p13）；Quant Platform 免费注册可在线跑 notebook（第 1 章 p9）；正文未给 GitHub 仓库。

## 怎么读这本书
- 路径：1（快）→2→3→6→5→4；先用复制建立「定价=复制成本」，再补连续模型与效用。
- 前置：矩阵可逆、张成、条件期望够用即可；测度论不必先学，书里只用到「鞅」的定义。
- 可跳：安装步骤、第 4 章数值均衡例（p106–114）、第 7 章书单。
- 坑：① `plt.style.use('seaborn')` 新版已移除，改 `'seaborn-v0_8'`；② 第 2 章价格过程是元组 `(t0, ndarray)`；③ 第 3 章矩阵不可逆须用 `lstsq`；④ 第 6 章循环版慢十倍属正常。

## 与其他书的关系
- **Reinforcement Learning for Finance**：本书第 5–6 章（BSM、CRR、蒙特卡洛）是那本第 7 章动态对冲的前置。
- **Deep Learning for Finance**（Kaabar）：互补——本书讲为何这样定价，Kaabar 讲如何用 LSTM/CNN 拟合。
- **Python Data Science Handbook**：ndarray、广播、matplotlib 可直接补。
- **Learning Modern C++ for Finance**：Hanson 用 C++ 实现同一套 BSM/二叉树，可对照看工程化。
- **Machine Learning with Python Cookbook**：第 4 章的 scipy 优化、第 6 章的回归可直接查配方。
- **Blueprints for Text Analytics** / **Hands-On LLM Serving**：无重叠，前者是 NLP 配方，后者是推理部署。

## 自测（4 题）
1. 用 B=(10,(11,11))、S=(10,(20,5))、K=15 手算复制组合与看涨价格，并说出 C0=2 怎么套利（第 2 章）。
2. 三状态两资产时鞅测度为何无穷多？q 区间怎么由 q∈[0,1] 推出（第 3 章）？
3. 写出对数效用下最优组合的一阶条件，并解释 λ 的含义（第 4 章）。
4. 为什么 Merton 跳扩散「宽意义上不完备」，BSM 却完备（第 5 章）？
