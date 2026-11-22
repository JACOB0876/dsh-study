# Machine Learning with Python Cookbook, 2nd Edition（Python 机器学习配方手册）

> 「问题—代码—解释」三段式配方书：23 章约 200 个可直接运行的解法，从读数据到把模型部署成 API；第 2 版深度学习部分整体换成 PyTorch。

## 基本信息

- 作者 / 版次 / 页数 / 出版年：Kyle Gallatin、Chris Albon（1e 作者）／Second Edition（2023 年 7 月首印，ISBN 978-1-098-13572-0）／404 页（PDF 总页，23 章约 200 个配方）／2023
- 难度：★★★☆☆ —— 不需推导，照敲能跑；难在跨度大（预处理→经典 ML→PyTorch→部署），配方之间不铺原理，不懂「为什么」容易套错场景。
- 目标读者：已会 Python 与 pandas、马上要建模调参上线的数据科学家与 ML 工程师；也适合当 API 速查手册。
- 建议投入：约 35 小时（每个配方 8–10 分钟手敲并换自己的数据重跑，每天 1.5 小时约四周）；跳过第 20–22 章可压到 25 小时。

## 章节结构

| 章 | 英文标题 | PDF 起始页 | 内容要点（一句） | 精读建议 |
|---|---|---|---|---|
| 1 | Working with Vectors, Matrices, and Arrays in NumPy | 9 | 向量矩阵与稀疏矩阵、逐元素运算、秩与迹、点积求逆、随机数。 | 快读 |
| 2 | Loading Data | 27 | 从 CSV/Excel/JSON/Parquet/Avro、SQL、Google Sheet、S3 取数。 | 选读 |
| 3 | Data Wrangling | 42 | 切片筛选、改名替换、缺失值、去重、分组聚合、apply 与合并。 | 精读 |
| 4 | Handling Numerical Data | 77 | 缩放标准化、多项式与交互特征、异常值、离散化、缺失填补。 | 精读 |
| 5 | Handling Categorical Data | 96 | 名义与有序编码、字典特征、类别缺失、类别不平衡。 | 精读 |
| 6 | Handling Text | 108 | 清洗分词去停用词、词干词性实体、词袋、TF-IDF、情感分类。 | 选读 |
| 7 | Handling Dates and Times | 125 | 时区、日期拆特征、日期间隔、星期编码、滞后特征、滚动窗口。 | 选读 |
| 8 | Handling Images | 138 | 缩放裁剪模糊锐化、边缘角点、颜色直方图、预训练 embedding、检测分类。 | 选读 |
| 9 | Dimensionality Reduction Using Feature Extraction | 168 | 造新特征：PCA、核 PCA、LDA、NMF、稀疏数据截断 SVD。 | 选读 |
| 10 | Dimensionality Reduction Using Feature Selection | 180 | 删原特征：方差阈值、高相关、卡方与 F 值、递归消除。 | 选读 |
| 11 | Model Evaluation | 190 | 交叉验证、基线、各任务指标、ROC 与阈值、学习曲线、自定义指标。 | 精读 |
| 12 | Model Selection | 217 | 网格与随机搜索、Pipeline 调参、并行加速、选完再评估。 | 精读 |
| 13 | Linear Regression | 230 | 拟合直线、交互效应、非线性、Ridge/Lasso 正则。 | 精读 |
| 14 | Trees and Forests | 240 | 决策树与可视化、随机森林、OOB、特征重要性、boosting、XGBoost、LightGBM。 | 精读 |
| 15 | K-Nearest Neighbors | 259 | 近邻检索、KNN 分类、选 k、半径邻居、faiss 近似近邻。 | 快读 |
| 16 | Logistic Regression | 270 | 二分类与多分类、正则、SGD 处理大数据、不平衡。 | 精读 |
| 17 | Support Vector Machines | 276 | 线性 SVC、核技巧、预测概率、支持向量、不平衡。 | 选读 |
| 18 | Naive Bayes | 286 | 连续/计数/二元特征的朴素贝叶斯与概率校准。 | 快读 |
| 19 | Clustering | 293 | K-Means 与加速版、Mean Shift、DBSCAN、层次聚类。 | 快读 |
| 20 | Tensors with PyTorch | 301 | 张量创建与互转、稀疏张量、索引形状、点积与乘法。 | 选读 |
| 21 | Neural Networks | 312 | autograd、网络设计、分类回归训练、训练曲线、早停、Dropout、调参。 | 精读 |
| 22 | Neural Networks for Unstructured Data | 344 | 图像与文本分类，用 torchvision / Transformers 微调预训练模型。 | 选读 |
| 23 | Saving, Loading, and Serving Trained Models | 354 | joblib/state_dict 存档，Flask、TensorFlow Serving、Seldon 部署。 | 选读 |

**理由（按段）**

