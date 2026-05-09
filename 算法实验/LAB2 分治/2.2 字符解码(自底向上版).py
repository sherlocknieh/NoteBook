# 2.2 字符解码

# 输入: 3[a]2[bc] 
# 输出: "aaabcbc"

# 输入: 3[a2[c]]
# 输出: "accaccacc"

# 输入: abc3[cd]xyz
# 输出: "abccdcdcdxyz"


# 文法分析:

# S = ''                    # 编码串S可以是一个空字符串
# S = S + alpha             # 任意编码串添加一个字母也是一个编码串
# S = S + number[S]         # 任意编码串添加一个 number[S] 单元也是一个编码串
# number = digit            # 一个 digit 是一个数字
# number = number + digit   # 任意数字添加一个 digit 也是一个数字


# 自底向上归约解码:
def decodeString(S: str):
    stack = []
    stack.append({'type': 'S', 'value': ''})
    for c in S:
        # 字母
        if c.isalpha():
            # 栈顶为 S, 则用 S = S + alpha 归约
            if stack[-1]['type'] == 'S':
                stack[-1]['value'] += c
            # 栈顶不是 S, 则直接入栈
            else:
                stack.append({'type': 'S', 'value': c})
        # 数字
        elif c.isdigit():
            # 栈顶为 number, 则用 number = number + digit 归约
            if stack[-1]['type'] == 'number':
                stack[-1]['value'] += int(c)
            # 栈顶不是 number, 则直接入栈
            else:
                stack.append({'type': 'number', 'value': int(c)})
        # 右括号
        elif c == ']':
            S2 = stack.pop()
            # 如果栈顶为 'number', 说明 S = S1 + number[S2] 中 S2 为空串
            if S2['type'] == 'number': continue

            # 如果栈顶为 'S', 则用 S = S1 + number[S2] 归约
            else:
                number = stack.pop()
                S2['value'] *= number['value']
                stack[-1]['value'] += S2['value']
    # 归约结束后, 栈顶即为解码后的S串
    return stack.pop()['value']


# 简单的状态栈解码:
def decode_string(S):
    # 栈
    stack = []
    # 状态
    current_num = 0         # 局部数字
    current_string = ""     # 局部S串

    for char in S:
        # 读入数字
        if char.isdigit():
            # 更新局部数字
            current_num = current_num * 10 + int(char)
        # 读入左括号
        elif char == '[':
            # 保存旧状态
            stack.append((current_string, current_num))
            # 进入新状态
            current_string = ""
            current_num = 0
        # 读入右括号
        elif char == ']':
            # 获取旧状态
            last_string, num = stack.pop()
            # 合并结果
            current_string = last_string + current_string * num
        # 读入字母
        else:
            # 更新当前S串
            current_string += char

    return current_string


def test():
    print("简单状态栈解码:")
    print(decode_string("3[a]2[bc]"))
    print(decode_string("3[a2[c]]"))
    print(decode_string("abc3[cd]xyz"))
    print("自底向上归约解码:")
    print(decodeString("3[a]2[bc]"))
    print(decodeString("3[a2[c]]"))
    print(decodeString("abc3[cd]xyz"))


if __name__ == "__main__":
    test()