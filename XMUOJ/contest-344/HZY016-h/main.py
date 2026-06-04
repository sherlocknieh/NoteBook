# 在n*n的地图上布置n个防御塔
# 每个防御塔可以攻击同一行、同一列和同一对角线
# 有多少种布阵方案,使得防御塔不会相互攻击

# 输入: 4
# 输出: 2

# 输入: 8
# 输出: 92

def count_arrangements(n):
    count = 0
    pos = [-1] * n

    def check(pos,i,j):
        for k in range(i):
            if pos[k] == j or abs(pos[k] - j) == abs(k - i):
                return False
        return True
    
    def dfs(i, pos):
        for j in range(n):
            if check(pos, i, j):
                pos[i] = j
                if i == n - 1:
                    nonlocal count
                    count += 1
                else:
                    dfs(i + 1, pos)
                pos[i] = -1

    dfs(0, pos)
    return count

if __name__ == "__main__":
    n = int(input())
    print(count_arrangements(n))