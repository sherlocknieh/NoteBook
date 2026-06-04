# 24点游戏

# 对于每一组测试数据, 如果可以得到24，输出“YES”；否则，输出“NO”。

# 输入
# 5 5 5 1
# 1 1 4 2
# 0 0 0 0
# 每行给出一组测试数据，包括4个小于10个正整数。
# 最后一组测试数据中包括4个0，表示输入的结束，这组数据不用处理。

# 输出
# YES
# NO

def solve(nums):
    if len(nums) == 1:
        return abs(nums[0] - 24) < 1e-6

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # 从 nums 中选出两个数 a 和 b
            a, b = nums[i], nums[j]
            # 将剩余的数放入 next_nums 中
            next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]

            # 加法
            if solve(next_nums + [a + b]):
                return True
            # 减法
            if solve(next_nums + [a - b]):
                return True
            if solve(next_nums + [b - a]):
                return True
            # 乘法
            if solve(next_nums + [a * b]):
                return True
            # 除法
            if b != 0 and solve(next_nums + [a / b]):
                return True
            if a != 0 and solve(next_nums + [b / a]):
                return True

    return False

while True:
    nums = list(map(int, input().split()))
    if nums == [0, 0, 0, 0]:
        break
    print("YES" if solve(nums) else "NO")