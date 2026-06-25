# 2.2 字符解码

# 输入: 3[a]2[bc] 
# 输出: "aaabcbc"

# 输入: 3[a2[c]]
# 输出: "accaccacc"

# 输入: abc3[cd]xyz
# 输出: "abccdcdcdxyz"


# 文法分析 (左递归版):
# S = ""                    # 编码串S可以是一个空字符串
# S = S + [a-z]             # 任意编码串添加一个字母也是一个编码串
# S = S + number[S]         # 任意编码串添加一个 number[S] 单元也是一个编码串
# number = [0-9]            # 一个 digit 是一个数字
# number = number + [0-9]   # 任意数字添加一个 digit 也是一个数字


# 自顶向下递归解码 (左递归版):


# 从 "...number" 末尾提取数字串, 返回数字串
def decode_number(str):
    # number = [0-9] 的情况, 字符串形如 "...1" 
    if len(str) == 1 or not str[-2].isdigit():
        return str[-1]
    # number = number + [0-9] 的情况, 字符串形如 "...123"
    return decode_number(str[:-1]) + str[-1]


# 从 "...S" 末尾提取S串, 返回解码后的S串和剩余串
def decode_string(S):
    # S为空串的情况, 可能是 "" 或 "...", 其中 "..." 的末尾只可能是 "["
    if len(S) == 0 or S[-1] == '[':
        return {
            'decoded': "",
            'remained': S,
        }
    
    # "...S+[a-z]" 的情况
    if S[-1].isalpha():
        # 去掉尾字符, 递归解码尾部S串
        S1 = decode_string(S[:-1])
        return {
            'decoded': S1['decoded'] + S[-1],
            'remained': S1['remained'],
        }
    
    # "...S1+number[S2]" 的情况
    elif S[-1] == ']':
        # 去掉尾括号 ']'，解码尾部S2串
        S2 = decode_string(S[:-1])
        
        # 去掉 '[', 解码 number
        number = decode_number(S2['remained'][:-1])

        # 去掉 "number[", 解码S1串
        S1 = decode_string(S2['remained'][:-len(number)-1])

        return {
            'decoded': S1['decoded'] + S2['decoded'] * int(number),
            'remained': S1['remained'],
        }



def test():
    print(decode_string("3[a]2[bc]")['decoded'])
    print(decode_string("3[a2[c]]")['decoded'])
    print(decode_string("abc3[cd]xyz")['decoded'])

def main():
    raw = input()
    print(decode_string(raw)['decoded'])

if __name__ == "__main__":
    test()
    main()