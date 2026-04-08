# 矩阵链乘法问题

# 输入
# 6
# 30 35
# 35 15
# 15 5
# 5 10
# 10 20
# 20 25

# 第一行输入矩阵的总个数n
# 后n行是每个矩阵的行列维数

# 输出少乘法次数
# 15125

# 动态规划算法, A 是矩阵链的维数表, n 是矩阵链的长度
def matrix_chain_order(A, n):
    memo = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            for k in range(i, j):
                q = memo[i][k] + memo[k+1][j] + A[i][0] * A[k][1] * A[j][1]
                if memo[i][j] == 0 or q < memo[i][j]:
                    memo[i][j] = q
    return memo[0][n-1]

def test():
    n = 6
    A = [[30, 35], [35, 15], [15, 5], [5, 10], [10, 20], [20, 25]]
    print(matrix_chain_order(A, n))
test()

if __name__ == "__main__":

    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]
    print(matrix_chain_order(A, n))