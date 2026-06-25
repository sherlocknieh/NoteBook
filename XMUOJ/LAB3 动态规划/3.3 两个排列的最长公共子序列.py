# 两个排列的最长公共子序列

# 输入:
# 5
# 1 3 2 5 4
# 2 3 5 4 1

# 输出:
# 3

# 2 5 4 是两个排列的最长公共子序列，长度为 3。

# 理解: 
# 任意两个排列等价于 [1,2,3,4,5] 及其打乱后的序列
# 递增序列 a = [1,2,3,4,5] 打乱后得 b = [2,5,3,1,4]
# a 和 b 的公共子序列一定是 a 的子序列, 所以必须递增
# 只需寻找 b 的递增子序列中最长的一个, 可找到 [2,3,4]

# 解法:
# 第一步: 获取相对排列
# 令 a = [(1,1), (2,3), (3,2), (4,5), (5,4)]
# 让 a 调整顺序变成 b, 得到
# b = [(3,2), (2,3), (4,5), (5,4), (1,1)]
# b_relative_a =  [3,2,4,5,1]
# 也可以类似的求 a_relative_b = [5, 2, 1, 3, 4]

# 第二步: 子序列分析
# F[2,5,1,3] = F[2,5,1]+[3] , F[2,5,1]
# F[2,5,1] = F[2,5]+[1] , F[2,5]
# F[2,5] = F[2]+[5] , F[2]
# F[2] = F[]+[2], F[]

# 第三步: 自底向上递推
# F[] = []					-> 0
# F[2] += [2]				-> 1
# F[2,5] += [2,5]			-> 2
# F[2,5,1] += [1]		    -> 2
# F[2,5,1,3] += [1,3],[2,3]	-> 2

# dp = [[],[2,5],[1,2],[1,2,3]]


# 导入二分查找模块
from bisect import bisect_left


def algorithm(n, a, b):
	# 建立 b 中各元素的位置索引
	pos = [0] * (n + 1)
	for i, x in enumerate(b, start=1):
		pos[x] = i
	
	# a 中元素 x 来自 b 中第 pos[x] 位
	seq = [pos[x] for x in a]

	# 在 seq 上求最长递增子序列。
	
	# tails[i] 表示：长度为 i + 1 的递增子序列中，末尾元素尽可能小的那个值。
	tails = []
	for x in seq:
		# 找到 x 应该插入到 tails 的位置：
		# - 如果 x 比所有 tails 元素都大，说明可以把当前 LIS 长度再扩展 1
		# - 否则，用 x 替换第一个 >= x 的位置，保持该长度下的末尾尽量小
		idx = bisect_left(tails, x)
		if idx == len(tails):
			# x 比当前所有尾值都大，形成了更长的递增子序列
			tails.append(x)
		else:
			# 用更小的 x 更新这一层的“最优尾值”
			tails[idx] = x

	# tails 的长度就是最长递增子序列的长度
	return len(tails)

def test():
	n = 5
	a = [1, 3, 2, 5, 4]
	b = [2, 3, 5, 4, 1]
	print(algorithm(n, a, b))

def main():
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	print(algorithm(n, a, b))

if __name__ == '__main__':
    test()
    main()