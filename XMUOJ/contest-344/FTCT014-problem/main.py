# 0/1背包问题 (背包容量和物品价值上限很大, 物品数量较少)

# 输入
# 4 5
# 1 2
# 2 4
# 3 4
# 4 5

# 第一行两个整数 n, w (1<= n <=8, 1<= w <=2000000000) 表示物品数量和背包容量。
# 接下来 n 行每行有两个整数 wi, vi (1<= wi <=1000000000, 1<= vi <=1000000),表示物品重量和价值


# 输出最大价格
# 8



def solve(w, n, items):
    max_value = 0

    # 深度搜索
    # 深度 i 表示正在对第 i 个物品做装/不装的判断
    # value, weight 表示当前已装物品的总价值和重量
    def dfs(i, value, weight):
        nonlocal max_value  # 涉及赋值的外部变量声明

        # 到达第 n 个物品
        if i==n:
            max_value = max(max_value, value)
            return

        # 假如不装入第 i 个物品
        dfs(i+1, value, weight)
        
        # 假如装入第 i 个物品
        wi, vi = items[i]
        if weight + wi <= w:  # 只有在不超过背包容量的情况下才考虑装入
            dfs(i+1, value+vi, weight+wi)
    
    # 启动深度搜索
    dfs(0,0,0)
    # 返回最大价值
    return max_value


def test():
    n, w = 4, 5
    items = [(1, 2), (2, 4), (3, 4), (4, 5)]
    
    print(solve(w, n, items))


if __name__ == "__main__":
    #test()
    n, w = map(int,input().split())
    items = [tuple(map(int,input().split())) for _ in range(n)]
    print(solve(w, n, items))
