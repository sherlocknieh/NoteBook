"""描述

给定一个 n 个点 m 条边的有向图，图中可能存在重边和自环，边权可能为负数。

再给定 k 个询问，每个询问包含两个整数 x 和 y，表示查询从点 x 到点 y 的最短距离，如果路径不存在，则输出 impossible。

数据保证图中不存在负权回路。

数据范围

1≤n≤200,

1≤k≤n^2,

1≤m≤20000,

图中涉及边长绝对值均不超过 10000。


输入

第一行包含三个整数 n, m, k。

接下来 m 行，每行包含三个整数 x, y, z，表示存在一条从点 x 到点 y 的有向边，边长为 z。

接下来 k 行，每行包含两个整数 x, y，表示询问点 x 到点 y 的最短距离。


输出

共 k 行，每行输出一个整数，表示询问的结果，若询问两点间不存在路径，则输出 impossible。


输入样例:
3 3 2
1 2 1
2 3 2
1 3 1
2 1
1 3

输出样例:
impossible
1
"""
import sys
input = sys.stdin.read().splitlines()

INF = float('inf')

n, m, k = map(int, input[0].split())

# 构建容器
dist = [[INF]*n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
    print(dist[i])

# 输入数据
for _ in range(m):
    u,v,d = map(int, input[_ + 1].split())
    dist[u-1][v-1] = min(dist[u-1][v-1], d)  # 处理重边，取最小值


for i in range(n):
    print(dist[i])

# 计算最短路径
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(n):
    print(dist[i])

# 查询与输出
for _ in range(k):
    u, v = map(int, input[_ + 1 + m].split())
    d = dist[u-1][v-1]
    if d == INF:
        print('impossible')
    else:
        print(d)