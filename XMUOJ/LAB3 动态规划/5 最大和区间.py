"""
最大子数组问题:
input:
8
-50 120 -30 80 -40 150 -200 90

output: 
280
"""

input_data = """8
-50 120 -30 80 -40 150 -200 90"""

n = int(input())
a = list(map(int, input_data.split()[1:]))

b = [0 for _ in range(n+1)]

max_sum = 0

for i in range(1,n+1):
    b[i] = b[i-1] + a[i-1]
    if b[i] < 0: b[i] = 0
    max_sum = max(max_sum, b[i])


print(max_sum)

