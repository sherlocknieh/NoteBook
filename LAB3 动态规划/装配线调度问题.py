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
    s1 = [0] * n    # 装配线1上各装配点的最快完成时间
    s2 = [0] * n    # 装配线2上各装配点的最快完成时间
    path1 = [0] * n # 装配线1上各装配点的最快路线来源
    path2 = [0] * n # 装配线2上各装配点的最快路线来源
    s1[0] = e[0] + a1[0]
    s2[0] = e[1] + a2[0]
    for i in range(1, n):
        if s1[i-1] == min(s1[i-1], s2[i-1] + t2[i-1]):
            s1[i] = a1[i] + s1[i-1]
            path1[i-1] = 1
        else:
            s1[i] = a1[i] + s2[i-1] + t2[i-1]
            path1[i-1] = 2
        
        if s2[i-1] == min(s2[i-1], s1[i-1] + t1[i-1]):
            s2[i] = a2[i] + s2[i-1]
            path2[i-1] = 2
        else:
            s2[i] = a2[i] + s1[i-1] + t1[i-1]
            path2[i-1] = 1
    
    path = [0] * n  # 最终最快路线

    if x[0] + s1[n-1] < x[1] + s2[n-1]:
        path[n-1] = 1
    else:
        path[n-1] = 2
    
    for i in range(n-2, -1, -1):
        if path[i] == 1:
            path[i] = path1[i]
        else:
            path[i] = path2[i]
    
    return path, min(s1[n-1] + x[0], s2[n-1] + x[1])


def test():
    n = 6
    a1 = [7, 9, 3, 4, 8, 4]
    a2 = [8, 5, 6, 4, 5, 7]
    t1 = [2, 3, 1, 3, 4]
    t2 = [2, 1, 2, 2, 1]
    e = [2, 4]
    x = [3, 2]
    print(AssemblyLineScheduling(n, a1, a2, t1, t2, e, x))
test()

def main():
    n = int(input())
    a1 = [int(i) for i in input().split()]
    a2 = [int(i) for i in input().split()]
    t1 = [int(i) for i in input().split()]
    t2 = [int(i) for i in input().split()]
    e = [int(i) for i in input().split()]
    x = [int(i) for i in input().split()]
    print(AssemblyLineScheduling(n, a1, a2, t1, t2, e, x))
main()