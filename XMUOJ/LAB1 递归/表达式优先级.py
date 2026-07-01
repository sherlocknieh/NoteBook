"""
输入:
2*3-4*5
输出:
-34
-14
-10
-10
10


输入:
10-5*6
输出:
-20
30
"""
expr = input()
ops = []
nums = []

i = 0
while i < len(expr):
    if expr[i] in '+-*':
        ops.append(expr[i])
        i += 1
    else:
        j = i
        while j < len(expr) and expr[j].isdigit():
            j += 1
        nums.append(int(expr[i:j]))
        i = j

def calc(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b

# 计算 nums[left:right+1] 范围内所有可能的结果
memo = {}
def dfs(left, right):
    # 如果范围内只有一个数字，直接返回该数字
    if left == right:
        return [nums[left]]
    
    # 记忆化，避免重复计算
    state = (left, right)
    if state in memo:
        return memo[state]
        
    res = []
    # i 是当前范围内可以作为“最后一步计算”的运算符索引
    # nums[left:right+1] 对应的运算符范围是 ops[left:right]
    for i in range(left, right):
        op = ops[i]
        
        # 分：计算左边和右边所有的可能结果
        left_results = dfs(left, i)
        right_results = dfs(i + 1, right)
        
        # 治：组合两边的结果
        for l in left_results:
            for r in right_results:
                res.append(calc(l, r, op))
                
    memo[state] = res
    return res

# 运算范围：从第 0 个数字到最后一个数字
results = dfs(0, len(nums) - 1)

# 从小到大排序输出
results.sort()
for result in results:
    print(result)