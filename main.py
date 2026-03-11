# 单词反转

# 输入样例
# Hello World

# 输出样例
# olleH dlroW

words = input().split()
reversed_words = [word[::-1] for word in words]
print(' '.join(reversed_words))