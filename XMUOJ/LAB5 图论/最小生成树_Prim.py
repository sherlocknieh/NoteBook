"""
input:
4
0 4 9 21
4 0 8 17
9 8 0 16
21 17 16 0

output:
28
"""


# 读取所有输入
import sys, heapq
data = sys.stdin.read().splitlines()

n = int(data[0])
G = []
for i in range(n):
    row = list(map(int, data[i + 1].split()))
    G.append(row)

visited = [0] * n
min_heap = [(0, 0)]  # (边权, 目标节点)
min_weight = 0

while min_heap:
    weight, u = heapq.heappop(min_heap)
    if visited[u]:
        continue
    visited[u] = 1
    min_weight += weight

    for v in range(n):
        if not visited[v] and G[u][v] != 0:
            heapq.heappush(min_heap, (G[u][v], v))
    if sum(visited) == n:
        break

print(min_weight)  # 输出最小生成树的总权重