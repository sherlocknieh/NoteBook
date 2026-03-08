
# 二分查找
# 循环不变量: 目标值 target 始终在区间 [low, high] 中
# 循环不变量: 目标值 target 始终不在区间 [low, high] 外?
def binary_search(arr: list[int], target: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    # 如果走到这里，说明 target 不在闭区间 [low, high] 中
    # 因为此时 low > high，区间为空
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
