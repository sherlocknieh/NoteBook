# 2.2 字符解码

# 输入: 3[a]2[bc] 
# 输出: "aaabcbc"

# 输入: 3[a2[c]]
# 输出: "accaccacc"

# 输入: abc3[cd]xyz
# 输出: "abccdcdcdxyz"


# 文法分析 (右递归版):
# S = ""
# S = [a-z] + S
# S = number[S] + S
# number = [0-9]
# number = [0-9] + number


# 自顶向下递归解码:


# 从 "number..." 开头提取数字串, 返回数字串
def decode_number(str):
    # number = [0-9] 的情况, 字符串形如 "1..."
    if not str[1].isdigit():
        return str[0]
    # number = number + [0-9] 的情况, 字符串形如 "123..."
    return str[0] + decode_number(str[1:])


# 从 "S..." 开头提取S串, 返回解码后的字符串和剩余字符串
def decode_string(str):
    # S = 空串, 即 str = "" 或 "..."; 其中 "..." 的开头只可能是 "]"
    if len(str) == 0 or str[0] == ']':
        return {
            'decoded': '',
            'remained': str
        }
    
    # str = "[a-z]S..." 的情况
    if str[0].isalpha():
        S = decode_string(str[1:])
        return {
            'decoded': str[0] + S['decoded'],
            'remained': S['remained']
        }
    
    # S = "number[S1] + S2..." 的情况
    if str[0].isdigit():
        # 解码数字串
        num = decode_number(str)

        # 去掉 "number[", 解码S1串
        S1 = decode_string(str[len(num)+1:])
        
        # 去掉 "S1]", 解码S2串
        S2 = decode_string(S1['remained'][1:])

        return {
            'decoded': S1['decoded'] * int(num) + S2['decoded'],
            'remained': S2['remained']
        }




def test():
    print(decode_string('3[a]2[bc]')['decoded'])
    print(decode_string('3[a2[c]]')['decoded'])
    print(decode_string('abc3[cd]xyz')['decoded'])


if __name__ == "__main__":
    test()