"""数列中的逆序对个数
输入:
6
2 3 4 5 6 1
输出:
5
"""

# 归并排序计数 | O(n log n)
import sys

def merge_sort(q, l, r):
    if l >= r:
        return 0
    
    mid = (l + r) // 2
    # 递归计算左右两半部分的逆序对
    res = merge_sort(q, l, mid) + merge_sort(q, mid + 1, r)
    
    # 合并阶段
    tmp = []
    i, j = l, mid + 1
    
    while i <= mid and j <= r:
        if q[i] <= q[j]:
            tmp.append(q[i])
            i += 1
        else:
            tmp.append(q[j])
            # 核心：如果 q[i] > q[j]，则 q[i] 到 q[mid] 都能与 q[j] 构成逆序对
            res += mid - i + 1
            j += 1
            
    # 链接剩余元素
    while i <= mid:
        tmp.append(q[i])
        i += 1
    while j <= r:
        tmp.append(q[j])
        j += 1
        
    # 将排序后的结果复制回原数组
    q[l:r+1] = tmp
    return res

def main():
    # 读取所有输入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    q = [int(x) for x in input_data[1:n+1]]
    
    # 计算逆序对数量
    print(merge_sort(q, 0, n - 1))

if __name__ == '__main__':
    main()