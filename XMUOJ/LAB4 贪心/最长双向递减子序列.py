"""
8
8 8 5 10 6 3 9 12

最少需要移除几个数字, 使剩余的数字构成一个最长的双向递减子序列(先递增后递减序列);
(允许递增或递减的部分为空);
(允许非严格递增或递减, 即允许相邻数字相等)

输出:
4

解释: 保留 [5,10,6,3] 构成一个最长的双调子序列, 长度为 4, 需要移除 8-4=4 个数字。
"""

# 思路: 取第 i 个数字作为峰值, 计算以第 i 个数字为峰值的最长双调子序列长度;
# 先计算以 a[i] 为结尾的最长递增子序列长度 up[i]; 
# 再计算以 a[i] 为开头的最长递减子序列长度 dn[i];
# 再遍历所有的 i, 计算 up[i] + dn[i] - 1 的最大值, 即为最长双调子序列长度;


n = int(input())
a = list(map(int, input().split()))

up = [1] * n
dn = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[i] >= a[j]:
            up[i] = max(up[i], up[j] + 1)
print(up)  # 输出 up 数组的值
for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if a[i] >= a[j]:
            dn[i] = max(dn[i], dn[j] + 1)
print(dn)  # 输出 dn 数组的值

max_length = 0
for i in range(n):
    max_length = max(max_length, up[i] + dn[i] - 1)

print(n - max_length)  # 输出需要移除的数字个数