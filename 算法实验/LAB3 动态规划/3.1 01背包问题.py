# 0/1背包问题

# 输入:
# 4 5
# 1 2
# 2 4
# 3 4
# 4 5

# 第一行:物品数量n, 背包容量w
# 其余行:物品重量wi, 物品价值vi

# 输出最大价值:
# 8

def knapsack(w, n, items):
    value = [[0 for _ in range(w+1)] for _ in range(n+1)]

    for N in range(1, n+1):
        # 提取物品价值和重量
        wi, vi = items[N-1]
        # 填写第 N 行
        for W in range(1, w+1):
            if W >= wi:
                value[N][W] = max(value[N-1][W], value[N-1][W-wi]+vi)
            else:
                value[N][W] = value[N-1][W]
    return value[n][w]
    

def test():
    n, w = 4, 5
    items = [(1, 2), (2, 4), (3, 4), (4, 5)]
    
    print(knapsack(w, n, items))


if __name__ == "__main__":
    
    n, w = map(int,input().split())
    items = [map(int,input().split()) for _ in range(n)]
    print(knapsack(w, n, items))
