# Learning Modern C++ for Finance（原书名 *Learning Modern C++ for Finance: Foundations for Quantitative Programming*；中文意译《金融现代 C++ 入门：量化编程基础》）

> 一句话定位：以 Black-Scholes、蒙特卡洛、债券与 Eigen 为主线，把 C++11–C++23 的现代特性讲成能直接写定价库的手艺。

## 基本信息

- 作者 Daniel Hanson｜第 1 版（O'Reilly，2024 年 11 月）｜431 页（PDF 计，正文与索引至第 406 页）
- 难度：★★★☆☆ 语言循序渐进，但默认你会类、指针与编译链接；模板、表达式模板、并发才是真门槛。
- 目标读者：写过 Python 或 C 的量化分析师、金融软件工程师、计算金融课程学生。
- 建议投入：约 60 小时。按 10 章＋5 附录、每章 4–5 小时（读＋自己编译跑通）估算，第 8、9 章因外部库再多留时间。

## 章节结构

| 章 | 英文标题 | PDF 起始页 | 内容要点（一句） | 精读建议 |
|---|---|---|---|---|
| 1 | An Overview of C++ | 23 | 金融里的 C++ 史、语言与标准库之分、auto/range-for/CTAD/enum class/lambda、std::numbers | 精读 |
| 2 | Writing User-Defined Classes with Modern C++ Features | 55 | Black-Scholes 类、payoff、functor 求隐含波动率、移动语义与 RVO、<=> | 精读 |
| 3 | Inheritance, Polymorphism, and Smart Pointers | 85 | Payoff 继承体系、裸指针所有权、clone、Rule of Three、unique/shared_ptr | 精读 |
| 4 | The Standard Template Library Part I: Containers and Iterators | 125 | 函数模板与编译模型、vector/deque/list、map/set、迭代器 | 选读 |
| 5 | The Standard Template Library Part II: Algorithms and Ranges | 165 | 算法与 ranges、函数对象、数值算法、view 链式组合 | 选读 |
| 6 | Random Number Generation and Concurrency | 199 | 引擎与分布、shuffle、蒙特卡洛与障碍期权、并行算法、async/future | 精读 |
| 7 | Dates and Fixed Income Securities | 247 | C++20 chrono 日期、计息基准、收益率曲线、贴现因子、债券定价 | 选读 |
| 8 | Linear Algebra | 299 | 惰性求值与表达式模板、Eigen、回归/Cholesky/PCA、mdspan、BLAS | 精读 |
| 9 | The Boost Libraries | 345 | Boost 数学常量与分布、MultiArray 二叉树、Accumulators 指标 | 选读 |
| 10 | Modules and Concepts | 379 | module/import 与头文件之别、分区、concepts 约束模板 | 快读 |
| 附录 A–E | Appendices A–E | 399 | 虚析构、对象切片、移动成员实现、vector 初始化歧义、valarray | 跳过 |

理由：①语法底座；②③的所有权与移动是后面每个定价类的模板；④⑤可边用边查；⑥唯一直接产出价格；⑦⑧⑨按职业方向取舍；⑩工具链尚不稳；附录属补遗。

## 核心概念（14 条）

- **RAII** — 资源随对象生命周期释放；第 3 章用 unique_ptr 管 payoff 的动机。
- **Move semantics** — 移动语义；第 2 章说明按值传参为何不再昂贵。
- **Rule of Three / Five / Zero** — 拷贝、移动、析构的配套规则；第 3 章判定何时手写。
- **unique_ptr / shared_ptr** — 独占与共享所有权；第 3 章用它们替换裸指针。
- **CTAD** — 类模板实参推导；第 1 章引入，第 8 章配 mdspan 使用。
- **Lambda / capture** — 闭包；第 1 章入门，第 5 章当算法谓词。
- **Range view** — C++20 惰性视图；第 5 章用 view 链替代临时容器。
- **Execution policy** — std::execution::par 一行开并行；第 6 章。
- **std::async / future** — 任务式并发；第 6 章给每个蒙特卡洛情景开任务。
- **year_month_day** — C++20 日历类型；第 7 章日期校验与加减的基础。
- **Day count basis** — 计息基准；第 7 章债券现金流折算的前提。
- **Expression template** — 表达式模板；第 8 章解释 Eigen 为何快。
- **mdspan** — C++23 多维数组视图；第 8 章展望标准库线代。
- **Concept** — 概念约束；第 10 章让模板报错变得可读。

## 代码与数据

- 依赖：C++20 标准库（chrono 日期、ranges、concepts），mdspan 需 C++23；Eigen 3.4+；Boost 的 Math Toolkit、MultiArray、Accumulators；编译器为 VS2022/gcc/clang，正文示例多用 VS2022。
- 代码：作者 GitHub 仓库（正文只写 available for download from GitHub，未印 URL），MPL 2.0；第 9 章二叉树用例数据取自 Hilpisch《Python for Finance》2e 第 10 章。

## 怎么读这本书

- 路径：1→2→3→4→5→6，再按方向挑 7/8/9，最后 10；每章先编译跑通再读文字。
- 可跳过：附录 A–E；不碰固收则跳 7，不用 Boost 则跳 9，modules 一节可略读。
- 常见坑：modules 的接口文件扩展名各家不一（MSVC 用 .ixx、Clang 用 .cppm，gcc 仍用 .cpp），编译 flag 也不同；mdspan 要 C++23 且 libstdc++ 够新；Eigen 的 .array() 与矩阵语义别混；gcc 并行算法要链 TBB；Boost 跨版本 API 有变。

## 与其他书的关系

- **Financial Theory with Python**：Hilpisch 补定价与组合理论；本书第 2、6、7 章默认你懂 Black-Scholes 与布朗运动。
- **Python Data Science Handbook**：numpy 的向量化直觉正对应第 8 章 Eigen/mdspan，可先用 Python 验证再翻译。
- **Deep Learning for Finance**：一条 Python 建模线、一条 C++ 实现线，几乎不重叠；做低延迟实盘时本书补的是执行层。
- **Machine Learning with Python Cookbook 2e / Blueprints for Text Analytics / Hands-On LLM Serving**：与本书无直接交集。
- **Reinforcement Learning for Finance**：同样无交集，属另一条算法线。

## 自测（4 题）

1. （第 2 章）BlackScholes 按值返回时，编译器何时用 RVO、何时调移动构造？
2. （第 3 章）OptionInfo 持有 unique_ptr<Payoff> 后，拷贝构造为何必须手写？
3. （第 6 章）把蒙特卡洛情景循环换成 std::execution::par，结果还能复现吗？
4. （第 9 章）用 MultiArray 建 n 步二叉树，节点数为何是 (n+1)(n+2)/2？
