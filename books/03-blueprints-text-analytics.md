# Blueprints for Text Analytics Using Python（Python 文本分析实战蓝图）

> 13 章、上百个可复制的 blueprint，把从抓数据到上线 API 的文本分析流水线走一遍。

## 基本信息

- 作者：Jens Albrecht、Sidharth Ramachandran、Christian Winkler｜第 1 版（2020-12，版权页 2021）｜422 页｜O'Reilly
- 难度：★★☆☆☆ —— 代码驱动，数学止于 TF-IDF 与余弦相似度；难在库版本与环境。
- 目标读者：有 pandas/scikit-learn 基础、要把 NLP 落地的分析师与数据工程师。
- 建议投入：约 40 小时（13 章每章 2.5–3 小时，含跑 notebook；环境调试另加 5–8 小时）。

## 章节结构

| 章 | 英文标题 | PDF 起始页 | 内容要点（一句） | 精读建议 |
| --- | --- | --- | --- | --- |
| 1 | Gaining Early Insights from Textual Data | 23 | UN 演讲语料：EDA、分词、TF-IDF、词云、KWIC、n-gram | 精读 |
| 2 | Extracting Textual Insights with APIs | 55 | GitHub API 的分页与限流；Tweepy 抓 Twitter | 选读 |
| 3 | Scraping Websites and Extracting Data | 79 | 路透社存档：robots.txt、sitemap/RSS、HTML 解析、Scrapy | 选读 |
| 4 | Preparing Textual Data for Statistics and Machine Learning | 111 | Reddit 清洗：正则去噪、textacy 规范化、spaCy 词形与 NER | 精读 |
| 5 | Feature Engineering and Syntactic Similarity | 143 | 手写 vectorizer 到 TF-IDF；余弦相似度与句法相似 | 精读 |
| 6 | Text Classification Algorithms | 173 | JDT bug 报告分类四步法、交叉验证、网格搜索 | 精读 |
| 7 | How to Explain a Text Classifier | 205 | 预测概率、SVM 权重、ELI5/LIME、Anchor | 精读 |
| 8 | Unsupervised Methods: Topic Modeling and Clustering | 229 | NMF/LSA/LDA、Gensim、coherence 选 k、HDP | 精读 |
| 9 | Text Summarization | 265 | 抽取式摘要：TF-IDF、TextRank、机器学习打分 | 选读 |
| 10 | Exploring Semantic Relationships with Word Embeddings | 289 | 词向量查询、Gensim 训练、降维可视化 | 精读 |
| 11 | Performing Sentiment Analysis on Text Data | 317 | 词典法、监督学习、BERT 微调 | 精读 |
| 12 | Building a Knowledge Graph | 345 | NER、共指消解、实体链接、共现图、关系抽取 | 选读 |
| 13 | Using Text Analytics in Production | 381 | conda/Docker、FastAPI、云部署、GitHub Actions | 选读 |

取舍理由：1、4、5、6 章打地基，8、10、11 章覆盖三类方法，精读；其余按项目选读。

## 核心概念（13 条）

- **Blueprint** — 自带目标、步骤与输出的完整代码单元，可改名复用；全书体例的核心。
- **TF-IDF** — 词频乘逆文档频率；第 1 章排关键词、第 5 章向量化、第 9 章摘要都用。
- **Keyword-in-context (KWIC)** — 截取关键词左右窗口；第 1 章查一个词的真实用法。
- **Rate limiting** — 单位时间调用配额；第 2 章抓 GitHub/Twitter 前必须先处理。
- **Boilerplate removal** — 去导航、广告等模板文本；第 3 章用密度法与 readability 取正文。
- **Lemma / POS tagging** — 词形还原与词性标注；第 4 章把 "running" 归到 "run"。
- **Document-term matrix** — 文档 × 词条的稀疏矩阵；第 5 章所有向量化方法的落点。
- **Cosine similarity** — 向量夹角余弦；第 5 章比标题、第 10 章比词向量。
- **LIME / Anchor** — 局部可解释：前者拟合线性代理，后者输出 IF-THEN 规则；第 7 章。
- **NMF / LSA / LDA** — 三种主题模型：NMF 最好读、LSA 用 SVD、LDA 为概率模型；第 8 章。
- **Topic coherence** — 主题一致性分数；第 8 章用它客观选主题数 k。
- **TextRank** — 把句子当图节点、按 PageRank 迭代排序；第 9 章抽取式摘要的主力算法。
- **Word embeddings** — 稠密词向量；第 10 章让 "movie" 与 "film" 距离变近。

## 代码与数据

- 依赖库：pandas、scikit-learn、spaCy 2.3.2（`en_core_web_sm`，第 10 章用 `en_core_web_lg`）、textacy、NLTK、Gensim、Transformers（`bert-base-uncased`）、ELI5 0.10.1、Anchor、Tweepy、Scrapy、sumy、NetworkX、FastAPI + Gunicorn、conda/Docker；无统一版本清单。
- 代码：作者 GitHub 仓库，每章一个 notebook，本地或 Colab 可跑；正文只写 "our GitHub repository"，未印 URL。
- 数据：UN General Debates、Reddit self-posts、ABC 标题、JDT bug 报告、Amazon 评论，多在 Kaggle。

## 怎么读这本书

- 推荐路径：1 → 4 → 5 → 6 → 7 → 8 → 10 → 11 → 12 → 13；抓数据时把 2、3 插在第 1 章后。只做一个项目走 1→4→5→6→13。
- 可以跳过：第 2 章 Twitter 部分、第 3 章 Scrapy 细节、第 9 章算法实现、第 13 章云厂商操作。
- 常见坑：① spaCy 2.3.2 与 3.x 的 pipeline API 和模型安装命令都变了；② Twitter v1.1 接口 2023 年后对多数账号关闭，Tweepy 示例失效；③ ELI5 0.10.1 与新版 scikit-learn 冲突（正文自标 "Work in Progress"）；④ textacy 预处理模块后续改名；⑤ Kaggle 数据集需登录、Colab 预装包会漂移。

## 与其他书的关系

- **Python Data Science Handbook**：前置，默认你会 pandas/NumPy/matplotlib 与 sklearn API。
- **Machine Learning with Python Cookbook 2e**：同级互补，第 6、7 章可与该书 sklearn 配方对照。
- **Hands-On LLM Serving and Optimization**：后续，本书停在"训好 BERT"，那本讲怎么高效托管。
- **Deep Learning for Finance**：补深层网络细节；做金融文本（公告、研报、舆情）可套本书流程。
- **Financial Theory with Python / Reinforcement Learning for Finance**：弱相关，只在金融文本决策项目里相邻。
- **Learning Modern C++ for Finance**：无重叠，仅当推理服务用 C++ 重写时相关。

## 自测（4 题）

- 第 1 章：同一语料上，纯词频 Top-10 与 TF-IDF Top-10 为何不同？各举一个会被挤掉的词。
- 第 4/5 章：lemma 与 stem 差别是什么？为什么 lemma 向量化常能降维却可能丢信息？
- 第 7 章：LIME 与 Anchor 的输出形式有何不同？什么场景更该用 Anchor？
- 第 8 章：NMF、LSA、LDA 对"主题"的假设分别是什么？coherence 解决选 k 的什么问题？
