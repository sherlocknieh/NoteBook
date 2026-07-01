import sys
 
def solve():

    # 输入案例
    # 5 2
    # 1 2 3 4 5

    # 优化读取大量输入
    data = [int(x) for x in sys.stdin.read().split()]  # [5, 2, 1, 2, 3, 4, 5]
    E = [0] + data[2:] + [0]    # E = [0, 1, 2, 3, 4, 5, 0]
    N,K = data[0], data[1]      # N = 5, K = 2
    total = sum(E)              # total = 15
    
    # f[i] 表示前 i 头奶牛中，第 i 头强制不选时，放弃的最小效率和
    f = [0] * (N + 2)
    
    # 使用 collections.deque 维护单调队列（存储下标）
    from collections import deque
    q = deque([0]) # 初始将 j = 0 压入队列
    
    for i in range(1, N + 2):
        # 1. 弹出离开滑动窗口的队头元素（上一头不选的奶牛必须在区间 [i-K-1, i-1] 内）
        while q and q[0] < i - K - 1:
            q.popleft()
            
        # 2. 此时队头就是窗口内 f[j] 的最小值
        f[i] = f[q[0]] + E[i]
        
        # 3. 维护队列的单调性，确保队列中对应的 f 值单调递增
        while q and f[q[-1]] >= f[i]:
            q.pop()
        q.append(i)
        
    # 最大总效率 = 总效率 - 最小放弃效率
    print(total - f[N + 1])
 
if __name__ == '__main__':
    solve()