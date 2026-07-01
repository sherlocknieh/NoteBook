str1 = '2*3-4*5'

nums = [int(c) for c in str1 if c.isdigit()]
ops = [c for c in str1 if not c.isdigit()]

print(nums)
print(ops)