# NP完全问题


#### 1 

定义判定问题: $\text{ExistsPath} = \{ \langle G, u, v, k \rangle \mid G=(V,E) \text{ 是一个无向图}, u,v \in V, k \in \mathbb{N}, \text{且 } G \text{中存在一条从 } u \text{到 } v \text{长度}\ge k\text{ 的简单路径} \}$

定义优化问题: $\text{LongestPath}(\langle G, u, v \rangle) = \max \{ |P|:  P \text{ 是 } G \text{ 中从 } u \text{ 到 } v \text{ 的简单路径} \}$

证明两个问题的难度是多项式等价的。

##### 解释:

> 判定问题只需用集合来定义:
> - `ExistsPath = { ... }` 定义了一个名为 ExistsPath 的语言集合;
> - `<G, u, v>` 表示图和顶点数据的字符串编码;
> - `|`或 `:` 后面是筛选条件，描述了哪些字符串属于这个集合;
>
>优化问题需要用函数来定义:
>
> - $\text{LongestPath}(\langle G, u, v \rangle)$ 定义了一个函数，输入是图和顶点数据的编码，输出是从 u 到 v 的最长简单路径的长度。

##### 解答:

1.证明 $\text{ExistsPath} \leq_P \text{LongestPath}$:

```python
def ExistsPath(G, u, v, k):
    l = LongestPath(G, u, v)
    return l >= k
```

显然 $\text{ExistsPath} = \text{LongestPath} * O(1)$

2.证明 $\text{LongestPath} \leq_P \text{ExistsPath}$:
```python
def LongestPath(G, u, v):
    low = 0
    high = len(G.nodes) - 1
    while low <= high:
        mid = (low + high) // 2
        if ExistsPath(G, u, v, mid):
            low = mid + 1
        else:
            high = mid - 1
    return low
```
显然 $\text{LongestPath} = \text{ExistsPath} * O(\log n)$

故: $\text{ExistsPath} =_P \text{LongestPath}$;



#### 7

证明如果 HamCycle ∈ P，则按顺序列出一个汉密尔顿回路中各个顶点的问题是多项式时间可解的。

##### 答:

>假设存在一个多项式时间算法 HamCycle(G) 来判断一个图 G 是否存在汉密尔顿回路。可以使用删边法获得一个汉密尔顿回路图：

```python
def find_hamiltonian_cycle(G):
    if not HamCycle(G):
        return None  # 没有汉密尔顿回路
    
    cycle = []
    edges = list(G.edges())
    
    for u, v in edges:
        G.remove_edge(u, v)  # 尝试删除边
        if not HamCycle(G):  # 判断删除后是否仍有回路 
        #O(n^p) * E < O(n^p) * n^2 = O(n^(p+2))
            cycle.append((u, v)) # 该边是回路的一部分
            G.add_edge(u, v)     # 恢复边
    
    return cycle  # 返回回路边列表

    # 之后可以遍历 cycle 中的边构建回路图 O(n)
    # 再遍历回路图得到回路顶点顺序 O(n)
```

#### 16

已知一个 m×n 整数矩阵 A 和一个 m 维整数向量 b，0/1 整数规划问题是：是否存在其元素属于集合 {0,1} 的 n 维整数向量 x，使得 Ax ≤ b。证明 0/1 整数规划问题是 NP 完全的。

##### 答:

1. 证明 0/1 整数规划问题属于 NP

> 即证明存在一个多项式时间的验证算法来验证一个给定的解是否满足 0/1 整数规划问题的约束条件。

> 候选解（Certificate）：一个 $n$ 维的整数向量 $x = (x_1, x_2, \dots, x_n)^T$。

> 验证算法（Verification Algorithm）：

> 检查 $x$ 中的每个元素 $x_i$ 是否都在 $\{0, 1\}$ 集合中。需要检查 $n$ 次。

> 计算矩阵与向量的乘积 $A \cdot x$，并验证是否满足每一行 $i$ 都有 $(Ax)_i \le b_i$。

> 复杂度分析：矩阵乘法 $A_{m \times n} \times x_{n \times 1}$ 的计算需要进行 $m \times n$ 次乘法和加法。验证所有的不等式需要 $m$ 次比较。这些操作的总时间复杂度为 $O(m \cdot n)$，显然在输入规模的多项式时间内。因此，0/1 整数规划问题属于 NP。

2. 证明 0/1 整数规划问题是 NP 完全的

> 即证明能用整数规划问题来解 3-CNF-SAT 问题;
> 3-CNF-SAT 问题：给定一个布尔公式，判断是否存在一个变量赋值使得公式为真。公式由若干子句组成，每个子句是三个字面（变量或其否定）的析取。


