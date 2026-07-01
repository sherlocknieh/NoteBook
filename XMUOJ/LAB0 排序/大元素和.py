"""
输入:
n
a[n]
输出:
b[n]

b[i] 表示 a 中所有比 a[i] 大的数的和(严格大于 a[i])，如果没有比 a[i] 大的数，则 b[i] = 0。

样例1:
5
2 3 3 4 4
输出
14 8 8 0 0

样例2:
10
31 42 59 26 53 58 97 93 23 54
输出
456 414 190 487 361 249 0 97 513 307
"""

# 思路:
# 1.带索引降序排序数组a
# 2.计算前缀和
# 3.处理重复元素


def solve(n, a):
    # 将每个元素与其原始索引一起存储
    a = [(a[i], i) for i in range(n)]   # O(n)
    # 按照数值从大到小（降序）排序
    a = sorted(a, reverse=True)         # O(n log n)
    
    # 初始化答案数组
    b = [0] * n
    
    # 计算前缀和
    prefix_sum = 0
    for i in range(n):                  # O(n)
        val, idx = a[i]
        b[idx] = prefix_sum
        prefix_sum += val
        if i>0 and a[i][0] == a[i-1][0]:
            # 如果当前元素与前一个元素相同，则不更新前缀和
            b[idx] = b[a[i-1][1]]

    # 输出结果，以空格分隔
    print(*(b))

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    solve(n, a)