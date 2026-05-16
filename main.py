# 算法模板

def solve(n,a):
    print('n:',n)
    print('a:',a)

def test():
    grid = list(input())
    print('grid:',grid)

if __name__ == "__main__":
    test()
    n = int(input())
    a = list(map(int,input().split()))
    solve(n,a)