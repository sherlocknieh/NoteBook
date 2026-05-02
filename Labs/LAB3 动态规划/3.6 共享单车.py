# 共享单车

# 输入:
# 10 2
# 1 0 0 0 5 4 0 1 2 0
# 1 5
# 2 7
# 2

# 第一行为 n(天数), k(骑行卡的种类数)。
# 接下来一行有 n 个整数，表示从第 1 天至第 n 天，每天使用共享单车的次数 di。
# 接下来 K 行，每行 2 个整数，表示 ti (骑行卡的有效期)和 ci (骑行卡的价格)。
# 接最后一行表示单次使用的价格 P0

# 输出最小花费:
# 15


# 第1天,单次付费，花费2元。
# 第5、6天，购买两天的骑行卡，花费7元。
# 第8天，单次付费，花费2元。
# 第9天，单次付费，花费4元。


def algorithm(n, times, tickets, P0):
    # 分析:
    # 每天有1+k种选择: 不买骑行卡, 买第i种骑行卡
    # 从最后一天开始考虑
    dp = [0] * n
    for i in range(n-1,-1,-1):
        # 默认方案
        dp[i] = P0 * times[i] + (dp[i+1] if i < n-1 else 0)
        # 买卡方案
        for T in tickets:
            temp = 0
            index = i+T[0]
            if index < n:
                temp = dp[i+T[0]]
            if dp[i] > T[1] + temp:
                dp[i] = T[1] + temp
    return dp[0]


def test():
    print(algorithm(10, [1, 0, 0, 0, 5, 4, 0, 1, 2, 0], [(2, 7), (3, 10)], 2))


def main():
    n, k = map(int, input().split())
    times = list(map(int, input().split()))
    tickets = []
    for _ in range(k):
        t, c = map(int, input().split())
        tickets.append((t, c))
    P0 = int(input())

    print(algorithm(n, times, tickets, P0))


if __name__ == '__main__':
    test()
    main()