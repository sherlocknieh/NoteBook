"""
有 n 个人排队在超时收银台结账;
由于每个人买的东西数量不同, 结账所需的时间也不同;
每个人结账所需的时间为 t[i], 1 <= i <= n;

输入: 
7
3 6 1 4 2 5 7

调整队列顺序, 使得所有人的平均等待时间最少;
输出最少的总等待时间:
56
"""

# 思路: 先将 t[i] 升序排序, 最短的时间排在最前面, 最长的时间排在最后面;

n = int(input())
t = list(map(int, input().split()))
t = sorted(t)

wait_time = [0] * n
for i in range(1, n):
    wait_time[i] = wait_time[i - 1] + t[i - 1]

total_wait_time = sum(wait_time)
print(total_wait_time)