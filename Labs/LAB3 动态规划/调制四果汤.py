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
# 商店只有含 A 的配料，无法满足要求，输出 -1。

def algorithm():
    # 目标特征集合
    target_features = set(chr(ord('A') + i) for i in range(n))

    # 最小费用覆盖特征集合
    min_cost = float('inf')
    for i in range(1 << T):
        covered_features = set()
        total_cost = 0
        for j in range(T):
            if (i >> j) & 1:
                total_cost += ingredients[j][0]
                covered_features.update(ingredients[j][1])
        if covered_features >= target_features:
            min_cost = min(min_cost, total_cost)

    print(min_cost if min_cost != float('inf') else -1)

def test():
    # 测试用例 1
    T, n = 4, 3
    ingredients = [(5, 'C'), (6, 'B'), (16, 'BAC'), (4, 'A')]
    algorithm()  # 输出: 15

    # 测试用例 2
    T, n = 1, 2
    ingredients = [(10, 'A')]
    algorithm()  # 输出: -1

def main():
    global T, n, ingredients
    T, n = map(int, input().split())
    ingredients = []
    for _ in range(T):
        w, s = input().split()
        ingredients.append((int(w), s))
    algorithm()

if __name__ == '__main__':
    test()
    main()
