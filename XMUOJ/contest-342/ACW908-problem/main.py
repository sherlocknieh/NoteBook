# 输入
# 3
# -1 1
# 2 4
# 3 5

# 输出
# 2

def algorithm(n,a):
    # 按结束时间升序排序
    a = sorted(a, key=lambda x: x[1])
    result = []
    for ai,bi in a:
        if not result or ai >= result[-1][1]:
            result.append((ai, bi))
    print(len(result))

def test():
    n = 3
    a = [(-1, 1), (2, 4), (3, 5)]
    algorithm(n,a)
    
if __name__ == "__main__":
    # test()
    n = int(input())
    a = [tuple(map(int,input().split())) for _ in range(n)]
    algorithm(n,a)