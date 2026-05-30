def QuickSort(A):
    if len(A) <= 1:
        return A
    pivot = A[len(A) // 2]
    left = [x for x in A if x < pivot]
    middle = [x for x in A if x == pivot]
    right = [x for x in A if x > pivot]
    return QuickSort(left) + middle + QuickSort(right)

A = [3, 1, 4, 1, 5, 9]
print(QuickSort(A))