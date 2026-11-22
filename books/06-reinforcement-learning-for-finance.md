# Reinforcement Learning for Finance：用 Python 做金融强化学习

> 以 DQL 为主线，把智能体从 CartPole 一路带到预测游戏、算法交易、动态对冲、动态配置与最优执行，几乎每章交付一个可跑的金融环境。

## 基本信息
- Yves Hilpisch / O'Reilly 第一版（2024-10 首印，版权页 2025）/ PDF 215 页（正文 192 页）
- 难度：★★★☆☆ — 数学只到 Bellman 递推，不难；难在 TF/Keras 与 Gymnasium 的版本敏感，以及「奖励怎么设」没有标准答案。
- 目标读者：会 NumPy/pandas/Keras、要做动态决策（交易、对冲、配置）的量化从业者；不适合 RL 零基础且不打算读代码的人。
- 建议投入：约 40 小时 — 10 章，每章 3 小时读 + 1 小时跑通；CPU 足够，单章训练多在几分钟内。

## 章节结构

| 章 | 英文标题 | PDF 起始页 | 内容要点（一句） | 精读建议 |
|---|---|---|---|---|
| 1 | Learning Through Interaction | 17 | 抛硬币/掷骰子的贝叶斯更新，RL 九大构件 | 选读——建立直觉即可 |
| 2 | Deep Q-Learning | 33 | FHMDP、Bellman、Q-learning，DQL 打通 CartPole | 精读——唯一系统讲算法 |
| 3 | Financial Q-Learning | 51 | 预测游戏：四个滞后特征预测涨跌，复用 DQL | 精读——第一个金融环境 |
| 4 | Simulated Data | 65 | 加白噪声、GBM/Vasicek 蒙特卡洛造序列 | 选读——思路简单代码可抄 |
| 5 | Generated Data | 81 | GAN 造时间序列，KS 检验比对分布 | 选读——非主线 |
| 6 | Algorithmic Trading | 99 | 富特征 + 模拟序列，多空两动作的交易环境 | 精读——第 3 章的升级版 |
| 7 | Dynamic Hedging | 119 | 把 BSM delta 对冲改成连续动作的 RL 问题 | 精读——全书最漂亮的映射 |
| 8 | Dynamic Asset Allocation | 143 | 两基金分离、2/3 资产，奖励=Sharpe−惩罚 | 精读——奖励设计范例 |
| 9 | Optimal Execution | 181 | Almgren-Chriss 最优清算，actor-critic | 精读——唯一的新算法 |
| 10 | Concluding Remarks | 203 | 总结与改进方向 | 快读——十分钟翻完 |

取舍理由：2、7、8、9 章决定你能否把 RL 用到自己问题上，第 5 章与第 10 章可后置。

## 核心概念（12 条）
- **agent / environment** — 智能体按 step 与环境交互，环境回 next_state、reward、done（第 2 章 p26）。
- **FHMDP** — 有限时域马尔可夫决策过程：状态、动作、转移、奖励四件套（第 2 章 p22）。
- **policy σ** — 从状态到动作的映射；最优策略让总奖励的上确界取到（第 2 章 p22）。
- **value function V** — 从某状态出发的最优总奖励，Bellman 方程把它拆成单步（第 2 章 p23）。
- **Q function** — Q(s,a)=r+γ·max_a Q(s′,a)，给「动作」而不是「状态」估值（第 2 章 p24）。
- **DQL** — 用 DNN 近似 Q，损失取 MSE，目标值由下一状态的最大 Q 给出（第 2 章 p31）。
- **ε-greedy** — ε 从 1.0 按 0.9975 衰减到 0.1，探索与利用的开关（第 2 章 p25）。
- **replay / memory** — deque(maxlen=2000) 存经验，每步抽 32 条批量更新（第 2 章 p30–31）。
- **reward shaping** — 交易用 P&L、配置用 Sharpe−调仓惩罚、对冲用复制误差；奖励决定学什么（第 8 章 p148）。
- **data augmentation** — 历史数据不够就加噪声、蒙特卡洛模拟、GAN 造样本（第 4–5 章）。
- **two-fund separation** — 最优组合只在无风险资产与市场组合之间分配（第 8 章 p130）。
- **actor-critic** — actor 输出动作、critic 估价值，两个网络分开训练（第 9 章 p182）。

