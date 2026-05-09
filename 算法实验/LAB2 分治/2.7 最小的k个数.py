# 输入包含n个整数的数列，找出其中最小的k个数

# 第一行包含两个整数 n 和 k。
# 第二行包含 n 个整数，表示数列中的元素。

# 输入:
# 8 4
# 1 3 5 7 2 4 6 8

# 输出:
# 1 2 3 4

# 目标: 数列升序排列后, 下标为 k 的元素;
# 不变量: 目标元素在 [L, R] 范围内;
def quickFind(A, L, R, k):
    # 退出条件: 区间长度为 1
    if L==R : return
    # 选取基准元素
    pivot = A[R]
    # 所有元素按基准分配到左右两边
    t = L
    for i in range(L, R):
        if A[i] < pivot:
            A[i], A[t] = A[t], A[i]
            t = t + 1
    # 把基准元素置于第 t 位
    A[R],A[t] = A[t],A[R]
    # 递归寻找
    if t==k : return
    elif t>k : quickFind(A, L, t-1, k)
    else : quickFind(A, t+1, R, k)

def test():
    A = [1,3,5,7,2,4,6,8]
    quickFind(A, 0, 7, 4)
    print(*A[0:4])

def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    quickFind(A, 0, n-1, k)
    print(*A[0:k])

if __name__ == '__main__':
    main()
