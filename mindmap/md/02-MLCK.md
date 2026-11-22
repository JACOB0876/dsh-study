# 02 Machine Learning with Python Cookbook (2e)

`Gallatin & Albon · Python 机器学习经典实例（第 2 版） · 404 页 · 23 章`

路径：数据与 ML 底座 → MLCK

```mermaid
mindmap
  root((MLCK))
    Working with NumPy ／NumPy 基础操作 · p9 · 快读
      1.2 Creating a Matrix ／1.2 创建矩阵 · p10
        · 用 np.array 建二维数组当矩阵
        · np.mat 有专用矩阵结构但不推荐
        · 数组（ndarray）才是 NumPy 事实标准
      1.3 Creating a Sparse Matrix ／1.3 创建稀疏矩阵 · p10
        · 稀疏矩阵只存非零元素
        · 多加零元素总大小不变
        · 类型有压缩列（CSC）、列表的列表、键字典（DOK）
      1.4 Preallocating NumPy Arrays ／1.4 预分配 NumPy 数组 · p12
        · 预分配数组是常见做法
        · 预填值数组可提升性能
        · 也方便造合成数据测算法
      1.5 Selecting Elements ／1.5 选择元素 · p13
        · 用下标 vector【2】 选单个元素
        · 索引从 0 起，【2】 是第三个元素
        · 向量与矩阵都靠索引切片取值
      1.6 Describing a Matrix ／1.6 描述矩阵 · p14
        · 用 shape 看行列数
        · size 返回元素总数（行×列）
        · ndim 返回维度数
      1.7 Applying Functions over Each Element ／1.7 逐元素应用函数 · p14
        · 用 np.vectorize 把函数向量化
        · 可作用到整个数组或切片
        · 本质是 for 循环，不加速
      1.8 Finding the Maximum and Minimum Values ／1.8 求最大值与最小值 · p15
        · 用 np.max / np.min 求极值
        · axis=0 按列，axis=1 按行
      1.9 Calculating the Average, Variance, and Standard ／1.9 计算均值、方差与标准差 · p16
        · 用 np.mean / np.var / np.std 算描述统计
        · axis 参数可按列或按行计算
      1.10 Reshaping Arrays ／1.10 变形数组 · p17
        · 用 reshape 改形状不改元素值
        · reshape 中 -1 表示该维自动推算
        · 只给一个整数则返回一维数组
      1.11 Transposing a Vector or Matrix ／1.11 转置向量或矩阵 · p18
        · 用 .T 转置矩阵或向量
        · 行向量转置后多一层括号变列向量
      1.12 Flattening a Matrix ／1.12 展平矩阵 · p19
        · 用 flatten（） 把矩阵展成一维
        · reshape（1,-1） 可得到行向量
        · np.ravel 能展平矩阵列表
      1.13 Finding the Rank of a Matrix ／1.13 求矩阵的秩 · p20
        · 用 np.linalg.matrix_rank 求秩
        · 秩是行或列张成向量空间的维数
      1.14 Getting the Diagonal of a Matrix ／1.14 获取矩阵对角线 · p20
        · 用 matrix.diagonal（） 取对角线
        · offset 取主对角线上下方的对角线
      1.15 Calculating the Trace of a Matrix ／1.15 计算矩阵的迹 · p21
        · 用 trace 求对角线元素之和
        · 也可 sum（matrix.diagonal（）） 算
        · 迹常在机器学习方法内部用到
      …另 5 节
    Loading Data ／加载数据 · p27 · 选读
      2.2 Creating a Simulated Dataset ／2.2 创建模拟数据集 · p28
        · 用 sklearn 的 make_blobs 造聚类数据
        · 还有 make_regression 与 make_classification
        · 可用 plt.scatter 画散点验证
      2.3 Loading a CSV File ／2.3 加载 CSV 文件 · p31
        · 用 pandas 的 read_csv 载入 CSV
        · 载入前先扫一眼文件结构
        · read_csv 有 30 多个参数适配各种格式
      2.4 Loading an Excel File ／2.4 加载 Excel 文件 · p32
        · 用 read_excel 读 Excel 文件
        · sheet_name 可传表名或零基序号
        · 要多个工作表就传列表
      2.5 Loading a JSON File ／2.5 加载 JSON 文件 · p33
        · read_json 用 orient 指明 JSON 结构
        · orient 可选 split/records/index/columns/values
        · json_normalize 可展开半结构 JSON
      2.6 Loading a Parquet File ／2.6 加载 Parquet 文件 · p34
        · 用 read_parquet 读 Parquet 文件
        · Parquet 是大数据常用高效存储格式
        · 常与 Hadoop、Spark 搭配
      2.7 Loading an Avro File ／2.7 加载 Avro 文件 · p35
        · 用 pandavro 的 read_avro 读 Avro
        · Avro 是靠 schema 的二进制格式
        · 不如 Parquet 常见但使用在增长
      2.8 Querying a SQLite Database ／2.8 查询 SQLite 数据库 · p36
        · 用 read_sql_query 执行 SQL 并载入
        · SELECT * FROM data 取表全部列
        · create_engine 需 SQLite 库已存在
      2.9 Querying a Remote SQL Database ／2.9 查询远程 SQL 数据库 · p37
        · 用 pymysql 建远程 SQL 连接
        · 再用 pandas 读成 DataFrame
        · 企业环境常需主机、端口与账密
      2.10 Loading Data from a Google Sheet ／2.10 从 Google 表格加载 · p38
        · 可直接用 URL 读 Google 表格
        · URL 末尾加 /export?format=csv 即 CSV
        · 省去先下载再读的中间步骤
      2.11 Loading Data from an S3 Bucket ／2.11 从 S3 存储桶加载 · p39
        · 给 pandas 加 storage_options 读 S3
        · s3:// 路径读 CSV 仍需 AWS 凭证
        · 公有对象也有 HTTP 直链可下载
      2.12 Loading Unstructured Data ／2.12 加载非结构化数据 · p40
        · 用内置 open（） 读取非结构化数据
        · 文本、图像这类数据没有固定行列结构
    Data Wrangling ／数据整理 · p42 · 精读
      3.1 Creating a Dataframe ／3.1 创建 DataFrame · p43
        · 用字典 pd.DataFrame（dictionary） 建表
        · 加新列只需 df【'Eyes'】=【...】
        · 真实场景多从文件或数据库建表
      3.2 Getting Information about the Data ／3.2 获取数据信息 · p44
        · 用 info（） 看列名、非空数与类型
        · info 还给出索引范围与内存占用
        · 载入数据后先摸清结构
      3.3 Slicing DataFrames ／3.3 切片 DataFrame · p46
        · 切片用 loc 与 iloc 两种索引
        · 数据清洗中会频繁用到两者
      3.4 Selecting Rows Based on Conditionals ／3.4 按条件选择行 · p49
        · 用 dataframe【条件】 选行
        · 如 df【df【'Sex'】=='female'】
        · 条件过滤是最常用的清洗操作
      3.5 Sorting Values ／3.5 排序值 · p50
        · 用 sort_values 按列排序
        · by 可传多列列表，按顺序排
        · ascending 默认 True，设 False 降序
      3.6 Replacing Values ／3.6 替换值 · p51
        · 用 replace 做查找替换
        · 可整表替换 df.replace（1,'One'）
        · regex=True 支持正则替换
      3.7 Renaming Columns ／3.7 重命名列 · p52
        · 用 defaultdict 建旧列名到新列名的字典
        · 遍历 dataframe.columns 生成字典键
        · 再交给 rename（columns=...） 改名
      3.8 Finding the Minimum, Maximum, Sum, Average, and ／3.8 求极值、和与均值 · p54
        · 用 min/max/mean/sum/count 求统计量
        · 既可作用于单列也可作用于整表
        · 还有 var/std/median/skew 等
      3.9 Finding Unique Values ／3.9 查找唯一值 · p55
        · 用 unique（） 取列中所有唯一值
        · 用 value_counts（） 数各值出现次数
      3.10 Handling Missing Values ／3.10 处理缺失值 · p56
        · 用 isna（） 筛出含缺失值的行
        · 用 fillna（列均值） 填充缺失值
      3.11 Deleting a Column ／3.11 删除列 · p58
        · 删列用 drop 并设 axis=1
        · inplace=True 会直接改原表
        · 建议把 DataFrame 当作不可变对象
      3.12 Deleting a Row ／3.12 删除行 · p60
        · 用布尔条件 df【df【'Name'】!=...】 删行
        · drop（【0,1】, axis=0） 也能删但不实用
        · 条件写法一次删多行更方便
      3.13 Dropping Duplicate Rows ／3.13 删除重复行 · p61
        · 用 drop_duplicates 删除重复行
        · subset 指定判断重复的列
        · keep 控制保留首次还是末次
      3.14 Grouping Rows by Values ／3.14 按值分组行 · p63
        · 用 groupby（列） 分组后取子列统计
        · 如 groupby（'Survived'）【'Name'】.count（）
        · 传列名列表可按多列分组
      …另 7 节
    Handling Numerical Data ／处理数值型数据 · p77 · 精读
      4.2 Standardizing a Feature ／4.2 标准化特征 · p78
        · 用 RobustScaler 做稳健标准化
        · 用中位数与四分位距（IQR）缩放
        · fit_transform 直接得到缩放后数组
      4.3 Normalizing Observations ／4.3 归一化观测值 · p80
        · 用 Normalizer 把观测缩成单位范数
        · norm 参数指定用哪种范数
        · 缩的是每个观测的向量总长度
      4.4 Generating Polynomial and Interaction Features ／4.4 生成多项式与交互特征 · p82
        · 用 PolynomialFeatures（degree=2） 造多项式特征
        · include_bias=False 不生成偏置列
        · 可表达特征与目标的非线性关系
      4.5 Transforming Features ／4.5 变换特征 · p83
        · 用 FunctionTransformer 或 pandas 的 apply 做自定义变换
        · 如对特征取自然对数
        · 先定义函数再映射到特征上
      4.6 Detecting Outliers ／4.6 检测异常值 · p84
        · 异常值检测没有唯一最佳方法
        · 常同时用 EllipticEnvelope 与 IQR 法
        · 要回头检查被判为异常的观测
      4.7 Handling Outliers ／4.7 处理异常值 · p86
        · 先想清异常的原因与数据用途
        · 不处理异常本身也是一种决定
        · 有异常值时标准化可能失效
      4.8 Discretizating Features ／4.8 离散化特征 · p88
        · 把连续特征切成区间变成类别特征
        · 用于特征与目标关系非线性的场景
      4.9 Grouping Observations Using Clustering ／4.9 用聚类分组观测值 · p90
        · 用 KMeans 把观测聚成 k 组作预处理
        · 输出每个观测的组别作为新特征
      4.10 Deleting Observations with Missing Values ／4.10 删除含缺失的观测 · p91
        · 删除含缺失值的观测以保证数据完整
        · 做法简单但会损失样本
        · 另一条路是插补（imputation）
      4.11 Imputing Missing Values ／4.11 填补缺失值 · p93
        · 用 KNNImputer 按近邻预测填补缺失
        · 数据多时用 SimpleImputer 更省事
    Handling Categorical Data ／处理类别型数据 · p96 · 精读
      5.2 Encoding Ordinal Categorical Features ／5.2 编码有序类别特征 · p99
        · 把高/中/低这类有序类别映射成数值
        · 有序类别（ordinal）转数值才能进模型
      5.3 Encoding Dictionaries of Features ／5.3 编码特征字典 · p101
        · 用 DictVectorizer 把字典列表转特征矩阵
        · sparse=False 返回稠密矩阵
        · 默认输出为稀疏矩阵（sparse=True）
      5.4 Imputing Missing Class Values ／5.4 填补缺失类别值 · p103
        · 用 KNN 分类器预测并填补缺失的类别值
        · 简化的替代是填该特征最常见值
        · SimpleImputer 的 strategy='most_frequent'
      5.5 Handling Imbalanced Classes ／5.5 处理不平衡类别 · p104
        · 类别不平衡时模型会偏向多数类
        · 常用重采样或调整类别权重来缓解
    Handling Text ／处理文本 · p108 · 选读
      6.2 Parsing and Cleaning HTML ／6.2 解析与清洗 HTML · p110
        · 用 BeautifulSoup 解析 HTML 并提取文本
        · 用 find（） 按标签定位内容
        · 抓取网页与静态 HTML 都能用
      6.3 Removing Punctuation ／6.3 移除标点 · p111
        · 用 translate 加标点字典删标点
        · 写法偏 hack 但比替代方案快
        · 标点本身含信息，删前要想清
      6.4 Tokenizing Text ／6.4 分词 · p112
        · 把文本切成词元（token）
        · 词级分词是提取词特征前的常见步骤
      6.5 Removing Stop Words ／6.5 移除停用词 · p113
        · 用 NLTK 的 stopwords 移除停用词
        · 首次使用要先下载停用词表
        · stopwords 假定词元已转小写
      6.6 Stemming Words ／6.6 词干提取 · p114
        · 用 PorterStemmer 做词干提取
        · 去掉词缀保留词根，如 humbled→humbl
      6.7 Tagging Parts of Speech ／6.7 词性标注 · p114
        · 用 nltk.pos_tag 给每个词标词性
        · 再用 MultiLabelBinarizer 独热编码
      6.8 Performing Named-Entity Recognition ／6.8 命名实体识别 · p116
        · 用 spaCy 预训练模型做命名实体识别
        · doc.ents 给出实体及其类型标签
        · 类型如 PERSON、ORG、MONEY
      6.9 Encoding Text as a Bag of Words ／6.9 编码为词袋 · p117
        · 把文本编码成词袋（bag of words）向量
        · 只统计词频，丢弃词序
      6.10 Weighting Word Importance ／6.10 加权词重要性 · p120
        · 用 TF-IDF 按重要性给词加权
        · TfidfVectorizer 直接产出特征矩阵
        · 本文件常见、他文件少见的词权重高
      6.11 Using Text Vectors to Calculate Text Similarity in a ／6.11 计算文本相似度 · p121
        · 用文本向量计算文本之间的相似度
        · 相似度常用余弦相似度（cosine similarity）
      6.12 Using a Sentiment Analysis Classifier ／6.12 用情感分析分类器 · p123
        · 用 transformers 的 pipeline 做情感分析
        · pipeline（'sentiment-analysis'） 直接分类
        · 首次运行会下载模型
    Handling Dates and Times ／处理日期与时间 · p125 · 选读
      7.2 Handling Time Zones ／7.2 处理时区 · p126
        · 用 all_timezones 列出可用时区（pytz）
        · 时间字符串可用 to_datetime 转成时间戳
      7.3 Selecting Dates and Times ／7.3 选择日期与时间 · p128
        · 用两个布尔条件分别当起止日期
        · 也可把日期列设为索引后切片
      7.4 Breaking Up Date Data into Multiple Features ／7.4 日期拆成多个特征 · p129
        · 用 Series.dt 取 year/month/day/hour
        · 把日期拆成多个数值特征
      7.5 Calculating the Difference Between Dates ／7.5 计算日期之差 · p130
        · 两个日期相减得到时间差
        · 差值的数据类型是 TimeDelta
      7.6 Encoding Days of the Week ／7.6 编码星期几 · p131
        · 用 dt.day_name（） 得星期几名称
        · 用 dt.weekday 得整数，周一为 0
      7.7 Creating a Lagged Feature ／7.7 创建滞后特征 · p132
        · 用 shift（1） 创建滞后特征
        · 首行没有上一期值，故为缺失值
      7.8 Using Rolling Time Windows ／7.8 使用滚动时间窗 · p133
        · 用 rolling（window=n）.mean（） 算滚动统计
        · 窗口依次滑过观测逐点计算
      7.9 Handling Missing Data in Time Series ／7.9 处理时序缺失数据 · p134
        · 时序缺失值需单独处理（插补或删行）
    Handling Images ／处理图像 · p138 · 选读
      8.2 Saving Images ／8.2 保存图像 · p140
        · 用 cv2.imwrite 保存图像
        · 格式由文件扩展名决定
        · 会直接覆盖同名文件且不报错
      8.3 Resizing Images ／8.3 调整图像大小 · p141
        · 用 resize 把图像尺寸统一
        · 尺寸一致才能当特征使用
        · 缩小图像会丢信息但省内存
      8.4 Cropping Images ／8.4 裁剪图像 · p142
        · 图像即矩阵，用行列切片裁剪
        · 只保留感兴趣的区域（ROI）
      8.5 Blurring Images ／8.5 模糊图像 · p143
        · 模糊是把像素换成邻域均值
        · 邻域与操作用核（kernel）表示
        · 可用 cv2.filter2D 应用核
      8.6 Sharpening Images ／8.6 锐化图像 · p145
        · 锐化用突出像素自身的核
        · 同样用 filter2D 应用核
        · 锐化后边缘对比更明显
      8.7 Enhancing Contrast ／8.7 增强对比度 · p146
        · 用直方图均衡（equalizeHist）增强对比度
        · 把像素强度拉伸到更宽区间
        · 结果常不真实但特征更突出
      8.8 Isolating Colors ／8.8 分离颜色 · p148
        · 先把图像转成 HSV 色彩空间
        · 定义颜色范围并生成掩码
        · 再用 bitwise_and 应用掩码
      8.9 Binarizing Images ／8.9 二值化图像 · p149
        · 用阈值化（threshold）简化图像
        · 自适应阈值需设邻域大小与常数
        · 阈值化可去噪、分离文字
      8.10 Removing Backgrounds ／8.10 移除背景 · p151
        · 画矩形标出前景，交给 GrabCut
        · GrabCut 生成前景与背景掩码
        · 应用掩码后只留前景
      8.11 Detecting Edges ／8.11 检测边缘 · p153
        · 用 Canny 边缘检测器找边缘
        · 边缘图可作后续处理的输入
      8.12 Detecting Corners ／8.12 检测角点 · p155
        · 用 Harris 的 cornerHarris 检测角点
        · 也可用 goodFeaturesToTrack 限定角点数
      8.13 Creating Features for Machine Learning ／8.13 为机器学习建特征 · p157
        · 把图像转成数值特征喂给模型
        · 特征可来自像素、直方图或预训练嵌入
      8.14 Encoding Color Histograms as Features ／8.14 颜色直方图作特征 · p160
        · 对每个颜色通道分别算直方图
        · 把各通道直方图拼成特征向量
      8.15 Using Pretrained Embeddings as Features ／8.15 用预训练嵌入作特征 · p162
        · 用预训练模型（Inception V1）取嵌入
        · 嵌入是 1024 维向量，可当特征
      …另 2 节
    Dimensionality Reduction Using Feature Extraction ／降维：特征抽取 · p168 · 选读
      9.2 Reducing Features When Data Is Linearly Inseparable ／9.2 线性不可分的特征抽取 · p171
        · 用带核的 KernelPCA 做非线性降维
        · 关键参数是 kernel、gamma 与 n_components
        · 核技巧把数据投影后更易线性可分
      9.3 Reducing Features by Maximizing Class Separability ／9.3 最大化可分性抽特征 · p173
        · 用 LDA 最大化类间可分性来降维
        · n_components=None 返回各成分解释方差比
        · 选累计解释方差达 0.95/0.99 的成分数
      9.4 Reducing Features Using Matrix Factorization ／9.4 用矩阵分解抽特征 · p175
        · 用非负矩阵分解（NMF）抽特征
        · 要求输入特征矩阵非负
      9.5 Reducing Features on Sparse Data ／9.5 稀疏数据的特征抽取 · p177
        · 稀疏矩阵降维用截断 SVD（TSVD）
        · 先标准化再转成 csr_matrix
        · TSVD（n_components=10） 指定输出维数
    Dimensionality Reduction Using Feature Selection ／降维：特征选择 · p180 · 选读
      2 Thresholding Binary Feature Variance ／2 按方差阈值筛特征 · p182
        · 用 VarianceThreshold 按方差筛二元特征
        · 方差低于阈值说明信息少，可删
      3 Handling Highly Correlated Features ／3 处理高度相关特征 · p183
        · 用 dataframe.corr（） 算相关矩阵
        · 高度相关特征信息冗余，删掉其一
      4 Removing Irrelevant Features for Classification ／4 为分类移除无关特征 · p184
        · 用卡方统计检验特征与目标的独立性
        · 观察计数与期望计数差异越大越相关
        · 据此剔除与分类无关的特征
      5 Recursively Eliminating Features ／5 递归消除特征 · p186
        · 递归消除特征会反复训练并删弱特征
        · 用 cross_val_score 交叉验证评估
        · n_jobs=-1 用满所有 CPU 核心
    Model Evaluation ／模型评估 · p190 · 精读
      2 Creating a Baseline Regression Model ／2 创建基线回归模型 · p193
        · 用 DummyRegressor 建回归基线模型
        · strategy='constant' 可恒定输出
        · score 返回决定系数 R²，越接近 1 越好
      3 Creating a Baseline Classification Model ／3 创建基线分类模型 · p195
        · 用 DummyClassifier 建分类基线模型
        · strategy 参数控制猜测策略
        · 用它衡量模型比随机猜好多少
      4 Evaluating Binary Classifier Predictions ／4 评估二分类器预测 · p196
        · accuracy 直观但不够全面
        · F1 平衡精确率与召回率
        · 可用 accuracy_score 直接算
      5 Evaluating Binary Classifier Thresholds ／5 评估二分类器阈值 · p199
        · 用 ROC 曲线看各阈值下的 TPR 与 FPR
        · 提高阈值后 TPR 与 FPR 同时下降
      6 Evaluating Multiclass Classifier Predictions ／6 评估多分类器预测 · p202
        · 多分类指标常用 micro 平均
        · micro 先对每个观测-类别组合打分再平均
      7 Visualizing a Classifier’s Performance ／7 可视化分类器性能 · p204
        · 用混淆矩阵（confusion matrix）看错分
        · 对比预测类别与真实类别
      8 Evaluating Regression Models ／8 评估回归模型 · p206
        · 回归用均方误差（MSE）评估
        · MSE 越大误差越大、模型越差
        · 平方会放大少数大误差
      9 Evaluating Clustering Models ／9 评估聚类模型 · p207
        · 聚类用轮廓系数（silhouette_score）评估
        · 取值 -1 到 1，越大簇越紧凑分离
      10 Creating a Custom Evaluation Metric ／10 创建自定义评估指标 · p209
        · 用 make_scorer 把自定义函数变评分器
        · 评分函数接收真实值与预测值
        · greater_is_better 指定越大越好
      11 Visualizing the Effect of Training Set Size ／11 可视化训练集大小影响 · p210
        · 用学习曲线（learning curve）看数据量影响
        · 判断增加训练数据是否还有收益
        · 本例扫了 50 个训练集规模
      12 Creating a Text Report of Evaluation Metrics ／12 生成评估指标文本报告 · p212
        · 用 classification_report 输出指标文本报告
        · 可传 target_names 指定类别名
      13 Visualizing the Effect of Hyperparameter Values ／13 可视化超参数取值影响 · p213
        · 用验证曲线看超参数取值的影响
        · 本例共 10×2×5=100 个候选模型
        · GridSearchCV 会用最优参数在全数据重训
    Model Selection ／模型选择 · p217 · 精读
      2 Selecting the Best Models Using Randomized Search ／2 用随机搜索选择模型 · p219
        · 用 RandomizedSearchCV 随机搜索超参数
        · 比网格搜索更省算力
        · 搜索完用最优超参在全数据重训
      3 Selecting the Best Models from Multiple Learning ／3 从多种学习算法中选模型 · p221
        · 搜索空间里可放多个候选算法
        · 算法参数用 classifier__ 前缀
        · best_estimator_ 看选中的算法
      4 Selecting the Best Models When Preprocessing ／4 预处理纳入模型时选择 · p223
        · 把预处理参数也放进搜索空间
        · 如 PCA 的 n_components 候选 1/2/3
        · 用 preprocess__pca__n_components 查最优
      5 Speeding Up Model Selection with Parallelization ／5 用并行化加速模型选择 · p225
        · 用 n_jobs 并行训练多个候选模型
        · 2000 候选 × 5 折 = 10000 次拟合
      6 Speeding Up Model Selection Using Algorithm- ／6 用算法特定优化加速 · p226
        · 用算法内置的 CV 版本加速调参
        · LogisticRegressionCV 的 Cs 给候选个数
      7 Evaluating Performance After Model Selection ／7 选择后评估性能 · p227
        · 选完模型后再用留出数据评估一次
        · 评估结果要能代表真实场景
    Linear Regression ／线性回归 · p230 · 精读
      2 Handling Interactive Effects ／2 处理交互效应 · p232
        · 用 PolynomialFeatures 造交互项
        · 交互项刻画一个特征对另一个特征的依赖
      3 Fitting a Nonlinear Relationship ／3 拟合非线性关系 · p234
        · 多项式特征加线性回归即多项式回归
        · degree 控制最高次幂
        · include_bias=False 去掉全 1 偏置列
      4 Reducing Variance with Regularization ／4 用正则化降低方差 · p236
        · 用 Ridge/Lasso 的收缩惩罚降低方差
        · alpha_ 保存选出的正则强度
        · 训练前必须标准化特征
      5 Reducing Features with Lasso Regression ／5 用 Lasso 回归减特征 · p238
        · Lasso 回归能把无用特征的系数压到 0
        · 训练前先用 StandardScaler 标准化
    Trees and Forests ／树与森林 · p240 · 精读
      2 Training a Decision Tree Regressor ／2 训练决策树回归器 · p241
        · 决策树按杂质下降最大的规则分裂
        · 默认用基尼不纯度（Gini）
        · 递归分裂到叶节点纯或达阈值
      3 Visualizing a Decision Tree Model ／3 可视化决策树模型 · p243
        · 把决策树导出为 DOT 格式再画图
        · 用 pydotplus 与 tree.export_graphviz
        · macOS 需先装 Graphviz
      4 Training a Random Forest Classifier ／4 训练随机森林分类器 · p245
        · 用 RandomForestClassifier 训练随机森林
        · criterion='entropy' 可换分裂度量
        · 森林比单棵树有更多参数
      5 Training a Random Forest Regressor ／5 训练随机森林回归器 · p246
        · 用 RandomForestRegressor 做回归森林
        · 每棵树用自助采样的观测子集
        · max_features 控制每节点考虑的特征数
      6 Evaluating Random Forests with Out-of-Bag Errors ／6 用袋外误差评估森林 · p247
        · 设 oob_score=True 用袋外误差评估
        · oob_score_ 即袋外观测上的得分
        · 袋外观测天然充当测试集
      7 Identifying Important Features in Random Forests ／7 识别森林中的重要特征 · p248
        · 用 feature_importances_ 看特征重要性
        · 数值越高越重要，所有重要性之和为 1
      8 Selecting Important Features in Random Forests ／8 选择森林中的重要特征 · p251
        · 用 SelectFromModel 按重要性阈值选特征
        · 只用重要特征重训模型
        · 独热编码会稀释重要性，相关特征会偏向一个
      9 Handling Imbalanced Classes ／9 处理不平衡类别 · p252
        · class_weight 传类别权重字典纠偏
        · 也可用算法内置的其他平衡方法
      10 Controlling Tree Size ／10 控制树的大小 · p253
        · 用 max_depth、min_samples_split 等控树
        · max_depth=None 会长到叶子纯为止
        · 限制树深可防过拟合
      11 Improving Performance Through Boosting ／11 通过提升改善性能 · p254
        · 用 AdaBoost 通过提升改善性能
        · base_estimator 默认是决策树
        · learning_rate 调小训练更慢但可能更好
      12 Training an XGBoost Model ／12 训练 XGBoost 模型 · p256
        · 用 xgb.train 训练 XGBoost 模型
        · param 里设 objective 与 num_class
        · 预测结果取 argmax 得类别
      13 Improving Real-Time Performance with LightGBM ／13 用 LightGBM 提实时性 · p257
        · 用 LightGBM 训练更快的梯度提升模型
        · 适合对实时性有要求的场景
    K-Nearest Neighbors ／K 近邻 · p259 · 快读
      2 Creating a K-Nearest Neighbors Classifier ／2 创建 K 近邻分类器 · p261
        · 用 KNeighborsClassifier 做 K 近邻分类
        · weights='distance' 让近邻票权更大
        · algorithm 默认自动选最优算法
      3 Identifying the Best Neighborhood Size ／3 确定最佳邻域大小 · p263
        · k 太小高方差、太大高偏差
        · 用 GridSearchCV 五折交叉验证选 k
      4 Creating a Radius-Based Nearest Neighbors ／4 创建基于半径的最近邻 · p264
        · 用 RadiusNeighborsClassifier 按半径找邻居
        · 需用 radius 指定固定半径
      5 Finding Approximate Nearest Neighbors ／5 查找近似最近邻 · p265
        · ANN 在小数据上结果与精确 KNN 几乎相同
        · 数据越大近似检索的价值越明显
      6 Evaluating Approximate Nearest Neighbors ／6 评估近似最近邻 · p268
        · 用 recall@k 比较 ANN 与精确 KNN
        · 借助 faiss 计算召回率
    Logistic Regression ／逻辑回归 · p270 · 精读
      2 Training a Multiclass Classifier ／2 训练多分类器 · p271
        · 逻辑回归本身只做二分类
        · multi_class='ovr' 为每个类各训一个模型
        · 训练前先标准化特征
      3 Reducing Variance Through Regularization ／3 通过正则化降低方差 · p272
        · 正则化给损失加惩罚项以降方差
        · 惩罚项常用 L1 或 L2
        · LogisticRegressionCV 用 Cs 给候选正则强度
      4 Training a Classifier on Very Large Data ／4 在超大数据上训练 · p273
        · 超大数据用 solver='sag' 的随机平均梯度
        · 先标准化特征再训练
      5 Handling Imbalanced Classes ／5 处理不平衡类别 · p274
        · 用 class_weight 给少数类更高权重
        · 也可重采样后再训练
    Support Vector Machines ／支持向量机 · p276 · 选读
      2 Handling Linearly Inseparable Classes Using Kernels ／2 用核处理不可分类 · p278
        · 线性不可分时用核（kernel）改进 SVM
        · RBF 核的 gamma 与多项式的 degree 要调
        · 惩罚参数 C 也是超参数
      3 Creating Predicted Probabilities ／3 生成预测概率 · p282
        · SVC 用超平面，不天然输出概率
        · 可用 Platt 缩放校准出类别概率
        · 校准需在交叉验证上拟合
      4 Identifying Support Vectors ／4 识别支持向量 · p283
        · 用 SVC（kernel='linear'） 训练线性 SVM
        · support_vectors_ 给出支持向量
        · 超平面只由少数支持向量决定
      5 Handling Imbalanced Classes ／5 处理不平衡类别 · p284
        · 用 class_weight 调整不平衡类别权重
        · 也可重采样后再训练
    Naive Bayes ／朴素贝叶斯 · p286 · 快读
      1 Training a Classifier for Continuous Features ／1 训练连续特征分类器 · p287
        · 连续特征用高斯朴素贝叶斯（GaussianNB）
        · 它假设每个特征服从正态分布
        · 可借 priors 指定类别先验
      2 Training a Classifier for Discrete and Count Features ／2 训练离散计数特征分类器 · p288
        · 离散计数特征用 MultinomialNB
        · alpha 是加性平滑，默认 1.0
        · alpha=0 表示不做平滑
      3 Training a Naive Bayes Classifier for Binary Features ／3 训练二值特征朴素贝叶斯 · p290
        · 二值特征用 BernoulliNB
        · 用 fit 训练后即可 predict
      4 Calibrating Predicted Probabilities ／4 校准预测概率 · p290
        · 把模型输出的概率校准成可信概率
        · SVC 这类模型的概率需校准
    Clustering ／聚类 · p293 · 快读
      2 Speeding Up K-Means Clustering ／2 加速 K-Means 聚类 · p295
        · 用 MiniBatchKMeans 加速 K-Means
        · batch_size=100 控制每批样本数
        · 结果与标准 K-Means 相近但更快
      3 Clustering Using Mean Shift ／3 用 Mean Shift 聚类 · p296
        · 用 MeanShift 聚类，无需预设簇数
        · 不假设簇为球形
        · n_jobs=-1 可并行
      4 Clustering Using DBSCAN ／4 用 DBSCAN 聚类 · p297
        · DBSCAN 用 eps 与 min_samples 定核心点
        · 离群观测被标为 -1
      5 Clustering Using Hierarchical Merging ／5 用层次合并聚类 · p299
        · 层次聚类逐步合并最相近的簇
        · 可画树状图（dendrogram）看合并过程
    Tensors with PyTorch ／PyTorch 张量 · p301 · 选读
      2 Creating a Tensor from NumPy ／2 从 NumPy 创建张量 · p302
        · 用 torch.from_numpy 从 NumPy 建张量
        · 张量可放到 GPU 等加速硬件
        · PyTorch 语法与 NumPy 很像
      3 Creating a Sparse Tensor ／3 创建稀疏张量 · p302
        · 用 tensor.to_sparse（） 建稀疏张量
        · 稀疏张量省内存，适合大量为 0 的数据
        · 稠密与稀疏张量都是 torch.Tensor
      4 Selecting Elements in a Tensor ／4 选择张量中的元素 · p303
        · 张量像数组一样用索引取元素
        · flip（dims=（-1,）） 可反转元素顺序
      5 Describing a Tensor ／5 描述张量 · p305
        · 用 shape、dtype、layout、device 描述张量
        · device 是张量区别于数组的关键属性
      6 Applying Operations to Elements ／6 对元素应用运算 · p306
        · 用广播（broadcasting）对所有元素运算
        · 如 tensor*100 一次性作用全部元素
      7 Finding the Maximum and Minimum Values ／7 求最大值与最小值 · p306
        · 用 tensor.max（） / min（） 求极值
        · 多维张量同样适用
      8 Reshaping Tensors ／8 变形张量 · p307
        · 用 reshape 改张量形状
        · 神经网络常要求张量有特定形状
      9 Transposing a Tensor ／9 转置张量 · p308
        · 用 mT 方法转置张量
        · 一维张量转置后与原张量相同
      10 Flattening a Tensor ／10 展平张量 · p309
        · 用 flatten（） 把张量降成一维
        · 多维输入常需降成一维再接后续层
      11 Calculating Dot Products ／11 计算点积 · p309
        · 用 tensor.dot 计算两个张量点积
        · 在 GPU 上算点积可大幅提速检索
      12 Multiplying Tensors ／12 张量乘法 · p310
        · 用 Python 算术运算符做张量乘法
        · 运算会按元素逐个进行
    Neural Networks ／神经网络 · p312 · 精读
      1 Using Autograd with PyTorch ／1 用 PyTorch 自动求导 · p313
        · PyTorch 的 autograd 自动计算梯度
        · 用有向无环图（DAG）记录运算
        · 转成 NumPy 会“断开计算图”
      2 Preprocessing Data for Neural Networks ／2 为神经网络预处理数据 · p314
        · 用张量运算做标准化，梯度仍可回传
        · grad_fn 记录该张量由哪步运算得来
      3 Designing a Neural Network ／3 设计神经网络 · p316
        · 继承 nn.Module 定义神经网络
        · 用 nn.Linear 堆层、ReLU/Sigmoid 激活
        · 在 forward 里写前向传播
      4 Training a Binary Classifier ／4 训练二分类器 · p319
        · 用 BCELoss 与优化器训练二分类网络
        · 评估放在 torch.no_grad（） 里
      5 Training a Multiclass Classifier ／5 训练多分类器 · p321
        · 训练循环：zero_grad→backward→step
        · 评估时用 no_grad 关掉梯度
      6 Training a Regressor ／6 训练回归器 · p323
        · 回归网络用 TensorDataset 与 DataLoader 供数
        · batch_size=100、shuffle=True 打乱批次
        · 用 MSE 评估回归效果
      7 Making Predictions ／7 进行预测 · p325
        · 用 network.forward（x）.round（） 取预测类别
        · round（） 把概率输出转成 0/1 类别
      8 Visualize Training History ／8 可视化训练历史 · p327
        · 画训练与测试损失随轮次变化
        · 测试误差先降后升说明开始过拟合
      9 Reducing Overfitting with Weight Regularization ／9 用权重正则化减过拟合 · p330
        · 用 weight_decay 做权重正则化
        · 在优化器里设 lr 与 weight_decay
      10 Reducing Overfitting with Early Stopping ／10 用早停减少过拟合 · p331
        · 用 PyTorch Lightning 的 EarlyStopping 早停
        · monitor='val_loss'、patience=3 无改善即停
      11 Reducing Overfitting with Dropout ／11 用 Dropout 减过拟合 · p334
        · Dropout 每批随机把部分单元置零
        · 是正则化小型网络的常用方法
      12 Saving Model Training Progress ／12 保存模型训练进度 · p336
        · 用 torch.save 存 epoch、模型与优化器状态
        · 训练可能数小时数天，中断会丢进度
      13 Tuning Neural Networks ／13 调优神经网络 · p338
        · 用 ray tune 自动搜索层大小与学习率
        · best_trial.config 给出最优配置
        · 自动调参不是万能药
      14 Visualizing Neural Networks ／14 可视化神经网络 · p341
        · 把网络结构画出来便于检查层与形状
    Neural Networks for Unstructured Data ／非结构化数据的神经网络 · p344 · 选读
      2 Training a Neural Network for Text Classification ／2 训练文本分类网络 · p346
        · 用嵌入（embedding）把词映射成向量
        · 文本分类网络用 nll_loss 训练
        · 用 argmax 取预测类别
      3 Fine-Tuning a Pretrained Model for Image ／3 微调预训练模型做图像 · p349
        · 用 transformers 与 torchvision 微调 ViT
        · 迁移学习可在小数据上训练
        · 微调复用预训练模型已学的知识
      4 Fine-Tuning a Pretrained Model for Text ／4 微调预训练模型做文本 · p351
        · 微调预训练模型做文本任务
        · 比从头训练需要更少的标注数据
    Saving, Loading, and Serving Trained Models ／保存、加载与部署 · p354 · 选读
      2 Saving and Loading a TensorFlow Model ／2 保存加载 TensorFlow 模型 · p355
        · 用 Keras 的保存与加载接口存取模型
        · SavedModel 是 TensorFlow 的标准格式
      3 Saving and Loading a PyTorch Model ／3 保存加载 PyTorch 模型 · p357
        · 用 torch.save 与 torch.load 存取模型
        · model.pt 其实是含参数的字典
        · 用 model_state_dict 键恢复权重
      4 Serving scikit-learn Models ／4 部署 scikit-learn 模型 · p359
        · 用 Flask 把 scikit-learn 模型包成 Web 服务
        · 先用 joblib.dump 存模型文件
        · curl POST 到 /predict 得预测结果
      5 Serving TensorFlow Models ／5 部署 TensorFlow 模型 · p360
        · 用 Flask 把 TensorFlow 模型部署成 API
        · 开发服务器不能直接用于生产环境
      6 Serving PyTorch Models in Seldon ／6 在 Seldon 部署 PyTorch · p363
        · 用 Seldon Core 的 Python wrapper 部署模型
        · 网络用 nn.Sequential 逐层堆叠
```