- 3–5 章精读：预处理复用率最高，后面每章 Pipeline 都要回来调它。
- 11–12 章精读：决定你会不会自欺欺人，12.4 讲「预处理必须和模型一起调参」。
- 13、14、16 章精读：表格数据三件套，14.11–14.13 的 boosting 直接能上比赛。
- 21 章精读：Lightning 把训练循环收进 `LightningModule`，是 22 章微调的前置。
- 其余快读/选读：NumPy、近邻、贝叶斯、聚类属速查；文本、图像、降维、部署按项目取用。

## 核心概念（10-20 条）

- **recipe 三段式** — 问题、可跑代码、解释取舍；决定用法是带着问题查而非通读。
- **Pipeline** — 把缩放编码与估计器串成一个 `fit` 对象，12.4 用它防交叉验证泄漏。
- **KFold 交叉验证** — 轮换切分估泛化误差，11.1 替代单次切分，11.11 画学习曲线。
- **baseline model** — Dummy 模型先立下限，11.2–11.3，打不过基线说明特征或标签有问题。
- **ROC AUC 与阈值** — 与阈值无关的排序质量，11.4–11.5 用它挑阈值应对不平衡。
- **GridSearchCV** — 穷举超参，12.1–12.2 配 `n_jobs`，12.7 选完再评估。
- **regularization（Ridge/Lasso）** — L2 压幅度、L1 压到 0 顺带选特征（13.4–13.5）。
- **OOB error** — 随机森林袋外误差，省一个验证集（14.6）。
- **feature importance** — 按不纯度下降排序特征后再做选择（14.7–14.8）。
- **boosting** — 逐轮拟合残差，14.11–14.13 是升级到竞赛级模型的最短路径。
- **feature extraction vs selection** — 第 9 章造特征、第 10 章删特征。
- **autograd** — PyTorch 自动微分，20 章建张量语感，21.1 手写梯度下降。
- **model serving** — 23.4 Flask+joblib、23.5 TensorFlow Serving、23.6 Seldon。

## 代码与数据

- 依赖库：NumPy、pandas、scikit-learn、PyTorch 与 PyTorch Lightning、torchvision、Transformers、XGBoost、LightGBM、faiss、NLTK/spaCy、OpenCV、Flask、TensorFlow/Keras（仅 23.2）、Docker。
- 配套代码/数据：正文只说「配有 GitHub 仓库，含在 Docker 里跑 Jupyter 的说明」，未给 URL；图书页 https://oreil.ly/ml_python_2e。示例多为 sklearn 自带 `load_digits`、`make_classification` 与本地文件。

## 怎么读这本书

- 推荐路径：3 → 4 → 5 → 11 → 12 → 13 → 14 → 16 →（做 DL 时）20 → 21 → 22 →（上线）23；第 2 章等换数据源再翻。
- 可跳过：第 1 章（NumPy 已熟）、15/18/19 章（不做基线或探索）、第 8 章（不做 CV）、第 20 章（不碰 PyTorch）。
- 常见坑：
  - 配方默认数据已清洗入内存；把 4.1/4.2 的缩放器在全量数据上 `fit` 再交叉验证即泄漏，正确做法见 12.4。
  - 第 9、10 章英文标题都叫 Dimensionality Reduction（P168、P180），别当重复章节跳过。
  - 深度学习绑定 PyTorch Lightning，`Trainer` 参数名在 2.x 有改动，旧博客代码常报 unexpected keyword。
  - 23.2 用 Keras SavedModel、23.3 用 `state_dict`，互不通用；23.5 需本机 Docker 起服务。

## 与其他书的关系

- 与《Python Data Science Handbook》同栈两端：本书 1–3 章≈PDSH 2–3 章的配方版，11–19 章对应其第 5 章；先 PDSH 建直觉，再用本书查写法。
- 与《Blueprints for Text Analytics Using Python》在文本上重叠（第 6 章 vs 对方 1、4、5 章），主题模型与可解释性由 Blueprints 补。
- 21–22 章是《Hands-On LLM Serving and Optimization》的最低前置：那本默认你会训练与保存模型，本书 23 章补「存与部署」。
- 对金融三书：第 7 章时序特征与 11–12 章评估法可迁移到 Hilpisch 两书与 Kaabar《Deep Learning for Finance》；《Learning Modern C++ for Finance》无重叠。

## 自测（4 题）

1. （第 4 章）右偏的收入特征，`StandardScaler` 与 `PowerTransformer` 各解决什么？
2. （第 11 章）类别不平衡时 accuracy 为何骗人？该看 ROC AUC 还是 PR 曲线？
3. （第 12 章）缩放器放在交叉验证循环外调参，报告的性能偏乐观还是偏悲观？
4. （第 23 章）joblib、SavedModel、`state_dict` 三种存档，加载时各依赖什么？
