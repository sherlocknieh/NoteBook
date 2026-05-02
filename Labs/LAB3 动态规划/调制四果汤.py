# 调制四果汤（原型：最小费用覆盖特征集合）

# 在覆盖全部 n 个目标特征的前提下，使总花费最小。

# 输入:
# 4 3
# 5 C
# 6 B
# 16 BAC
# 4 A

# 第一行两个整数 T, n
# T 表示配料数量
# n = 3 表示必需配料为 A、B、C。
# 接下来 T 行，每行包含 w:价格 s:包含的配料


# 输出:
# 15
#选择第 1、2、4 种配料，总价 5 + 6 + 4 = 15，优于买第 3 种配料。


# 输入:
# 1 2
# 10 A

# 输出:
# -1

# n = 2 表示必需配料为 A、B;
# 商店只有含 A 的配料，无法满足要求，输出 -1.


def algorithm(T, n, ingredients):
    dp = [float('inf')] * (1 << n)
    dp[0] = 0
    for w, s in ingredients:
        mask = 0
        for c in s:
            mask |= 1 << (ord(c) - ord('A'))
        for i in range(1 << n):
            dp[i | mask] = min(dp[i | mask], dp[i] + w)
    return dp[(1 << n) - 1] if dp[(1 << n) - 1] != float('inf') else -1

def test():
    # 测试用例 1
    T, n = 4, 3
    ingredients = [(5, 'C'), (6, 'B'), (16, 'BAC'), (4, 'A')]
    print(algorithm(T, n, ingredients))  # 输出: 15

    # 测试用例 2
    T, n = 1, 2
    ingredients = [(10, 'A')]
    print(algorithm(T, n, ingredients))  # 输出: -1


def main():
    T, n = map(int, input().split())
    ingredients = []
    for _ in range(T):
        w, s = input().split()
        ingredients.append((int(w), s))
    print(algorithm(T, n, ingredients))

if __name__ == '__main__':
    test()
    main()
