# 选课问题 (二分图最大匹配问题)

# 输入
# 7 4 4
# 1 1
# 1 2
# 1 3
# 2 1
# 2 4
# 3 1
# 4 2
# 3 3 3
# 1 2
# 2 1
# 3 3


# 每个样例第一行是三个整数 k,m,n (0<k<=1000,1<=m,n<=500)
# k 表示选课数据的行数
# m 表示学生的数量
# n 表示课程数量
# 接下来包含 k 行，每行有两个数，表示学生 ai 愿意选择课程 bi。

# 每门课只接收一个学生，且每个学生只能进入一门课。

# 每行输出一个整数，表示最多能使多少学生选到心仪的课程。
# 4
# 3


def main():
    try:
        while True:
            k, m, n = map(int, input().split())

            # 建立邻接表，下标从 1 到 m 对应左侧点
            graph = [[] for _ in range(m + 1)]

            for _ in range(k):
                u, v = map(int, input().split())
                # 过滤掉越界数据，避免污染匹配图
                if 1 <= u <= m and 1 <= v <= n:
                    graph[u].append(v)

            # match[v] 表示右侧点 v 当前匹配到的左侧点，-1 表示未匹配
            match = [-1] * (n + 1)

            def dfs(u):
                for v in graph[u]:
                    if visited[v]:
                        continue
                    visited[v] = True
                    if match[v] == -1 or dfs(match[v]):
                        match[v] = u
                        return True
                return False

            max_match = 0
            for u in range(1, m + 1):
                visited = [False] * (n + 1)
                if dfs(u):
                    max_match += 1

            print(max_match)
    except EOFError:
        return

if __name__ == '__main__':
    main()