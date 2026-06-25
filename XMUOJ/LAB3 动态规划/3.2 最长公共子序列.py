# 最长公共子序列

# 输入:
# 4 5
# acbd
# abedc

# 输出:
# 3

def F(A,m,B,n):
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]


def test():
    m,n = (4,5)
    A = 'abcd'
    B = 'abedc'
    print(F(A,m,B,n))
test()

if __name__ == "__main__":
    m,n = map(int, input().split())
    A = input()
    B = input()
    print(F(A,m,B,n))