# 2.8 石子游戏


# Alice 和 Bob 两个人轮流玩一个游戏，Alice 先手。
# 一开始，有 n 个石子堆在一起。每个人轮流操作，正在操作的玩家可以从石子堆里拿走 任意 非零 平方数 个石子。
# 如果石子堆里没有石子了，则无法操作的玩家输掉游戏。
# 给你正整数 n ，且已知两个人都采取最优策略。
# 如果最终 Alice 赢得比赛，那么输出"yes"，否则输出"no"。


# 输入:
# 第一行一个正整数t（t<=100），表示有t个测试用例
# 接下来t行，每行为一个正整数n，表示初始时有n个石子1<=n<=100000

# 5
# 1
# 2
# 4
# 7
# 17

# 输出:
# yes
# no
# yes
# no
# no



import sys

sys.setrecursionlimit(1000000)

# 记忆化字典
memo = {0: False}

def can_win(n):
    # 检查是否已经计算过
    if n in memo:
        return memo[n]
    
    # 尝试所有平方数
    i = 1
    while i * i <= n:
        # 如果对手在剩下的石子中会输，那么我就赢了
        if not can_win(n - i * i):
            memo[n] = True
            return True
        i += 1
    
    # 尝试了所有拿法都无法让对手输，则我必败
    memo[n] = False
    return False

def main():
    # 读取输入
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    for i in range(1, min(t, len(data)-1) + 1):
        n = int(data[i])
        # 执行递归搜索
        if can_win(n):
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()