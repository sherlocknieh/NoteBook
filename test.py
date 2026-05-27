a = [1, 2, 3]
b = ['x', 'y', 'z']
result = list(zip(a, b))   # 没有星号，但传了两个参数
print(result)  # [(1, 'x'), (2, 'y'), (3, 'z')]

x = list(zip(*result))
print(x)  # [(1, 2, 3), ('x', 'y', 'z')]