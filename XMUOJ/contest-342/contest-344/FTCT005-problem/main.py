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

# 第一行是三个整数 k,m,n
# k 表示选课数据的行数
# m 表示学生的数量
# n 表示课程数量
# 接下来包含 k 行，每行有两个数，表示学生 ai 愿意选择课程 bi。

# 每门课只接收一个学生，且每个学生只能进入一门课。

# 输出一个整数，表示最多能使多少学生选到心仪的课程。
# 4


def solve(a, k, m, n):
    print('a:', a)
    print('k:', k)
    print('m:', m)
    print('n:', n)

def test():
    k, m, n = 7, 4, 4
    a = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (4, 2)]
    solve(a, k, m, n)

if __name__ == "__main__":
    test()
    k,m,n = map(int,input().split())
    a = []
    for _ in range(k):
        ai, bi = map(int,input().split())
        a.append((ai, bi))
    solve(a,k,m,n)