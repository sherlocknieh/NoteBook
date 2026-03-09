
# 二分查找
# 循环不变量: 目标值 target 不在区间 [low, hig] 外.
def binary_search(arr: list[int], target: int) -> int:
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid
        else:
            # target > arr[mid]
            low = mid + 1
    return -1


# 循环不变量解决的困惑
# low <= high 还是 low < high
# high = mid - 1 还是 high = mid
# low = mid + 1 还是 low = mid



if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    index = binary_search(arr, target)
    print(f"Target {target} found at index: {index}")