## 数学与公式
- 贝叶斯/MLE：α_MLE=f_h/(f_h+f_t)——第 1 章 p10。
- 目标函数：max Σ r_t(s_t,a_t) s.t. s_t=f_(t−1)(s_(t−1),a_(t−1))——第 2 章 p22。
- Bellman：V_t(s_t)=max_a [r_t(s_t,a)+V_(t+1)(f_t(s_t,a))]——第 2 章 p23。
- Q-learning：Q(s_t,a_t)=r_t(s_t,a_t)+γ·max_a Q(s_(t+1),a)——第 2 章 p24。
- DQN 目标：target=r+γ·max_a Q̂(s′,a)，loss=(target−Q̂(s,a))²——第 2 章 p31。
- Sharpe 奖励：reward=SR−(x_t−x_(t−1))²，SR=年化收益/年化滚动波动——第 8 章 p148–149。
- AC99 成本：永久冲击 γΣx_t，临时冲击 ηΣ(x_t/Δt)²Δt，执行风险 λσ²Σ(X−Σ(x_i/Δt))²Δt——第 9 章 p168–169。
- 最优轨迹：d²x/dt²−(λσ²/η)x=0 ⇒ x_t\*=X·sinh(κ(T−t))/sinh(κT)，κ=√(λσ²/η)——第 9 章 p169。
- actor-critic 更新：critic 拟合 target=r+η·V(s′)，actor 拟合动作——第 9 章 p183。

## 代码与数据
- 依赖：TensorFlow 2.13 + Keras（`keras.optimizers.legacy.Adam`、`disable_eager_execution()`）、Gymnasium（CartPole-v1）、NumPy/pandas/matplotlib/SciPy、scikit-learn。
- 代码：https://rl4f.pqp.io；数据：https://certificate.tpq.io/rl4finance.csv 与 findata.csv（含 AAPL.O、.SPX、.VIX、EUR= 等 12 个标的）；正文从 `dqlagent.py`、`simulation.py` 导入类，Quant Platform 免费注册即可在线跑。

## 怎么读这本书
- 路径：2→3→7→8→9，回头再补 4、5 的数据增强；1、10 随时翻。
- 可跳：第 1 章 AlphaGo/AlphaZero 战报（p12–17）、第 5 章简单示例的 GAN 原理推导。
- 坑：① `optimizers.legacy` 在 TF 2.16+ 已移除，而 TF 2.13 只支持到 Python 3.11；本机 RTX 50 系装不上就退 CPU 或 Colab。② Gymnasium 的 `step()` 返回 5 元组，旧 gym 是 4 元组，`done` 与 `trunc` 要分开看。③ 数据 URL 失效时用本地 CSV 顶上，列名必须与代码一致。④ 结果强依赖 seed，书中数字不可逐位复现。

## 与其他书的关系
- **Financial Theory with Python**：第 7 章的 delta、BSM 公式、风险中性定价都来自那本第 5–6 章，先读它再来。
- **Deep Learning for Finance**（Kaabar）：那本是监督学习预测价格，本书是序贯决策；网络搭建部分可互看。
- **Python Data Science Handbook** / **MLCK**：pandas 时间序列、scipy.stats、sklearn 预处理查这两本。
- **Learning Modern C++ for Finance**：第 9 章的 AC99 在 C++ 书里有对应的数值实现视角。
- **Blueprints** / **Hands-On LLM Serving**：无重叠，前者 NLP 配方，后者推理部署。

## 自测（4 题）
1. 为什么 DQN 的目标值取「下一状态的最大 Q」而不是实际回报？这会带来什么偏差（第 2 章）？
2. 第 3 章的预测游戏里动作不影响下一状态，这对「强化」意味着什么（第 3 章）？
3. 动态对冲环境的状态为什么是 8 个量？奖励为什么取复制组合的 P&L（第 7 章）？
4. 资产配置把奖励设成 Sharpe−惩罚项，惩罚项究竟起什么作用（第 8 章）？
