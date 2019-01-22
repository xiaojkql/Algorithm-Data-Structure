# Sort and Search

计算机程序 = 算法 + 数据结构

算法：描述了解决一个问题计算过程

评价算法好坏的标准：正确性，可读性，易维护性、时间性能、空间性能。

复杂性分析的工具：评估算法的运行时间性能和效率。

### 1 评估算法的性能

选择算法：解决时间和空间的平衡问题。

#### 1.1 度量算法的运行时间

基准评价、探查。

[示例代码]()

能够较精确的预测很多算法运行时间。但存在一些缺陷：

- 在不同硬件的机器平台上处理时间是不一样的。
- 不同语言实现的算法也是不一样的。
- 对于很大的数据集确定时间是不切实际的。

建立独立与特定的硬件与软件平台的评估方法。

#### 1.2 统计指令

两种指令：

- 随着问题规模变化的指令。
- 与问题规模无关的指令。

示例：[Fibonacci数列]()

算法指令的增长率。

#### 1.3 度量算法所使用的内存

实际的使用率，以及增长率。

### 2 复杂度分析

一种方法来评价算法的性能，摆脱时间统计和指令统计。

#### 2.1 复杂度的阶

算法的性能是通过复杂度的阶（或级）来区分的。

常数阶，对数阶，线性阶，，二次方阶，多项式阶，指数阶。

较高复杂度阶的算法会随着问题的规模增大变得越来越糟糕。

#### 2.2 大O表示法

#### 2.3 常量比列的作用

与问题规模的增长的速率是相同额。

### 3 搜索算法

#### 3.1 搜索最小值

复杂度：O(n)

#### 3.2 线性搜索、顺序搜索

python中in运算符实际上是调用python类中__contains  方法

最好情况：O(1)

最坏情况：O(n)

平均情况：O(n)

#### 3.3 二分搜索

复杂度：$$O(logn)$$

### 4 比较数据项

$${\_\_}eq{\_\_}$$表示相等

$$\_\_lt\_\_$$表示小于

$$\_\_lte\_\_$$表示小于等于

$$\_\_gt\_\_$$表示大于

$$\_\_gte\_\_$$表示大于等于
