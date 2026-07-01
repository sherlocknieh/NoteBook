"""



input:
5
0 2 4 5 1
2 0 6 5 3
4 6 0 8 3
5 5 8 0 5
1 3 3 5 0

input 第1行: 节点数 n (1<=n<=8)
旅行商问题(TSP), 但是固定起点=0和终点=n-1, 经过每个节点恰好一次, 求最短路径长度;

output:
18
"""



def solve(n,dist):
    # n:    节点数 (节点 id 范围在 0 到 n-1)
    # dist: 距离矩阵 (dist[u][v] = 节点u到v的距离)

    SOURCE = 0              # 固定起点为 0
    TARGET = n - 1          # 固定终点为 n-1

    min_dist = float('inf')             # 初始化最短路径长度为无穷大
    visited  = set([SOURCE,TARGET])     # 记录已经访问过的节点

    def dfs(u, current_dist, city_remain):
        # u:            当前节点
        # current_dist: 当前路径长度
        # city_remain:  剩余未访问的节点数

        nonlocal min_dist
        if city_remain == 0:  # 如果没有剩余未访问的节点
            current_dist += dist[u][TARGET]         # 加上从当前节点到终点
            min_dist = min(min_dist, current_dist)  # 更新最短路径长度
            return
        
        for i in range(1, n-1):  # 遍历所有节点，除了起点和终点
            if i in visited: continue
            if current_dist + dist[u][i] >= min_dist:
                continue    # 剪枝：如果当前路径已经比已知最短路径长，则不再继续

            visited.add(i)
            dfs(i, current_dist + dist[u][i], city_remain - 1)
            visited.remove(i)    # 回溯，移除当前节点，尝试剩余路径

    # 从起点0开始DFS
    dfs(SOURCE, 0, n - 2)  # n - 2: 剩余未访问的节点数（不包括起点和终点）

    return min_dist  # 返回最短路径长度




if __name__ == '__main__':
    # 输入
    import sys
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    dist = []
    for i in range(n):
        row = list(map(int, data[i + 1].split()))
        dist.append(row)

    # 输出
    print(solve(n,dist))