# Deep Learning for Finance（原书名 *Deep Learning for Finance: Creating Machine & Deep Learning Models for Trading in Python*；中文意译《金融深度学习》）

> 一句话定位：用 EURUSD 日线数据把「技术分析 → 传统机器学习 → LSTM/TCN → DQN」串成一条可回测的流水线，前半本补课，后半本建模。

## 基本信息

- 作者 Sofien Kaabar｜第 1 版（O'Reilly，2024 年 1 月）｜362 页（PDF 计，正文与索引至第 344 页）
- 难度：★★☆☆☆ 数学停在导数、矩阵、ADF 检验这一层，代码是几十行的 Keras/sklearn 脚本；难的是金融直觉与前视偏差，不是推导。
- 目标读者：会基础 Python、懂一点交易的量化研究员与金融专业高年级学生。
- 建议投入：约 45 小时。按 12 章、每章 3–4 小时（读＋跑通仓库代码）估算，第 8–11 章各多留 1 小时调参。

## 章节结构

| 章 | 英文标题 | PDF 起始页 | 内容要点（一句） | 精读建议 |
|---|---|---|---|---|
| 1 | Introducing Data Science and Trading | 17 | 数据科学流程、四类资产、金融应用场景 | 快读 |
| 2 | Essential Probabilistic Methods for Deep Learning | 35 | 概率、抽样与检验、熵与信息量 | 选读 |
| 3 | Descriptive Statistics and Data Analysis | 51 | 集中趋势与离散度、相关、平稳性、回归 | 精读 |
| 4 | Linear Algebra and Calculus for Deep Learning | 97 | 矩阵、线性方程组、极限导数积分、优化 | 选读 |
| 5 | Introducing Technical Analysis | 151 | 图表形态、均线、RSI、形态识别 | 选读 |
| 6 | Introductory Python for Data Science | 167 | 语法、异常、pandas、MT5 取数 | 快读 |
| 7 | Machine Learning Models for Time Series Prediction | 193 | 滞后特征框架＋八种回归器对比 | 精读 |
| 8 | Deep Learning for Time Series Prediction I | 231 | 反向传播、优化器，MLP、RNN、LSTM、TCN | 精读 |
| 9 | Deep Learning for Time Series Prediction II | 265 | 分数阶差分、阈值、再训练、时序 CV、多期预测 | 精读 |
| 10 | Deep Reinforcement Learning for Time Series Prediction | 293 | 状态/动作/奖励、Q 表、Bellman、DQN | 选读 |
| 11 | Advanced Techniques and Strategies | 307 | COT 三类模型、比特币波动率、训练可视化 | 选读 |
| 12 | Market Drivers and Risk Management | 341 | 宏观驱动、新闻解读、风控与行为偏差 | 快读 |

理由：①只交代背景；②可后补；③必读、④按需，二者是特征与损失的底座；⑤用到再查；⑥老手可跳；⑦⑧⑨是主干；⑩仅 14 页；⑪是案例拼盘；⑫几乎无代码。

## 核心概念（12 条）

- **Fractional differentiation** — 分数阶差分；第 9 章用 fracdiff 在保留记忆与平稳间取 d≈0.48。
- **Forecasting threshold** — 预测阈值；把连续收益预测切成多/空/观望信号。
- **Look-ahead bias** — 前视偏差；标准化、阈值、再训练一旦跨切分点即泄漏。
- **Stationarity / ADF test** — 平稳性与单位根检验；第 3 章判断能否直接建模。
- **Lagged features** — 滞后特征矩阵；第 7 章框架核心，仓库封装为 data_preprocessing。
- **Time series cross validation** — 时序交叉验证；第 9 章按时间滚动，替代随机 K 折。
- **Continuous retraining** — 连续再训练；每来一根新数据就重训，作者点明代价是速度。
- **Direct / recursive multiperiod forecasting** — 多期预测两条路线，第 9、11 章各有实现。
- **MLP / LSTM / TCN** — 三种网络；第 8 章各给出 Keras 实现与训练曲线。
- **Dropout / BatchNormalization** — 正则化；第 8、9 章用在 MLP 上压过拟合。
- **COT report** — 持仓报告；第 11 章做成净持仓特征预测长期趋势。
- **Model bias / directional accuracy** — 自建指标：预测均值比实际均值、方向命中率。

## 代码与数据

- 依赖：numpy、pandas、matplotlib、scipy、statsmodels、scikit-learn、Keras/TensorFlow（书中写 tensorflow.keras）、xgboost、fracdiff、minepy、pandas-datareader、MetaTrader5；正文只给 pip install 命令，未标版本。
- 代码与数据：GitHub 仓库 github.com/sofienkaabar/deep-learning-for-finance（正文明确），含 master_function.py 与 COT、ISM PMI 的 Excel；行情靠 MetaTrader 5 导出，CPI 经 pandas-datareader 从 FRED 取。

## 怎么读这本书

- 推荐路径：1→3→7→8→9→11，卡住再回补 2/4，第 5 章随用随查；第 10 章留到读完 RLF 再回来。
- 可跳过：第 2 章信息论推导、第 4 章三角与积分、第 5 章形态识别、第 12 章宏观叙事，都不影响跑通主线。
- 常见坑：MetaTrader5 的 Python 包只支持 Windows；fracdiff 的 window 与 mode='valid' 会吃掉开头样本；Keras 3 与书中写法有出入；XGBoost 新参数名改过；阈值化别在切分前做。

## 与其他书的关系

- **Python Data Science Handbook**：numpy/pandas/matplotlib 的地基，第 6 章远不如它细。
- **Machine Learning with Python Cookbook 2e**：第 7 章八种回归器在那边有更干净的 sklearn 配方。
- **Blueprints for Text Analytics Using Python**：第 12 章「新闻解读」只有概念，文本情感得靠这本补。
- **Financial Theory with Python**：Hilpisch 讲定价与无套利，本书几乎不推导，互为理论与实战。
- **Reinforcement Learning for Finance**：第 10 章只是 DQN 速写，RLF 才是强化学习正餐。
- **Hands-On LLM Serving and Optimization**：本书是单机小 MLP，部署与推理优化没涉及，属后续。
- **Learning Modern C++ for Finance**：另一条语言线，无重叠。

## 自测（4 题）

1. （第 3 章）价格一阶差分后 ADF 通过，为什么反而更难预测？平稳与记忆如何取舍？
2. （第 7 章）把 forecasting threshold 从 0 调到 ±0.0005，混淆矩阵与方向准确率怎么变？
3. （第 9 章）分数阶差分 d=0.48 与 d=1 各丢掉什么信息，作者为何取前者？
4. （第 10 章）Q 表与 DQN 的状态表示有何不同？奖励只写持仓浮盈会退化成什么策略？
