# 最大流问题

# 输入
# 5 4
# 1 2 40
# 1 4 20
# 2 4 20
# 2 3 30
# 3 4 10

# 第1行: M N。M是边的数量, N是点的数量。其中点1是生产地, 点N是目的地。
# 后续 M 行每行三个整数: si ei ci。 表示起点,终点,运输量。

# 输出最大运输量
# 50

# 导入队列，用于广度优先搜索
from collections import deque

def solve(M, N, edges):
    """
    :param M: 边数
    :param N: 点数
    :param edges: 边表，格式为 [(s1, e1, c1), (s2, e2, c2), ...]
    """
    SOURCE = 1
    DESTIN = N
    
    # 1. 构建易索引的图结构
    # 邻接矩阵: 加速访问边数据
    capacity = [[0] * (N + 1) for _ in range(N + 1)]
    # 邻接表: 加速查找邻节点
    adj = [[] for _ in range(N + 1)]
    # 初始化图结构
    for s, e, c in edges:
        capacity[s][e] = c
        adj[s].append(e)
        adj[e].append(s)  # 添加反向边以支持残量网络


    # 2. BFS寻找一条从源点到汇点的通路
    def bfs(path):
        # path 初始化为 [-1, -1, -1, -1, -1]
        for i in range(len(path)):
            path[i] = -1

        # 标记源点已访问
        path[SOURCE] = -2
        
        # 队列中存储 (当前节点, 当前流量)，初始为 (SOURCE, ∞)
        queue = deque([(SOURCE, float('inf'))])

        while queue:
            i, flow = queue.popleft()
            for nxt in adj[i]:
                if path[nxt] == -1 and capacity[i][nxt] > 0:
                    path[nxt] = i
                    new_flow = min(flow, capacity[i][nxt])
                    if nxt == DESTIN:
                        return new_flow
                    queue.append((nxt, new_flow))
        return 0


    # 3. 循环增广直到无法产生新流量
    max_flow = 0
    path = [-1] * (N + 1)  # path[i] 记录 i 节点的来源节点
    
    while True:
        flow = bfs(path)
        if flow == 0:
            break
        max_flow += flow
        
        # 沿增广路更新残量网络
        i = DESTIN
        while i != SOURCE:
            prev = path[i]
            capacity[prev][i] -= flow
            capacity[i][prev] += flow
            i = prev
            
    return max_flow


def test():
    M = 5
    N = 4
    edges = [(1, 2, 40),
            (1, 4, 20),
            (2, 4, 20),
            (2, 3, 30),
            (3, 4, 10)]
    print(solve(M, N, edges)) # 50


if __name__ == '__main__':

    #test()
    
    M, N = map(int, input().split())
    edges = []
    for _ in range(M):
        s, e, c = map(int, input().split())
        edges.append((s, e, c))
        
    print(solve(M, N, edges))