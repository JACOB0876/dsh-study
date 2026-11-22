# 08 Learning Modern C++ for Finance

`Hanson · 面向金融的现代 C++ · 431 页 · 11 章`

路径：工程技能 → C++

```mermaid
mindmap
  root((C++))
    An Overview of C++ ／C++ 概览 · p23 · 精读
      C++11: The Modern Era Is Born ／C++11：现代纪元开启 · p24
        · C++11 起，金融模型的各个组件都能用对象表达
      Open Source Mathematical Libraries ／开源数学库 · p26
        · Boost、Eigen、Armadillo 等开源库免去 C 接口适配
        · 用标准 C++ 编写，可直接嵌入金融定价代码
      Some Myths about C++ ／关于 C++ 的误解 · p26
        · 「学 C++ 必须先学 C」是被反复传播的误解
        · C++ 保留大部分 C 语法，但已是独立语言
      Compiled Versus Interpreted Code ／编译型与解释型代码 · p26
        · 解释型语言适合快速建模与可视化
        · 计算密集模型换成 C++ 可从数天缩到数分钟
        · 常见做法是解释语言与 C++ 库互补
      The Components of C++ ／C++ 的组成部分 · p27
        · C++ 由语言特性与标准库两大部分组成
      C++ Language Features ／C++ 语言特性 · p27
        · 支持过程式、面向对象、泛型、函数式四种范式
        · 四者依次对应自由函数、类继承、模板、lambda
        · 语言层面还提供丰富的数值与逻辑基础类型
      The C++ Standard Library ／C++ 标准库 · p28
        · std::size_t 属于标准库而非核心语言
        · vector、string 等是标准库最常用的类型
      Some New Language Features Since C++11 ／C++11 以来的新语言特性 · p31
        · C++11 引入花括号统一初始化：vector<int> v｛1, 2, 3｝
        · CTAD 让类模板实参可省略：MyPair<> p｛...｝
        · std::size_t 是表示对象大小的标准库类型
      The auto Keyword ／auto 关键字 · p32
        · auto k = 1 推导为 int，auto x = 419.53 为 double
        · 本书对 int、double 等基础类型仍显式写出
        · 返回类型明显时用 auto：make_unique<T>（.）
      Range-Based for Loops ／基于范围的 for 循环 · p33
        · for （double x : v） 按值遍历，不必管下标
        · for （double& x : v） 用引用可直接改动元素
        · C++ Core Guidelines 建议容器优先用范围 for
      The using Keyword ／using 关键字 · p34
        · using 把新名字写在前面，比 typedef 更易读
        · Core Guidelines 建议优先 using 而非 typedef
      Uniform Initialization ／统一初始化 · p35
        · int i｛100｝ 是 C++11 起的统一（花括号）初始化
        · vector<int> v（2） 是两个元素，v｛2｝ 是一个 2
        · 圆括号与花括号语义不同，选错含义全变
      Formatting Output ／格式化输出 · p36
        · std::format 返回 string，取代 cout 链式拼接
        · ｛0｝、｛1｝ 是占位符，顺序一致时可省略编号
        · 重复或乱序引用同一参数时才需要编号
      Class Template Argument Deduction ／类模板实参推导 · p37
        · MyPair<> real_pair｛19.73, 10.26｝ 自动推导出 double
        · CTAD 靠构造实参推断模板实参，省去 <double>
        · std::map 这类多参数模板同样受益
      …另 9 节
    User-Defined Classes with Modern C++ ／现代 C++ 用户自定义类 · p55 · 精读
      A Black-Scholes Class ／Black-Scholes 类 · p56
        · Black-Scholes 类可顺带复习自定义类的写法
        · 示例用到 std::array、enum class 与 lambda
      Representing the Payoff ／收益的表示 · p57
        · enum class PayoffType ｛ Call = 1, Put = -1 ｝ 把 ±1 编进枚举
        · static_cast<int>（payoff_type） 取出 ±1 交给定价公式
      Writing the Class Declaration ／编写类声明 · p57
        · 构造函数用默认实参：double div = 0.0
        · 重载 operator（）（double vol），对象像函数一样可调用
        · 成员按声明顺序初始化，列表顺序要与之一致
      Writing the Class Implementation ／编写类实现 · p58
        · std::array<double, 2> 是编译期定长的数组容器
        · compute_norm_args_ 返回 ｛d1, d2｝ 供正态 CDF 使用
        · C++11 加入 std::array，容量固定且无堆分配
      Using a Functor for Root Finding: Implied Volatility ／用 functor 求根：隐含波动率 · p61
        · functor 的 operator（）（vol） 直接充当求根的目标函数
        · time_to_exp = 0 时直接返回到期收益，跳过公式
      Move Semantics and Special Member Functions ／移动语义与特殊成员函数 · p65
        · C++03 四个特殊成员函数：默认构造、拷贝构造、拷贝赋值、析构
        · 移动语义转移所有权，省掉整块数据的拷贝开销
        · 金融程序常只需转移所有权，不必留两份数据
      Data Members and Performance Considerations ／数据成员与性能考量 · p65
        · 大 vector 成员按值拷贝代价很高，因此需要移动
        · 数据成员持有大块内存时优先考虑转移所有权
      An Introduction to Move Semantics ／移动语义入门 · p67
        · SimpleClass（int k） : k_｛k｝ ｛｝ 用初始化列表构造成员
        · 移动把资源从源对象转走，源对象只留空壳
      Initialization of Constructor Arguments with std::move（.） ／用 std::move（.） 初始化构造实参 · p70
        · 实参用 std::move 转移进成员：data_｛std::move（data_in）｝
        · 外层对象借此独占子对象数据，省掉两次拷贝
      Anonymous Temporary Objects and Move Semantics ／匿名临时对象与移动语义 · p72
        · 匿名临时对象本身就是右值，无需再套 std::move
        · std::move（具名对象） 后原对象状态有效但不确定
      Return Value Optimization ／返回值优化 · p73
        · RVO 与 NRVO 让返回对象就地构造，不产生额外拷贝
        · C++17 起部分拷贝省略成为强制要求
      Default Constructor ／默认构造函数 · p74
        · 成员在声明处给初值：double x_｛0.0｝
        · Core Guidelines 建议字面量初值写进类内，各构造函数一致
        · C++11 起可用 = default 显式要求默认实现
      Three-Way Comparison Operator （Spaceship Operator） ／三路比较运算符（飞船运算符） · p76
        · operator<=> 一次定义即可生成 <、<=、>、>=
        · double 的 == 应按容差判等，不能直接比较
        · weak_ordering 表示大小写不敏感这类近似等价
      Lambda Expressions and User-Defined Class Members ／lambda 表达式与用户自定义类成员 · p80
        · lambda 捕获 【this】 即可访问全部成员变量与成员函数
        · 在成员函数里用 【this】（double x） 造局部函数对象
        · 配合范围 for 逐元素生成新容器
      …另 1 节
    Inheritance, Polymorphism, Smart Pointers ／继承、多态与智能指针 · p85 · 精读
      Polymorphism ／多态 · p87
        · 动态多态在运行时才确定类型，靠虚函数实现
        · 静态多态用模板，运行更快但编译更慢、写法更复杂
      Resource Ownership with Raw Pointers ／裸指针的资源所有权 · p92
        · 裸指针持有多态对象：构造时初始化、析构时释放
        · RAII 两条件：构造即得资源，随宿主析构而释放
      Using Clone Methods ／使用克隆方法 · p96
        · clone（） 里 new CallPayoff（*this） 把自身复制到堆上
        · 克隆法又叫虚构造函数，按动态类型复制对象
      Creating an Instance of OptionInfo ／创建 OptionInfo 实例 · p97
        · clone 返回的指针赋给 payoff_ptr_，由 owner 统一管理
        · payoff（） 用 std::max（spot - strike_, 0.0） 算看涨收益
      Preventing Shallow Copy ／防止浅拷贝 · p98
        · = delete 禁用拷贝构造与拷贝赋值，避免浅拷贝
        · 禁止拷贝后所有权不会出现两份，杜绝重复释放
      Implementing the OptionInfo Destructor ／实现 OptionInfo 析构函数 · p101
        · 自定义析构里 delete payoff_ptr_，把堆内存还给系统
        · 只用默认析构不会释放指针指向的内存，必然泄漏
      Pricing an Option ／期权定价 · p101
        · 先构造 payoff 与 OptionInfo，再交给定价模型算价
        · 移动操作也一并 = delete，所有权不随对象转移
      Implementing Copy Operations ／实现拷贝操作 · p103
        · 拷贝构造调用 clone 深拷贝，让每个对象独有资源
        · 先拷贝再 swap，异常时原对象保持原状（强异常保证）
      The （Old） Rule of Three ／（旧）三法则 · p107
        · 三法则：写了析构就要写拷贝构造与拷贝赋值
        · 三法则源于资源管理职责，是 C++11 前的标准做法
      Introducing Smart Pointers ／智能指针入门 · p107
        · unique_ptr 独占所有权，不能拷贝，只能 move 转移
        · Core Guidelines 建议用 unique_ptr/shared_ptr 取代裸指针
      Unique Pointers ／unique_ptr 指针 · p108
        · std::make_unique<T>（args） 构造独占指针，避免裸 new
        · reset（） 释放对象并置空，解引用空指针是未定义行为
      Shared Pointers ／shared_ptr 指针 · p110
        · shared_ptr 靠引用计数共享所有权，计数归零才释放
        · use_count（） 不能用来判断多线程下的安全性
      Managing Resources with Unique Pointers ／用 unique_ptr 管理资源 · p113
        · unique_ptr 成员不必自定义析构，默认析构自动释放
        · 资源寿命仍绑定 owner，RAII 的要求照样满足
      Just Move It ／移动即可 · p113
        · std::move 把 unique_ptr 交给新 owner，不花拷贝成本
        · make_unique 的临时对象直接 move 进成员，零额外开销
      …另 3 节
    STL I: Containers and Iterators ／STL I：容器与迭代器 · p125 · 选读
      Templates ／模板 · p126
        · 容器管存储、迭代器管遍历、算法管对数据的操作
        · 算法基于迭代器，写一次可通用于多种容器
      Using Function Templates ／使用函数模板 · p127
        · vector<T> 把元素类型作为模板参数传入
        · 同一模板既可放 double，也可放自定义类对象
      Compiling Template Code ／编译模板代码 · p131
        · 模板写在头文件，编译器按类型生成特化代码
        · 每种类型生成一份特化，二进制体积随之增加
      STL Containers ／STL 容器 · p132
        · 类模板可带多个类型参数：template <typename T, typename U>
        · std::map<K, V> 分别是键类型与值类型
        · 模板参数还可以是编译期整型常量
      Sequential Containers ／顺序容器 · p133
        · std::vector 是连续内存的动态数组，尾部增删最快
        · 顺序容器按位置访问，关联容器按键检索
      Associative Containers ／关联容器 · p150
        · std::set 自动排序，且元素唯一
        · std::map 的键唯一且有序，值可以重复
      STL Iterators ／STL 迭代器 · p156
        · 迭代器用法像指针：++iter 前进，*iter 取值
        · 普通指针也能直接传给标准库算法
      Using auto to Reduce Verbosity ／用 auto 简化冗长代码 · p159
        · auto pos = v.begin（） 省去写 std::vector<int>::iterator
        · 长类型名交给 auto，代码噪声大幅下降
      Using Constant Iterators ／使用常量迭代器 · p159
        · cbegin（）、cend（） 返回常量迭代器，禁止修改元素
        · 与 const 成员函数同理，默认就该加 const
      Iterators or Indices? ／迭代器还是下标？ · p159
        · 范围 for 建立在迭代器上而非下标，任何容器可用
        · 下标只在随机访问足够快时才有优势
      Iterators on Associative Containers ／关联容器上的迭代器 · p160
        · map 迭代器解引用得 pair：first 是键，second 是值
        · map 的键是 const 不能改，值可改：pos->second = 100.0
      Summary ／小结 · p161
        · 模板、容器、算法、迭代器构成 STL 的通用体系
        · 迭代器是容器与算法之间的统一接口
    STL II: Algorithms and Ranges ／STL II：算法与 ranges · p165 · 选读
      A First STL Algorithm Example ／首个 STL 算法示例 · p166
        · 谓词 is_odd 返回 bool，专门给算法筛选用
        · std::count_if 用谓词计数，替代手写循环
      A First Example with Ranges ／首个 ranges 示例 · p170
        · C++20 ranges 算法直接接收容器，不必写 begin（）、end（）
        · C++17 执行策略参数可让算法并行执行
      Some Commonly Used Algorithms ／一些常用算法 · p171
        · 部分算法还没有 ranges 版本，迭代器版仍需掌握
        · 并行执行策略暂不支持 ranges 形式
        · 第三方容器只认迭代器，两种写法要并存
      Function Objects as Auxiliary Functions ／函数对象作辅助函数 · p175
        · 有状态的 functor 把系数存成成员，operator（） 负责求值
        · 重载 operator（） 的对象可当辅助函数传给算法
      Class Member Functions as Auxiliary Functions ／类成员函数作辅助函数 · p175
        · 成员函数不能直接当算法参数，要用 lambda 包一层
        · 【&q】 捕获对象引用，调用 q.value（x） 复用其状态
      Locating, Sorting, Searching, Copying, and Moving Elements ／定位、排序、查找、拷贝与移动元素 · p176
        · std::move 算法把元素移入目标，源元素状态变为未定
        · std::ranges::move 提供范围版，写法更短
        · 拷贝或移动也可直接用容器的区间构造函数
      Numeric Algorithms ／数值算法 · p183
        · std::accumulate 一次遍历累加，可求总和与均值
        · adjacent_difference 求相邻元素差，适合算收益率
        · 数值算法在 <numeric>，与 <algorithm> 分开
      Range Views, Range Adaptors, and Functional Programming ／range 视图、适配器与函数式编程 · p191
        · std::log 是重载函数，直接传给算法会歧义，须用 lambda 包装
        · 视图是惰性的，不复制底层元素
      Chaining for Functional Composition ／函数式组合的链式调用 · p195
        · 用 | 串联 views::take、views::filter 等适配器
        · 链式组合把多步变换写成一条管道，惰性求值
      Views, Containers, and Range-Based for Loops ／视图、容器与基于范围的 for 循环 · p195
        · 视图可直接用于范围 for：for （auto x : w | views::take（5））
        · 要落地成容器就先 reserve，再 push_back
      Summary ／小结 · p196
        · 优先调用算法而不是手写循环，意图更清晰
        · ranges 与迭代器两种写法都要会用
    Random Numbers and Concurrency ／随机数与并发 · p199 · 精读
      Distributional Random Number Generation ／分布随机数生成 · p200
        · C++11 前须自写 Mersenne Twister 加 Box-Muller 变换
        · 标准库分布直接产出正态随机数，省去自研与测试
      Introducing Engines and Distributions ／引擎与分布入门 · p200
        · 随机数 = 引擎 + 分布：引擎出整数，分布转成目标分布
        · std::normal_distribution<> 的默认模板参数是 double
        · 引擎自带状态，连续调用得到不同序列
      Generating Random Normal Draws ／生成正态随机数 · p203
        · 引擎状态会前进，所以重复运行结果不同
        · uniform_real_distribution<>｛0.0, 1.0｝ 生成 【0,1） 均匀数
        · 固定种子即可复现同一条随机序列
      Using Other Distributions ／使用其他分布 · p204
        · 分布构造参数就是均值与标准差：｛0.25, 0.15｝
        · 不同标准库实现产生的随机序列并不相同
        · Student's t 分布适合厚尾的收益数据
      Shuffling ／洗牌 · p206
        · std::shuffle（v.begin（）, v.end（）, mt） 用引擎打乱顺序
        · random_shuffle 依赖 std::rand，C++17 已被移除
        · 现代引擎周期更长，且无全局可变状态
      Monte Carlo Option Pricing ／蒙特卡洛期权定价 · p216
        · 期权价 = 各路径到期收益贴现后的均值
        · 到期作废的路径也要计入，收益按 0 算
        · 通常需要两万到十万条路径才能收敛
      A Review of Monte Carlo Option Pricing ／蒙特卡洛期权定价回顾 · p216
        · 用少量路径示例演示：收益取均值再贴现
        · 路径越多，结果越逼近理论价格
      Generating Random Equity Price Scenarios ／生成随机股票价格情景 · p218
        · operator（） 生成一条价格路径 vector<double>
        · dt_ = time_to_expiration / num_time_steps 是步长
        · 构造用初始化列表给全部成员赋值
      Calculating the Option Price ／计算期权价格 · p220
        · GBM 步进含漂移 （r − q − σ²/2）dt 与 σ√dt·Z
        · 【this】 捕获成员，lambda 里取用 rf_rate_、volatility_
      Pricing Path-Dependent Options ／路径依赖期权定价 · p224
        · make_unique 的结果直接 std::move 进 OptionInfo
        · MCOptionValuation 构造后调用 calc_price 得价
        · 两万条路径、固定种子 42，便于复现
      Concurrency and Parallelism ／并发与并行 · p230
        · 蒙特卡洛各路径独立，是天然可并行的任务
        · std::async 与 future 按任务并行，代码改动很小
      Parallel Algorithms from the Standard Library ／标准库并行算法 · p231
        · 并行执行策略只是请求，实现可以不并行
        · 数据量小时并行反而可能比串行更慢
      Concluding Remarks on async and future ／async 与 future 结语 · p244
        · 无数据竞争时 async 加 future 简单又可靠
        · 省去手写线程管理的复杂度与出错风险
        · 社区对 future 在复杂场景的用法仍有争议
      Summary ／小结 · p244
        · 标准库随机数加任务并行，可显著提速蒙特卡洛
        · 现代 C++ 让蒙特卡洛代码更短也更安全
    Dates and Fixed Income ／日期与固定收益 · p247 · 选读
      Representation of a Date ／日期的表示 · p248
        · 日期用 std::chrono::year_month_day 表示
        · 日期计算服务于日计数、收益率曲线与债券定价
      Serial Representation ／序列化表示 · p251
        · sys_days 表示距 1970-01-01 的天数
        · 两日期相减再 count（） 即相隔天数（181 天）
      Accessor Functions for Year, Month, and Day ／年月日访问函数 · p252
        · ymd.year（） 等访问器返回 year、month、day 对象而非 int
        · 要整数须显式转换，如 static_cast<unsigned>
      Checking the Validity of a Date ／检查日期有效性 · p252
        · ymd.ok（） 校验年月日是否为合法组合
        · 负年份合法，2 月 31 日这类组合返回 false
      Checking Leap Years and Last Day of the Month ／检查闰年与月末日 · p253
        · year｛2024｝/month｛2｝/last 得月末日 2024-02-29
        · year_month_day_last 可隐式转成 year_month_day
      Identifying Weekdays and Weekends ／识别工作日与周末 · p254
        · weekday 由 sys_days 构造，iso_encoding（） 给 1 到 7
        · iso_encoding（） 大于等于 6 即周末，可判交易日
      Adding Years, Months, and Days ／加年、月与日 · p255
        · ymd + months｛6｝ 得半年后的日期，自动进位
        · 加天数可用 sys_days + days｛...｝，不必手算月末
      A Date Class Wrapper ／日期类包装器 · p258
        · 用类包装 year_month_day，把 chrono 细节藏进成员函数
        · 对外只暴露直观的构造、访问器与运算符
      Class Declaration ／类声明 · p258
        · 三个构造函数、访问器与比较运算符构成接口
        · private 的 date_ 在类内初始化到 1970-01-01
        · validate_（） 集中做日期合法性校验
      Class Implementation ／类实现 · p261
        · 实现只是把前文的 chrono 计算包进成员函数
        · operator<=> 让 <、<=、>、>= 一次到位
      Day Count Basis ／日计数基准 · p268
        · 日计数基准把日期差换成以年为单位的时间 t
        · 利率三要素：年化值、单复利类型、日计数基准
        · 同一笔利息因基准不同而不同，如 Act/365
      Yield Curves ／收益率曲线 · p271
        · 收益率曲线由一组固定利率产品的市场收益率拟合
        · 同一结算日、不同到期日构成曲线节点
      Deriving a Yield Curve from Market Data ／由市场数据推导收益率曲线 · p271
        · treasury_bill 用 DayCount& 多态参数支持不同基准
        · 国库券价 = 面值 / （1 + 收益率 × 年分数）
      Discount Factors ／贴现因子 · p274
        · 贴现因子 P（s,m） = exp（−t·y（t）），t 按 Act/365 算
        · 由即期收益率直接得到即期贴现因子
      …另 9 节
    Linear Algebra ／线性代数 · p299 · 精读
      Lazy Evaluation and Expression Templates ／惰性求值与表达式模板 · p300
        · 表达式模板把 a+b+c 合成一次循环，省掉临时对象
        · 惰性求值推迟到赋值时才真正计算
        · VectorAddExpr 需转换运算符才能赋给 vector<double>
      The Eigen Linear Algebra Library ／Eigen 线性代数库 · p308
        · Eigen 用惰性求值与表达式模板换取高性能
        · 被 TensorFlow、Stan、CERN ATLAS 等采用
      Eigen Matrices and Vectors ／Eigen 矩阵与向量 · p309
        · VectorXd 是动态长度向量，MatrixXd 是矩阵
        · 圆括号既是访问器也是修改器：vec_04（0） = 3.19
        · 用 << 逗号初始化：vec << 10.0, 12.0, 14.0
      Matrix and Vector Math Operations ／矩阵与向量运算 · p313
        · 向量相减直接写 v - u，结果仍是 VectorXd
        · 矩阵乘法与转置几乎按数学公式直接表达
      STL Compatibility ／STL 兼容性 · p319
        · Eigen 容器可迭代，STL 算法能直接作用其上
        · 可与 std::vector 互传数据，便于衔接已有代码
      Matrix Decompositions and Applications ／矩阵分解与应用 · p325
        · 矩阵分解是回归、相关性等金融问题的常用工具
        · Eigen 提供 QR 与 SVD，应对秩亏与数值稳定性
      Fund Tracking with Multiple Regression ／用多元回归跟踪基金 · p325
        · 多元回归把基金收益分解到各因子的暴露上
        · 最小二乘可用 QR 或 SVD 求解，比正规方程稳健
      Correlated Random Equity Paths and the Cholesky Decomposition ／相关随机股价路径与 Cholesky 分解 · p328
        · Cholesky 分解把独立随机数变成相关的股价路径
        · 协方差矩阵须正半定，特征值才都是实数
        · selfadjointView<Eigen::Upper> 只取上三角即可分解
      Future Directions: Linear Algebra in the Standard Library ／未来方向：标准库线性代数 · p335
        · 标准化方向之一是 mdspan 提供多维数组视图
        · 方向之二是基于 BLAS 的 std::linalg 接口
      mdspan ／mdspan · p336
        · mdspan 是数组的非拥有视图，可表示二维矩阵
        · C++23 才有 【i, j】 多下标，之前写成 （i, j）
      BLAS Interface ／BLAS 接口 · p341
        · P1673 按 BLAS 语义提供 scale、dot、matrix_product 等
        · 目前位于 std::experimental，接口风格贴近 STL
      Summary ／小结 · p343
        · 现状用 Eigen，未来交给 mdspan 与 std::linalg
        · BLAS 函数与 std::linalg 名称几乎一一对应
    The Boost Libraries ／Boost 库 · p345 · 选读
      Mathematical Constants ／数学常量 · p346
        · Boost 常是新标准特性的试验田：智能指针、future 等
        · Math Toolkit 多为 header-only，常量与特殊函数现成可用
      Statistical Distributions ／统计分布 · p347
        · boost::math::double_constants 提供 1/√（2π） 等常量
        · 标准正态 PDF：φ（x） = （1/√（2π））·exp（−x²/2）
      Probability Functions ／概率函数 · p348
        · Boost 分布提供 PDF、CDF、分位数与补函数
        · 标准库 distribution 只用于生成随机数，不做确定性计算
      Drawdown Example, Revisited ／回撤示例再探 · p350
        · 不再硬编码 Z0.95 = 1.64485，改用 quantile 求分位点
        · 先由最大回撤样本估均值方差，再算置信上限
      Random Number Generation with Boost Distributions ／用 Boost 分布生成随机数 · p351
        · 34 个 Boost 分布也能配合引擎直接生成随机数
        · 调用 quantile 前应先检查参数的边界
      MultiArray ／MultiArray · p353
        · boost::multi_array 是高效的多维数组类模板
        · 接口按标准库风格设计，可当作泛型容器使用
      A Simple Two-Dimensional MultiArray ／简单的二维 MultiArray · p353
        · boost::multi_array<double, 2> 配 extents【行】【列】 定维
        · 元素用 ma【i】【j】 双层下标访问
      Binomial Lattice Option Pricing ／二叉树期权定价 · p355
        · struct Node 存 underlying 与 payoff，作数组元素
        · 先正向生成价格，再倒推各节点收益
        · 美式期权取相邻两步均值可减小振荡误差
      Accumulators ／累加器 · p368
        · 累加器边喂数据边更新统计量，一次遍历算多项
        · 适合流式行情，无需先缓存全部样本
      Max and Min Example ／最大值与最小值示例 · p368
        · max、min 累加器可与其他统计量放进同一个 set
        · 实时监控极值类指标（如最大回撤）时很方便
      Mean and Variance ／均值与方差 · p370
        · accumulator_set 的 stats<> 列出要算的统计量
        · 喂数据用 mv_acc（1.0），取值用 accumulators::extract
        · mean、variance 需分别 include 各自头文件
      Rolling Mean and Variance ／滚动均值与方差 · p371
        · rolling_window 指定窗口，只统计最近 N 条数据
        · 滚动方差算的是样本方差，与总体方差不同
        · 移动平均类指标用滚动累加器最省事
      Trading Indicator Examples ／交易指标示例 · p372
        · 布林带中轨是滚动均值，上下轨是 ±k 倍滚动标准差
        · 滚动频率可从秒级到月级，按策略选择
      Summary ／小结 · p377
        · Boost 是 C++ 标准的试验田，多项新特性源自这里
        · 统计分布与累加器补上标准库在分析上的空白
    Modules and Concepts ／模块与 concepts · p379 · 快读
      Modules ／模块 · p380
        · 模块可在单文件里同时写声明与实现，用 export 暴露
        · import 取代 ＃include，避免重复解析头文件
      Standard Library Header Units ／标准库头单元 · p382
        · import <vector>; 导入标准库头单元，末尾要分号
        · 未 export 的内部函数在模块外不可见
        · <cmath> 等源自 C 的头文件暂不宜做头单元
      Templates in Modules ／模块中的模板 · p383
        · 模板也要 export，否则模块外无法实例化
        · export 写在 template 之前，整体导出模板
      import Versus ＃include ／import 与 ＃include 对比 · p384
        · module; 开全局模块片段，其中只能放 ＃include
        · Boost、Eigen 等外部库目前只能 ＃include 引入
      Declarations in Module Interfaces ／模块接口中的声明 · p386
        · export import 把导入的模块再导出，使用者无需二次导入
        · 模块接口只暴露 export 出去的名字
      Separating Declarations from Implementation ／声明与实现分离 · p387
        · 模块接口预编译一次，消除重复解析，构建更快
        · 预编译头依赖平台，模块则是标准做法
        · 模块会削弱构建并行度，提速并非绝对
      Namespaces ／命名空间 · p391
        · export namespace 一次导出整个命名空间
        · 也可只导出个别类或函数，控制可见范围
      Partitions ／分区 · p392
        · 实现分区仅供模块内部使用，不能导出名字
        · 接口分区可 export，但须由主接口再 export import
      Concepts ／concepts · p392
        · concept 用 requires 表达式声明类型必须支持的操作
        · concepts 把冗长模板报错压成一句约束不满足
      Defining Concepts ／定义 concepts · p394
        · template<can_square T> 把 concept 直接写进模板参数
        · 不满足约束时报 constraints not satisfied
      Defining Concepts with Multiple Conditions ／定义含多个条件的 concepts · p395
        · 多个 concept 用 && 组合成复合约束
        · requires 子句也可以写在函数模板的尾部
      Standard Library Concepts ／标准库 concepts · p396
        · 标准库预置 integral、floating_point 等常用 concepts
        · 复用标准 concepts 比自己写更统一
    Appendix A–E ／附录 A–E · p399 · 参考
```