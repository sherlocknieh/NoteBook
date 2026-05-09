# 装配线调度问题

# 输入:
# 6
# 7 9 3 4 8 4
# 8 5 6 4 5 7
# 2 3 1 3 4
# 2 1 2 2 1
# 2 4
# 3 2

# 第1行: 装配线的个数 n
# 第2行: 装配线1上各装配点的装配时间
# 第3行: 装配线2上各装配点的装配时间
# 第4行: 从装配线1转到装配线2的转移时间
# 第5行: 从装配线2转到装配线1的转移时间
# 第6行: 从工厂入口到装配线1和装配线2的进入时间
# 第7行: 从装配线1和装配线2的出口到工厂的退出时间


# 输出:
# 38

def AssemblyLineScheduling(n, a1, a2, t1, t2, e, x):

    a1[0]   += e[0]  # 把进入时间合并到开头装配时间上
    a2[0]   += e[1]  # 把进入时间合并到开头装配时间上

    a1[n-1] += x[0]  # 把退出时间合并到末尾装配时间上
    a2[n-1] += x[1]  # 把退出时间合并到末尾装配时间上

    path_1 = [0] * (n-1)  # 装配线1上的最优来源表
    path_2 = [0] * (n-1)  # 装配线2上的最优来源表

    for i in range(1, n):
        # 如果从装配线1直行更快，就走装配线1
        if a1[i-1] <= a2[i-1] + t2[i-1]:
            a1[i] += a1[i-1]
            path_1[i-1] = 1
        # 如果从装配线2转过来更快，就从装配线2来
        else:
            a1[i] += a2[i-1] + t2[i-1]
            path_1[i-1] = 2
        
        # 如果从装配线2直行更快，就走装配线2
        if a2[i-1] <= a1[i-1] + t1[i-1]:
            a2[i] += a2[i-1]
            path_2[i-1] = 2
        # 如果从装配线1转过来更快，就从装配线1来
        else:
            a2[i] += a1[i-1] + t1[i-1]
            path_2[i-1] = 1

    # 打印最优装配时间
    print('min:',min(a1[n-1], a2[n-1]))

    # 打印最优装配方案(从后往前输出)
    if a1[n-1] <= a2[n-1]:
        print('line 1 station', n)
        for i in range(n-1, 0, -1):
            print('line', path_1[i-1], 'station', i)
    else:
        print('line 2 station', n)
        for i in range(n-1, 0, -1):
            print('line', path_2[i-1], 'station', i)



def test():
    n = 6
    a1 = [7, 9, 3, 4, 8, 4]
    a2 = [8, 5, 6, 4, 5, 7]
    t1 = [2, 3, 1, 3, 4]
    t2 = [2, 1, 2, 2, 1]
    e = [2, 4]
    x = [3, 2]
    AssemblyLineScheduling(n, a1, a2, t1, t2, e, x)
test()

def main():
    n = int(input())
    a1 = [int(i) for i in input().split()]
    a2 = [int(i) for i in input().split()]
    t1 = [int(i) for i in input().split()]
    t2 = [int(i) for i in input().split()]
    e = [int(i) for i in input().split()]
    x = [int(i) for i in input().split()]
    AssemblyLineScheduling(n, a1, a2, t1, t2, e, x)
main()