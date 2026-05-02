# 校园巡检（普通版）

# 输入:
# 4 3
# 1 2 3
# 2 3 4
# 3 4 5

# 第一行输入两个整数 n, m，分别表示区域数和道路数。
# 接下来 m 行，每行输入三个整数 u, v, w，表示区域 u 和区域 v 之间有一条长度为 w 的双向道路。

# 输出:
# 12

# 输出一个整数，表示从 1 号区域出发，任何区域至少被经过一次的最短总时间。
# 如果无法经过所有区域，输出 -1。



def algorithm(edges):
    return 0

def test():
    edges = [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
    print(algorithm(edges))

def main():
    n,m = map(int, input().split())
    edges = []
    for _ in range(m):
        u,v,w = map(int, input().split())
        edges.append((u,v,w))
    print(algorithm(edges))

if __name__ == '__main__':
    test()
    main()