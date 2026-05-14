# 算法模板

def algorithm(n,a):
    print('n:',n)
    print('a:',a)

def test():
    n = 3
    a = [-1, 2, 3]
    algorithm(n,a)

if __name__ == "__main__":
    test()
    n = int(input())
    a = list(map(int,input().split()))
    algorithm(n,a)