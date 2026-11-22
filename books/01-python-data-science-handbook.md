# Python Data Science Handbook（Python 数据科学手册：核心工具四件套）

> 把 IPython、NumPy、Pandas、Matplotlib、Scikit-Learn 串成一条工作流的教材，讲「为什么这样写」，不只讲「这样写」。

## 基本信息

- 作者 / 版次 / 页数 / 出版年：Jake VanderPlas／First Edition（2016 年 12 月首印）／548 页（PDF 总页，正文 5 章 + 索引）／2016
- 难度：★★☆☆☆ —— 假定你会写 Python，五个库都从零讲，数学只给直觉与图示，无矩阵微积分门槛。
- 目标读者：把 Python 当分析工具的科研人员、分析师、转行工程师；也可长期当 API 速查。
- 建议投入：约 45 小时（第 2、3 章各 10h，第 4 章 8h，第 5 章 12h，第 1 章 5h；每天 1.5 小时约五周）。
- 页码说明：下文页码均为 `=== PAGE n ===` 的 PDF 页，比书内印刷页大 18（PDF 19 = 印刷页 1）。

## 章节结构

| 章 | 英文标题 | PDF 起始页 | 内容要点（一句） | 精读建议 |
|---|---|---|---|---|
| 1 | IPython: Beyond Normal Python | 19 | `?`/`??` 查文档、Tab 补全、魔法命令、In/Out 历史、shell 互通与 `%timeit`/`%prun` 剖析。 | 快读 |
| 2 | Introduction to NumPy | 51 | ndarray 的 dtype 与内存、索引切片重塑、ufunc、广播、布尔掩码、排序与结构化数组。 | 精读 |
| 3 | Data Manipulation with Pandas | 115 | Series/DataFrame/Index、标签对齐、缺失值、MultiIndex、concat/merge、groupby、时间序列。 | 精读 |
| 4 | Visualization with Matplotlib | 235 | 两套接口、线/散点/误差/密度图、图例色条、子图、刻度注解、3D、Basemap、Seaborn。 | 选读 |
| 5 | Machine Learning | 349 | scikit-learn 全流程：估计器 API → 验证与网格搜索 → 贝叶斯/回归/SVM/森林/PCA/聚类/GMM/KDE。 | 精读 |

**理由（逐章一句）**

- 第 1 章：知道有这回事即可，用时查表。
- 第 2 章：广播与索引是第 3、5 章的语法地基，含糊了后面寸步难行。
- 第 3 章：对齐、MultiIndex、groupby 是 pandas 反直觉行为的来源，必须动手复现。
- 第 4 章：只需线图/散点/子图/图例四件套，其余按项目取用。
- 第 5 章：同一份数据跑十个算法，是理解「模型即假设」最快的路径。

## 核心概念（10-20 条）

- **ndarray** — 同类型定长多维数组，NumPy 一切操作的载体，比 list 省内存且走编译级循环。
- **ufunc** — 逐元素运算的编译级函数，作者用它解释 NumPy 快在哪（PDF 68 起）。
- **broadcasting** — 形状按尾部维度自动扩展的规则，省掉显式 tile，也是形状错误的主要来源（PDF 81–87）。
- **boolean mask / fancy indexing** — 用布尔数组或整数数组作索引筛元素，后者返回副本（PDF 88、96）。
- **structured array** — 带字段名的复合 dtype 数组，NumPy 版的「表」（PDF 110）。
- **Series / DataFrame / Index** — 带标签一维数组、带行列标签二维表、不可变标签轴（PDF 116–124）。
- **index alignment** — 运算按标签而非位置对齐，对不上补 NaN，pandas 最反直觉也最有用的行为（PDF 134）。
- **MultiIndex** — 层级索引，配 `stack`/`unstack`、`groupby(level=)` 做透视（PDF 146）。
- **merge 的关系代数** — inner/outer/left/right 与 `on` 键、`suffixes` 重名处理（PDF 164）。
- **split-apply-combine** — groupby 的骨架：分组、聚合或变换、拼回（PDF 179）。
- **DatetimeIndex / resample / rolling** — 时间索引、频率偏移、重采样、滑动窗口（PDF 206–220）。
- **estimator API** — `fit`/`predict`/`transform` 统一接口，学会一个就会全部（PDF 379 起）。
- **regularization（ridge/lasso）** — 系数惩罚压复杂度，在多项式基函数回归上演示（PDF 414）。

## 代码与数据

- 依赖库：Python 3；`conda install numpy pandas scikit-learn matplotlib seaborn ipython-notebook`；正文点明 NumPy ≥ 1.8、Matplotlib ≥ 1.5，示例标注「call signature as of Pandas 0.18」。
- 配套代码/数据：https://github.com/jakevdp/PythonDataScienceHandbook；各州人口数据在 http://github.com/jakevdp/data-USstates/；其余用 Seaborn 内置数据集与 sklearn 自带 digits/iris。

## 怎么读这本书

- 推荐路径：2 → 3 → 4（只读 PDF 242–255 线图散点、280–285 子图、267–273 图例）→ 5（PDF 379 估计器 API → 395 验证与网格搜索 → 418 起按需挑算法）；第 1 章留作查表。
- 可跳过：第 1 章 PDF 43–48 的 profiling（需另装 line_profiler/memory_profiler）；第 4 章 308–328 的 3D 与 Basemap、329–348 的 Seaborn；第 5 章 463 流形、494 GMM、509 KDE。
- 常见坑：
  - 书中 `from sklearn.cross_validation import train_test_split` 在 sklearn 0.20 起已移除，须改 `sklearn.model_selection`。
  - `df1.append(df2)`（PDF 160 一带）在 pandas 2.0 被删除，改用 `pd.concat`；`ix` 索引器同理。
  - `%matplotlib inline` 只是 notebook 魔法，脚本里要显式 `plt.show()`（PDF 236 有解释）。
  - Basemap 不在 matplotlib 主包，需 `conda install -c conda-forge basemap`，作者自评「a bit clunky」；项目已停维护，新项目多用 Cartopy（书外补充）。

## 与其他书的关系

- 与《Machine Learning with Python Cookbook, 2e》重叠最多：本书第 2–3 章 ≈ 对方第 1–3 章，第 5 章 ≈ 对方第 11–19 章；本书给「为什么」，对方给配方，宜先本书。
- 是《Blueprints for Text Analytics Using Python》的前置：第 3 章的 groupby、字符串向量化、时间序列正是文本分析的清洗与统计地基。
- 是金融三书的数据层前置：Hilpisch 两书与 Kaabar 都默认你会 NumPy 与 pandas 时间序列。
- 与《Hands-On LLM Serving and Optimization》几乎无重叠；《Learning Modern C++ for Finance》无交集。

## 自测（4 题）

1. （第 2 章）形状 (3,1) 与 (4,) 相加结果是什么形状？广播从哪一维开始对齐？
2. （第 3 章）`groupby(...)['x'].agg('sum')` 与 `.transform('sum')` 长度为何不同？各适合什么场景？
3. （第 4 章）让 2×3 子图共享 x 轴、只在外侧显示刻度标签，`plt.subplots` 要传哪几个参数？
4. （第 5 章）为什么不能用训练集准确率挑模型？网格搜索如何保证「挑参数」与「报成绩」用的不是同一份数据？
