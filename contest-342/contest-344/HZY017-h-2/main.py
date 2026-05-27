# 含障碍物的防御塔问题
# 规定任意两个防御塔不能位于同一行或者同一列, 除非它们之间有障碍物隔开

# 输入
# 第一行一个n(2<=n<=4),表示地图的大小
# 然后是 4*4 的矩形,矩形的每个元素为'X'或'.',分别表示障碍物和空地

# 4
# .X..
# ....
# XX..
# ....

# 输出防御塔的最大个数
# 5


def is_valid(row, col, grid, n):
    # 检查当前格子是否可以放置防御塔
    if grid[row][col] == 'X':
        return False
    # 检查同一行和同一列是否有防御塔
    # 向左检查
    for i in range(col - 1, -1, -1):
        if grid[row][i] == 'X':
            break
        if grid[row][i] == 'T':
            return False
    # 向右检查
    for i in range(col + 1, n):
        if grid[row][i] == 'X':
            break
        if grid[row][i] == 'T':
            return False
    # 向上检查
    for i in range(row - 1, -1, -1):
        if grid[i][col] == 'X':
            break
        if grid[i][col] == 'T':
            return False
    # 向下检查
    for i in range(row   + 1, n):
        if grid[i][col] == 'X':
            break
        if grid[i][col] == 'T':
            return False
    # 如果没有冲突，返回True
    return True

def solve(n, grid):
    max_towers = 0
    # 使用回溯算法尝试放置防御塔
    def backtrack(index, count):
        # index 是一维化的索引，范围在 [0,n*n-1]
        if index == n * n:
            nonlocal max_towers
            max_towers = max(max_towers, count)
            return

        row = index // n    # 提取行
        col = index % n     # 提取列
        
        if is_valid(row,col,grid,n):
        # 如果可放置
            # 放置防御塔
            grid[row][col] = 'T'
            # 继续尝试下一个位置
            backtrack(index + 1, count + 1)
            # 回退
            grid[row][col] = '.'
            # 选择不放置，继续尝试下一个位置
            backtrack(index + 1, count)
        else:
        # 不可放置，继续尝试下一个位置
            backtrack(index + 1, count)
        pass
    
    backtrack(0, 0)
    return max_towers

def test():
    n = 4
    grid = [
        ['.','X','.','.'],
        ['.','.','.','.'],
        ['X','X','.','.'],
        ['.','.','.','.']
    ]
    print(solve(n, grid))

if __name__ == "__main__":
    #test()
    n = int(input())
    grid = [list(input()) for _ in range(n)]
    print(solve(n, grid))