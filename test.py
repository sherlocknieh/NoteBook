def Pow(x, n):
    # 先统一计算正指数的幂, 最后再根据指数符号决定是否取倒数;
    is_negative = (n < 0)
    n = abs(n)
    product = 1

    # 把 n 分解为2的幂次方的和
    # 如 n = 13 = 8 + 4 + 1, 
    # 则 x^n = x^1 * x^4 * x^8;
    # 如此计算高次幂时可以复用低次幂的结果, 从而减少乘法次数;
    while n > 0:
        # 如果 n 的二进制最低位是 1, 则乘上当前的 x;
        if n % 2 == 1:
            product *= x
        # x 幂次翻倍, n 右移一位;
        x = x * x
        n = n // 2
    # 根据指数符号决定是否取倒数;
    if is_negative:
        product = 1 / product
    return product

# 测试
print(Pow(2.0, -2))  # 0.25