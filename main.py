# 算法模板

def solve(n,a):
    print('n:',n)
    print('a:',a)

def test():
    n = 3
    a = [-1, 2, 3]
    solve(n,a)

if __name__ == "__main__":
    test()
    n = int(input())
    a = list(map(int,input().split()))
    solve(n,a)