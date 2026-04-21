# 两个排列的最长公共子序列
# 描述

# 给定两个长度均为 n 的排列 a 和 b，其中 1 到 n 每个整数都在两个排列中恰好出现一次。

# 请你求出这两个排列的最长公共子序列长度，并将时间复杂度控制在 O(n log n)。

# 出题人：周泰儒同学


# 输入

# 第一行输入一个整数 n。

# 第二行输入排列 a。

# 第三行输入排列 b。


# 输出

# 输出一个整数，表示两个排列的最长公共子序列长度。


# 输入样例 1 

# 5
# 1 3 2 5 4
# 2 3 5 4 1
# 输出样例 1

# 3

from bisect import bisect_left
import sys


def solve() -> None:
	data = list(map(int, sys.stdin.buffer.read().split()))
	if not data:
		return

	n = data[0]
	a = data[1:1 + n]
	b = data[1 + n:1 + 2 * n]

	# pos[x] = x 在排列 b 中的位置（从 1 开始），用于将 LCS 转化为 LIS。
	pos = [0] * (n + 1)
	for i, x in enumerate(b, start=1):
		pos[x] = i

	seq = [pos[x] for x in a]

	# 在 seq 上求严格递增子序列长度（LIS），即答案。
	tails = []
	for x in seq:
		idx = bisect_left(tails, x)
		if idx == len(tails):
			tails.append(x)
		else:
			tails[idx] = x

	sys.stdout.write(str(len(tails)))


if __name__ == "__main__":
	solve()