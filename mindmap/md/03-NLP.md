# 03 Blueprints for Text Analytics Using Python

`Albrecht 等 · Python 文本分析实战 · 422 页 · 13 章`

路径：文本与推理工程 → NLP

```mermaid
mindmap
  root((NLP))
    Gaining Early Insights from Textual Data ／从文本数据中获取初步洞察 · p23 · 精读
      Exploratory Data Analysis ／探索性数据分析 · p24
        · 用汇总统计与频次统计系统检视数据
        · 文本集合在自然语言处理中称语料库（corpus）
      Introducing the Dataset ／介绍数据集 · p25
        · 案例语料为联合国大会 7507 篇演讲
        · 覆盖 1970–2016 年，可观察时代思潮
      Blueprint: Getting an Overview of the Data with Pandas ／蓝图：用 Pandas 概览数据 · p26
        · 先用 df.head 与 df.info 摸清列结构
        · 大数据集先抽样开发语句与图表
      Calculating Summary Statistics for Columns ／计算各列汇总统计 · p27
        · df.info（） 看类型与内存，deep 估文本占用
        · df.describe（include='O'） 汇总类别列
        · 旧版 Pandas 字符串列类型为 object
      Checking for Missing Data ／检查缺失数据 · p28
        · fillna（'unknown'） 填补缺失的说话人
        · describe 的 unique 与 freq 暴露取值不一致
      Plotting Value Distributions ／绘制取值分布 · p29
        · 同名异写（如 Bush 多种拼法）会扭曲统计
        · 直方图把长度列等宽切成 30 个区间
      Comparing Value Distributions Across Categories ／比较各类别取值分布 · p30
        · catplot 按类别对比分布，可选箱线或小提琴
        · isin 过滤出五个常任理事国子集
        · 小提琴图能显出多峰，箱线图不能
      Visualizing Developments Over Time ／可视化时间趋势 · p31
        · groupby（'year'）.size（）.plot（） 画时间序列
        · dt 访问器直接取 year、month 等时间属性
      Blueprint: Building a Simple Text Preprocessing Pipeline ／蓝图：构建简单文本预处理流水线 · p32
        · 简单流水线三步：小写化、分词、去停用词
        · 这里用正则自建分词器，不依赖 spaCy
      Performing Tokenization with Regular Expressions ／用正则表达式分词 · p33
        · 分词（tokenization）把字符序列切成词
        · str.split（） 是最简单最快的分词器
      Treating Stop Words ／处理停用词 · p34
        · 停用词（stop words）高频但信息量低
        · 可套用 NLTK 停用词表，也可换任意词表
      Processing a Pipeline with One Line of Code ／一行代码跑通流水线 · p35
        · 去停用词会删掉否定词，破坏情感分析
        · TF-IDF 以降权代替删除高频词
      Blueprints for Word Frequency Analysis ／词频分析蓝图 · p37
        · 词袋模型（bag-of-words）丢词序只看频次
        · 词频分析适合分类与主题，不适合情感分析
      Blueprint: Counting Words with a Counter ／蓝图：用 Counter 统计词频 · p37
        · Counter 统计词频，FreqDist 继承并扩充
        · 按频次降序取 head（n） 得高频词表
      …另 8 节
    Extracting Textual Insights with APIs ／用 API 提取文本洞察 · p55 · 选读
      Blueprint: Extracting Data from an API Using the Requests Module ／蓝图：用 Requests 提取 API 数据 · p57
        · 用 requests 库按 URL 调用 API 取数据
        · 以 GitHub API 演示查询语言流行度
        · requests 是最常用的 HTTP 请求库
      Pagination ／分页 · p61
        · 分页（pagination）逐页取完整个结果集
        · 用递归函数翻页直到没有下一页
      Rate Limiting ／速率限制 · p63
        · 递归分页共抓到约 3800 条 PyTorch 评论
        · 速率限制（rate limiting）限制单位时间请求数
      Blueprint: Extracting Twitter Data with Tweepy ／蓝图：用 Tweepy 提取 Twitter 数据 · p67
        · 用社区维护的 Tweepy 封装 Twitter API
        · 封装库省去调用与认证的技术细节
      Obtaining Credentials ／获取凭据 · p67
        · 在 Twitter 开发者平台建应用取凭据
        · 凭据含 API key 与 API secret key
      Installing and Configuring Tweepy ／安装并配置 Tweepy · p69
        · pip install tweepy 安装库
        · AppAuthHandler 传入密钥完成认证
        · 实例化 tweepy.API 作为调用入口
      Extracting Data from the Search API ／从搜索 API 提取数据 · p69
        · 搜索 API 按关键词批量拉取推文
        · 结果转成 DataFrame 便于后续分析
      Extracting Data from a User’s Timeline ／从用户时间线提取数据 · p73
        · 用 screen name 取指定账号的时间线
        · 对比两队推文词云看主题差异
        · max_words 与 stopwords 控制词云
      Extracting Data from the Streaming API ／从流式 API 提取数据 · p75
        · 流式 API 主动推送数据，不用反复请求
        · 适合近实时采集，需保持长连接监听
    Scraping Websites and Extracting Data ／抓取网站并提取数据 · p79 · 选读
      Scraping and Data Extraction ／抓取与数据提取 · p80
        · 抓取三阶段：生成 URL、下载、提取
        · 本章提供常见元素的提取蓝图
      Introducing the Reuters News Archive ／介绍路透社新闻档案 · p81
        · 路透档案约 20 亿网页，存为 WARC 格式
        · 可从 AWS S3 直接读取，或整包下载
        · sklearn 自带 newsgroups 数据便于快速实验
      URL Generation ／生成 URL · p83
        · URL 生成（URL generation）常是最难一步
        · 关键在于避免系统性地漏掉 URL
      Blueprint: Downloading and Interpreting robots.txt ／蓝图：下载并解读 robots.txt · p84
        · RobotFileParser 读取并解析 robots.txt
        · can_fetch 判断某 agent 能否抓某 URL
        · sitemap 位置不固定，多写在 robots.txt 里
      Blueprint: Finding URLs from sitemap.xml ／蓝图：从 sitemap.xml 找 URL · p85
        · sitemap 常只给子 sitemap 引用，需再展开
        · 先从 robots.txt 确认 sitemap.xml 被放行
      Blueprint: Finding URLs from RSS ／蓝图：从 RSS 找 URL · p87
        · RSS 用 XML 给出 URL、标题与摘要
        · RSS 停供时可退回使用网页存档版本
      Downloading Data ／下载数据 · p88
        · 没有 sitemap 时改从其他来源收集 URL
        · URL 列表可直接喂给下载循环
      Blueprint: Downloading HTML Pages with Python ／蓝图：用 Python 下载 HTML 页面 · p90
        · requests.Session 复用连接批量下载
        · 用 r.ok 与状态码判断是否被封
        · 被封可换 IP、代理或 VPN，注意合法性
      Blueprint: Downloading HTML Pages with wget ／蓝图：用 wget 下载 HTML 页面 · p91
        · wget 支持 URL 列表与 HTTP keep-alive
        · -nc 跳过已下载文件，避免重复抓取
      Extracting Semistructured Data ／提取半结构化数据 · p92
        · 先拿单篇文章试验提取方法
        · 半结构化数据要按页面结构定位
      Blueprint: Extracting Data with Regular Expressions ／蓝图：用正则表达式提取数据 · p92
        · 用浏览器查看源代码定位目标片段
        · re.search 抓 <title> 等标签内容
      Blueprint: Using an HTML Parser for Extraction ／蓝图：用 HTML 解析器提取 · p93
        · 正则不适合解析 HTML，应改用 HTML 解析器
        · BeautifulSoup 按标签树取目标内容
      Blueprint: Spidering ／蓝图：爬虫遍历 · p100
        · 爬虫遍历是生成 URL 与下载的多级循环
        · 该蓝图可扩展到百万级页面
      Introducing the Use Case ／介绍应用场景 · p100
        · 只看单页不够，需整站内容看全貌
        · 组合前几节技术做档案级抓取
      …另 7 节
    Preparing Textual Data ／准备文本数据 · p111 · 精读
      A Data Preprocessing Pipeline ／数据预处理流水线 · p112
        · 流水线：原始数据进，干净特征出
        · 预处理步骤分必需与可选两类
      Introducing the Dataset: Reddit Self-Posts ／介绍数据集：Reddit 自发帖 · p113
        · 用 Reddit 自发帖（UGC）练数据清洗
        · 用户文本多缩写、话题标签、表情与错字
        · 只取 autos 类 2 万条子集
      Loading Data Into Pandas ／把数据载入 Pandas · p113
        · 2 万条子集可直接载入内存处理
      Blueprint: Standardizing Attribute Names ／蓝图：标准化属性名 · p113
        · 用 rename 统一列名为小写风格
        · 列名统一后蓝图代码才能复用
      Saving and Loading a DataFrame ／保存与加载 DataFrame · p115
        · to_pickle 快且保留类型，但仅限 Python
        · CSV 与 JSON 通用却会丢数据类型
        · 每步预处理后存检查点文件
      Cleaning Text Data ／清洗文本数据 · p116
        · 先列出质量问题类型再动手清洗
        · 去掉 HTML、Markdown 标签与链接
        · 删除问候语、签名与重复引用
      Blueprint: Identify Noise with Regular Expressions ／蓝图：用正则识别噪声 · p117
        · 用正则定位 HTML 标签、URL 等噪声
        · 识别不必完美，能暴露问题即可
      Blueprint: Removing Noise with Regular Expressions ／蓝图：用正则去除噪声 · p118
        · apply（min_len=10） 算出 impurity 列
        · 按 impurity 排序挑最脏记录检查
      Blueprint: Character Normalization with textacy ／蓝图：用 textacy 规范字符 · p120
        · textacy 统一连字符、引号与 Unicode
        · remove_accents 去掉重音符号
      Blueprint: Pattern-Based Data Masking with textacy ／蓝图：用 textacy 按模式脱敏 · p121
        · textacy.preprocessing 按模式替换敏感片段
        · 邮箱、电话、@用户名换成占位符
        · 表情符号统一替换为 _EMOJI_
      Tokenization ／分词 · p123
        · 分词要顾及日期、@用户名与连字符
        · 简单正则 \w\w+ 会丢掉符号与表情
      Blueprint: Tokenization with Regular Expressions ／蓝图：用正则表达式分词 · p123
        · 自定义 RE_TOKEN 并补表情符号规则
        · re.VERBOSE 让复杂正则可读
      Tokenization with NLTK ／用 NLTK 分词 · p124
        · word_tokenize 组合 Treebank 与 Punkt
        · 对话题标签与表情切分效果差
        · 也可改用 RegexpTokenizer
      Recommendations for Tokenization ／分词建议 · p125
        · 按语料选分词器，社媒用推文分词器
        · 表情与 URL 需专门的正则规则
      …另 17 节
    Feature Engineering and Syntactic Similarity ／特征工程与句法相似度 · p143 · 精读
      What You’ll Learn and What We’ll Build ／学习目标与结果 · p144
        · 文档向量化把文本转成数值向量
        · 自建向量化器可当专用蓝图
        · scikit-learn 提供词袋与 TF-IDF 模型
      A Toy Dataset for Experimentation ／实验用玩具数据集 · p145
        · 实验表明知道词是否出现往往已够用
        · 先用几句名著的玩具数据做实验
      Blueprint: Building Your Own Vectorizer ／蓝图：自建向量化器 · p145
        · 分步实现：先枚举词表，再生成矩阵
        · 自建一遍便于理解向量化内部机制
      Enumerating the Vocabulary ／枚举词表 · p145
        · 用 set 枚举词表并按首次出现编号
        · 词典（dictionary）即词到编号的映射
        · BPE、SentencePiece 可压缩词表维度
      Vectorizing Documents ／将文档向量化 · p146
        · 按词表把每句转成 0/1 向量
        · 只记词是否出现即 one-hot 编码
      The Document-Term Matrix ／文档-词项矩阵 · p148
        · 文档-词项矩阵行是文档、列是词
        · 大词表须用稀疏向量（sparse vector）
        · 该矩阵是后续相似度计算的基础
      Bag-of-Words Models ／词袋模型 · p151
        · 词袋（bag-of-words）记录每篇的词频
        · LDA 主题模型明确要求词袋输入
        · 分类与情感任务上表现尚可
      Blueprint: Using scikit-learn’s CountVectorizer ／蓝图：用 CountVectorizer · p151
        · CountVectorizer 一行代码产词频矩阵
        · 输出列按字母序排列
        · 重复词在矩阵中显示为计数 2
      Blueprint: Calculating Similarities ／蓝图：计算相似度 · p153
        · 点积受向量长度影响，不宜判相似
        · 余弦相似度只看向量夹角
        · cosine_similarity 可直接传整个矩阵
      TF-IDF Models ／TF-IDF 模型 · p154
        · 余弦相似度取值 0–1，便于比较
        · 一次算全部两两相似度得对称矩阵
      Optimized Document Vectors with TfidfTransformer ／用 TfidfTransformer 优化文档向量 · p155
        · TfidfTransformer 把词频矩阵转成 TF-IDF
        · IDF 给常见词降权、稀有词提权
      Introducing the ABC Dataset ／介绍 ABC 数据集 · p156
        · ABC 数据集含 2003–2017 年新闻标题
        · TF-IDF 让仅共享常见词的文档相似度下降
      Blueprint: Reducing Feature Dimensions ／蓝图：降低特征维度 · p158
        · 特征过多时训练成本按多项式上升
        · 先删停用词这类低信息量词来降维
      Blueprint: Improving Features by Making Them More Specific ／蓝图：让特征更具体 · p160
        · max_df 删除在语料中出现太频繁的词
        · 例：剔除见于 ≥10% 标题的词
        · 领域专用高频词未必在停用词表里
      …另 9 节
    Text Classification Algorithms ／文本分类算法 · p173 · 精读
      What You’ll Learn and What We’ll Build ／学习目标与结果 · p174
        · 监督学习需带标签的数据训练
        · 案例：预测缺陷优先级与所属模块
        · 涵盖划分、评估与交叉验证
      Introducing the Java Development Tools Bug Dataset ／介绍 Java 开发工具缺陷数据集 · p174
        · 标签含优先级 P1–P5 与六类组件
        · 各组件缺陷数差异大，UI 17479、Core 13669
      Blueprint: Building a Text Classification System ／蓝图：构建文本分类系统 · p178
        · 先分步实现，再合成统一蓝图
        · 监督学习学的是输入到标签的映射
      Step 1: Data Preparation ／第1步：数据准备 · p180
        · 多类别（multiclass）每条只有一个标签
        · 多标签（multilabel）一条可有多个标签
      Step 2: Train-Test Split ／第2步：训练测试划分 · p181
        · train_test_split 固定 random_state 便于对比
        · stratify 保持训练集与测试集标签分布
      Step 3: Training the Machine Learning Model ／第3步：训练机器学习模型 · p183
        · 用 LinearSVC 训练，C 控制正则强弱
        · tol 设置收敛容差，如 1e-5
        · fit 的输入是向量化后的特征
      Step 4: Model Evaluation ／第4步：模型评估 · p185
        · 用准确率等指标量化分类效果
        · 混淆矩阵看错分集中在哪些类别
      Final Blueprint for Text Classification ／文本分类最终蓝图 · p192
        · 类别不平衡可上采样或下采样
        · SMOTE 合成新少数类样本而非复制
      Blueprint: Using Cross-Validation to Estimate Realistic Accuracy Metri ／蓝图：用交叉验证估计真实准确率 · p195
        · 效果差可加词元化、清噪声、调 min_df
        · 交叉验证给出更真实的准确率
      Blueprint: Performing Hyperparameter Tuning with Grid Search ／蓝图：用网格搜索调超参数 · p197
        · cross_val_score 做 5 折交叉验证评分
        · 验证前要在整个数据集上重新向量化
      Blueprint Recap and Conclusion ／蓝图回顾与结论 · p199
        · 网格搜索比较 min_df、ngram_range 与 C
        · 最佳组合准确率也只有约 0.46
        · 可列出候选模型看参数如何互相影响
      Closing Remarks ／结语 · p203
        · 模型在语义边界样本上仍会错分
        · 结语强调结果必须人工审视
    How to Explain a Text Classifier ／如何解释文本分类器 · p205 · 精读
      What You’ll Learn and What We’ll Build ／学习目标与结果 · p206
        · 本章讲如何解释监督模型的预测结果
        · 从缺陷分类案例切入可解释性
      Probability ／概率 · p206
        · 分类器输出各类别的预测概率
        · 概率高低可当置信度参考
      Blueprint: Measuring Feature Importance of Predictive Models ／蓝图：衡量预测模型特征重要性 · p211
        · 预测概率与结果质量存在相关性
        · 只让模型判断高置信样本，模糊的交人工
        · 剔除大量样本会牺牲整体覆盖
      Blueprint: Using ELI5 to Explain the Classification Results ／蓝图：用 ELI5 解释分类结果 · p220
        · LIME 适用线性 SVM，复杂核不行
        · ELI5 同样用 LIME 算法但代码更少
        · ELI5 也支持非线性 SVM
      Blueprint: Using Anchor to Explain the Classification Results ／蓝图：用 Anchor 解释分类结果 · p223
        · Anchor 用规则集合解释单条预测
        · threshold 控制解释要达到的置信度
      Using the Distribution with Masked Words ／用掩码词的分布 · p223
        · 被遮词的分布揭示哪些词影响判断
        · ELI5 仍在开发，注意与 sklearn 版本兼容
        · 同用 LIME，LIME 与 ELI5 结果应可比
      Working with Real Words ／处理真实词语 · p226
        · use_unk_distribution=False 用真实词替换
        · UNK 词会掩盖模型的真实反应
        · 替换词由 spaCy 词向量挑选
    Topic Modeling and Clustering ／主题建模与聚类 · p229 · 精读
      What You’ll Learn and What We’ll Build ／学习目标与结果 · p230
        · 对比 NMF、SVD 与 LDA 三种主题模型
        · 同一用例跑多种方法再比优劣
      Our Dataset: UN General Debates ／数据集：联合国一般性辩论 · p230
        · 沿用联合国大会辩论语料
        · 可在文档与段落两级上建主题
      Checking Statistics of the Corpus ／检查语料统计 · p230
        · 统计确认无缺失年份，语料可用
        · 每篇演讲平均段落数随年份下降
      Preparations ／准备工作 · p232
        · 主题建模的输入是文档-词项矩阵
        · TfidfVectorizer 用 min_df=5、max_df=0.7
        · 文档级矩阵为 7507×24611
      Nonnegative Matrix Factorization （NMF） ／非负矩阵分解（NMF） · p233
        · NMF 把非负矩阵分解为 W 与 H
        · W 是文档-主题，H 是主题-特征
        · 主题数越少，分解就越不精确
      Blueprint: Creating a Topic Model Using NMF for Documents ／蓝图：用 NMF 为文档建主题模型 · p234
        · W 按总和归一化得各主题占比
        · 主题占比过于集中说明主题数要调
      Blueprint: Creating a Topic Model for Paragraphs Using NMF ／蓝图：用 NMF 为段落建主题模型 · p236
        · 段落级建模要先展平并剔除空段落
        · 单元更细，主题往往更纯
      Latent Semantic Analysis/Indexing ／潜在语义分析与索引（LSA） · p237
        · SVD 把矩阵分成 U、Σ、V*
        · 只取最大奇异值即得近似解
        · 奇异值个数 t 相当于主题数
      Blueprint: Creating a Topic Model for Paragraphs with SVD ／蓝图：用 SVD 为段落建主题模型 · p239
        · 截断后 U 为 m×t、V* 为 t×n
        · 思路与 NMF 的图示结构相近
      Latent Dirichlet Allocation ／潜在狄利克雷分配（LDA） · p241
        · LDA 视文档为多个主题的混合
        · 主题又由词的混合构成
        · 狄利克雷先验让主题与词更集中
      Blueprint: Creating a Topic Model for Paragraphs with LDA ／蓝图：用 LDA 为段落建主题模型 · p241
        · 对段落的计数矩阵跑 LDA
        · 以段落为单元，主题更聚焦
      Blueprint: Visualizing LDA Results ／蓝图：可视化 LDA 结果 · p243
        · pyLDAvis 直接吃 sklearn 的 LDA 结果
        · 气泡大小是主题占比，红条是词频
      Blueprint: Using Word Clouds to Display and Compare Topic Models ／蓝图：用词云展示并比较主题模型 · p244
        · 用 PCA 把主题投到二维看分布
        · 传 mds='tsne' 改用 t-SNE 投影
        · 二维投影只是近似，别过度解读
      Using Gensim for Topic Modeling ／用 Gensim 做主题建模 · p250
        · Gensim 提供更多主题模型算法
        · 还能估计模型质量（一致性）
      …另 9 节
    Text Summarization ／文本摘要 · p265 · 选读
      Extractive Methods ／抽取式方法 · p267
        · 抽取式（extractive）摘要挑原文句子拼接
        · 不改写原文，结果可溯源
      Data Preprocessing ／数据预处理 · p267
        · 摘要对象分长文、短新闻、对话三类
        · 文本类型不同，预处理方式也不同
      Blueprint: Summarizing Text Using Topic Representation ／蓝图：用主题表示做文本摘要 · p268
        · 先下载并解析文章得到待摘要文本
        · 用主题表示给句子打分再排序
      Identifying Important Words with TF-IDF Values ／用 TF-IDF 值识别重要词 · p269
        · 算法靠词的重要性而非理解语义
        · 含重要词多的句子排名更靠前
        · TF-IDF 是最简单的找重要词方法
      Blueprint: Summarizing Text Using an Indicator Representation ／蓝图：用指示表示做文本摘要 · p273
        · 指示表示（indicator）用句子特征打分
        · TextRank 用图排序挑出重要句
      Measuring the Performance of Text Summarization Methods ／评估文本摘要方法性能 · p277
        · TextRank 几乎覆盖各节重点句
        · 可与 LSA 方法的结果对比
      Blueprint: Summarizing Text Using Machine Learning ／蓝图：用机器学习做文本摘要 · p280
        · ROUGE 用精确率、召回率与 F 值评摘要
        · 实测 TextRank 得分高于 LSA
        · 评测要选合适的参考摘要
      Step 1: Creating Target Labels ／第1步：构建目标标签 · p281
        · 读 travel_threads.csv 建 DataFrame
        · 用给定摘要标出 summaryPost 标签
      Step 2: Adding Features to Assist Model Prediction ／第2步：添加特征辅助预测 · p284
        · 论坛帖按是否入选摘要打 0/1 标签
        · 极短帖子可能被误判成摘要
      Step 3: Build a Machine Learning Model ／第3步：构建机器学习模型 · p285
        · 手工特征与 TF-IDF 特征拼在一起建模
        · 特征列含标题相似度、文本长度、帖序
      Closing Remarks ／结语 · p287
        · 抽取式摘要落地容易，适合筛论坛帖
    Word Embeddings ／词向量 · p289 · 精读
      The Case for Semantic Embeddings ／语义嵌入的理由 · p290
        · 语料是 autos 类 20 个子版块共 2 万帖
        · 嵌入让语义相近的词向量也相近
      Word Embeddings ／词向量 · p291
        · 嵌入维度 d 通常取 50–300
        · 各维含义不可解释，由模型自行学出
      Analogy Reasoning with Word Embeddings ／词向量类比推理 · p292
        · 词向量能支持类比推理（analogy）
        · queen−king ≈ woman−man 的向量关系
      Types of Embeddings ／嵌入类型 · p292
        · 常见嵌入有 Word2Vec、GloVe、FastText
        · FastText 用子词信息处理未登录词
      Blueprint: Using Similarity Queries on Pretrained Models ／蓝图：在预训练模型上做相似度查询 · p295
        · 预训练嵌入省去自己训练的成本
        · 用 Gensim 的下载器直接取模型
      Loading a Pretrained Model ／加载预训练模型 · p295
        · api.load 自动下载并载入模型
        · 模型默认缓存到 ~/gensim-data
        · glove-wiki-gigaword-50 体积小且够用
      Similarity Queries ／相似度查询 · p296
        · 该 GloVe 模型在约 60 亿词上训练
        · most_similar 查最接近的词
      Blueprints for Training and Evaluating Your Own Embeddings ／训练与评估自定义嵌入蓝图 · p299
        · 在 2 万条领域帖上训练专属嵌入
        · 数据准备方式显著影响模型效果
      Data Preparation ／数据准备 · p299
        · 预训练嵌入会带有性别等偏见
        · 清洗与分词决定嵌入质量
      Blueprint: Training Models with Gensim ／蓝图：用 Gensim 训练模型 · p302
        · Word2Vec 设 size=100、window=2
        · sg=1 用 skip-gram，缺省为 CBOW
        · negative 指定负采样数
      Blueprint: Evaluating Different Models ／蓝图：评估不同模型 · p303
        · 参数网格比较 Word2Vec 与 FastText
        · 只存词向量 KeyedVectors，省空间
      Blueprints for Visualizing Embeddings ／嵌入可视化蓝图 · p306
        · 画图前先把向量降维到二维或三维
      Blueprint: Applying Dimensionality Reduction ／蓝图：应用降维 · p306
        · window=5 的 skip-gram 效果最好
        · 相似词能对上竞品车型，可验质量
        · 降维（dimensionality reduction）后再画图
      Blueprint: Using the TensorFlow Embedding Projector ／蓝图：使用 TensorFlow 嵌入投影器 · p310
        · Embedding Projector 支持 PCA、t-SNE、UMAP
        · 需准备向量与词表两个 TSV 文件
        · 有在线版，不必安装 TensorFlow
      …另 2 节
    Sentiment Analysis ／情感分析 · p317 · 精读
      What You’ll Learn and What We’ll Build ／学习目标与结果 · p318
        · 介绍多种估计文本情感的技术路线
        · 没有一种蓝图能通吃所有场景
      Sentiment Analysis ／情感分析 · p318
        · 情感分析要按文本类型定制方案
        · 推文口语化、标点乱，处理更难
      Introducing the Amazon Customer Reviews Dataset ／介绍亚马逊客户评论数据集 · p319
        · 数据集含 ASIN、评论文本、标题与星级
        · 词典法免标注，监督法更准但要标注
        · 句子级情感需再汇总到文档级
      Blueprint: Performing Sentiment Analysis Using Lexicon-Based Approache ／蓝图：用词典法做情感分析 · p321
        · 没有标签时用情感词典（lexicon）打分
        · 逐词取分再相加得整体情感
      Bing Liu Lexicon ／Bing Liu 词典 · p322
        · Bing Liu 词典给正负词标极性分
        · 词典由专家整理，省去逐条标注
        · 德语等 81 种语言也有现成词典
      Disadvantages of a Lexicon-Based Approach ／词典法的缺点 · p324
        · 词典法结果可当其他方法的基线
        · 按星级分组看均值，验证方向正确
        · scale 归一后再按 overall 求均值
      Supervised Learning Approaches ／监督学习方法 · p325
        · 监督法学习数据中的模式，更贴近现实
        · 可比较多种算法挑出最准的
      Preparing Data for a Supervised Learning Approach ／为监督学习准备数据 · p325
        · 监督法要标注数据，成本较高
        · 多人标注分歧时由第三人裁决
      Learning Algorithm ／学习算法 · p326
        · 按评分把评论转成 1/0 情感标签
        · 问题变成用文本预测情感
      Step 2: Train-Test Split ／第2步：训练测试划分 · p327
        · 按 80/20 划分训练集与测试集
        · stratify 保持正负类分布一致
      Step 3: Text Vectorization ／第3步：文本向量化 · p327
        · 用 TF-IDF 把文本转成特征矩阵
        · 向量化只在训练集上 fit，避免泄漏
      Step 4: Training the Machine Learning Model ／第4步：训练机器学习模型 · p328
        · 文本分类首选 SVM，LinearSVC 训练快
        · 随机森林、XGBoost 精度相近可备选
        · tol=1e-5 控制收敛精度
      Pretrained Language Models Using Deep Learning ／基于深度学习的预训练语言模型 · p329
        · 模型能判出负面与正面评论
        · 要与 Bing Liu 词典基线对比才知提升
      Deep Learning and Transfer Learning ／深度学习与迁移学习 · p330
        · 语言模型是自然语言的数学表示
        · 预训练模型在大语料上学好再迁移
      …另 5 节
    Building a Knowledge Graph ／构建知识图谱 · p345 · 选读
      What You’ll Learn and What We’ll Build ／学习目标与结果 · p346
        · 信息抽取是 NLP 中最难的任务之一
        · 目标是从公司新闻建知识图谱
      Knowledge Graphs ／知识图谱 · p346
        · 知识图谱用节点与边表示实体及关系
        · 可用 RDF 三元组或属性图存储
      Information Extraction ／信息抽取 · p347
        · RDF 是 W3C 定义实体关系的标准
        · Wikidata、DBpedia 是公开大图谱
      Introducing the Dataset ／介绍数据集 · p348
        · 流程含 NER、共指消解与关系抽取
        · 图数据库可选 GraphDB、Neo4j、Grakn
      Named-Entity Recognition ／命名实体识别 · p349
        · 只用 acq 类并购新闻建图
        · 清洗掉 HTML 转义与股票代码
        · 全大写标题被丢弃，正文保留
      Blueprint: Using Rule-Based Named-Entity Recognition ／蓝图：用规则做命名实体识别 · p351
        · spaCy 默认 NER 能找出全部实体
        · 人名与机构常被混淆，需后续消解
        · 也可换用 Stanza 或 Flair
      Blueprint: Normalizing Named Entities ／蓝图：规范化命名实体 · p353
        · 规范化先删去无信息的前后缀
        · 如去掉机构名末尾的 's 与冠词
      Merging Entity Tokens ／合并实体词元 · p354
        · 用 Span 复制并调整首尾词元位置
        · 合并后 London 与交易所的关系会丢失
      Coreference Resolution ／共指消解 · p355
        · 同一实体有多种表面形式（surface form）
        · 把后文提及链到首次提及
      Blueprint: Using spaCy’s Token Extensions ／蓝图：用 spaCy 的词元扩展 · p356
        · 用 token._ 扩展自定义属性存消解结果
        · 每步处理都实现成 nlp 管道函数
      Blueprint: Performing Alias Resolution ／蓝图：做别名消解 · p357
        · 别名消解（alias resolution）用查字典
        · 把 SEC 之类缩写映射到全称
      Blueprint: Resolving Name Variations ／蓝图：消解名称变体 · p358
        · 名称变体按文中先后顺序匹配
        · 传播实体类型来修正误标
      Blueprint: Performing Anaphora Resolution with NeuralCoref ／蓝图：用 NeuralCoref 做指代消解 · p360
        · NeuralCoref 消解代词等间接指代
        · its、He 指回先出现的机构或人
      Name Normalization ／名称规范化 · p362
        · 正则去掉 Co、Inc、Ltd 等法律后缀
        · 同名不同实体仍分开处理
      …另 10 节
    Using Text Analytics in Production ／在生产环境使用文本分析 · p381 · 选读
      Blueprint: Using Conda to Create Reproducible Python Environments ／蓝图：用 Conda 建可复现环境 · p382
        · 用 environment.yml 锁定依赖版本
        · 文件只列显式请求的包，其余自动解析
        · 换机器即可重建同一环境
      Blueprint: Using Containers to Create Reproducible Environments ／蓝图：用容器建可复现环境 · p386
        · Docker 镜像把系统与依赖一起打包
        · 平台无关，协作方拉取即可运行
        · docker tag 与 push 用于分享镜像
      Blueprint: Creating a REST API for Your Text Analytics Model ／蓝图：为文本分析模型建 REST API · p394
        · 用 FastAPI 把模型包成 REST 接口
        · 框架自动生成接口文档与测试页
      Blueprint: Deploying and Scaling Your API Using a Cloud Provider ／蓝图：用云厂商部署并扩展 API · p400
        · 镜像推上云端即可对外提供服务
        · 用 Kubernetes 扩缩容与负载均衡
        · kubectl 与 gcloud 管理集群
      Blueprint: Automatically Versioning and Deploying Builds ／蓝图：自动版本化并部署构建 · p405
        · 推 git tag 触发 GitHub 自动部署
        · 删除 service 与 cluster 可释放算力
        · 生产还须监控准确率并触发重训
      Closing Remarks ／结语 · p409
        · 结语回顾环境、容器与 API 三条路径
        · 目标是让他人能复现并使用你的分析
      Further Reading ／延伸阅读 · p409
        · 延伸阅读给出可深入的方向与资料
      position ／位置 · p3027
        · 本节为图表位置标注，无正文要点
```