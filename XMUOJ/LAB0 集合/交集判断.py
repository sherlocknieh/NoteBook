"""输入格式:
n m
A1 A2 ... An
b1 b2 ... bm

含义:
n 为 A 的长度, m 为 b 的长度, m < n;
A 是一个数组, b 是一组下标, 表示 A 的一个子集; (下标从 1 开始计数)
如果 A 中最大值对应的下标出现在 b 中，则输出 Yes，否则输出 No。

输入:
5 3
6 8 10 7 10
1 2 3

输出:
Yes

解释:
A 中最大值为 10, 对应的下标为 3 和 5
b 中包含下标 3, 所以输出 Yes。
"""

# 思路:
# 1. 找到 A 中所有的最大值并提取其下标到列表 a 中 (需要两遍扫描, 第一遍获取最大值, 第二遍获取所有下标)
# 2. 扫描列表 a 检查这些下标是否出现在 b 中(或者扫描 b 检查这些下标是否出现在 a 中)

n, m = map(int, input().split())
A = list(map(int, input().split()))
b = list(map(int, input().split()))

def solve(n, m, A, b):
    max_value = max(A)      # O(n)
    a = [i+1 for i in range(n) if A[i] == max_value]  # O(n)

    for idx in a:           # O(k)次循环, 0 < k <= n，取决于 A 中最大值的数量
        if idx in b:        # O(m)
            print("Yes")
            break
    else:
        print("No")

# 时间复杂度: O(km), 最坏情况下 k = n 时间复杂度为 O(nm)

# 优化思路:
# 一:把 b 转换为集合，对 a 进行扫描, 时间复杂度为 O(k)，其中 k 为 A 中最大值的数量，0 < k <= n;
# 二:把 a 转换为集合，对 b 进行扫描, 时间复杂度为 O(m);

# [6, 8, 10, 7, 10] 最大值 10, 对应下标为 3 和 5, 列表 [3,5] 的快查集为 [0, 0, 0, 1, 0, 1];
# [6, 8, 10, 7, 10] 本身就能做一个快查集, 故只需扫描 b, 如果 b[i] == 10, 则输出 Yes, 否则输出 No。

# 最终优化代码如下:

def solve(n, m, A, b):
    max_value = max(A)  # O(n)
    for idx in b:       # O(m)
        if A[idx - 1] == max_value:  # 下标从 1 开始计数, 所以 A[idx - 1]
            print("Yes")
            break
    else:
        print("No")