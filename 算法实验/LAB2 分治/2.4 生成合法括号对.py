# 2.4 生成括号
#
# 有 n 个元素和一个空容器;
# 每个元素都要经历一次进入容器和一次离开容器;
# 用左括号 "(" 表示添加, 右括号 ")" 表示离开。
# 生成所有可能的括号序列, 要求按字典序输出;
#
# 输入:
# 3
#
# 输出:
# "((()))","(()())","(())()","()(())","()()()"


# 思路: 
# 递归生成所有括号序列, 用条件排除不合法的分支;
# 优先生成左括号, 以保证输出的序列按字典序排列;

# 排除条件:
# 1. 左括号数量超过 n 个;
# 2. 右括号数量超过左括号数量;


def generate_parentheses(n):
    results = []
    result = []

    def backtrack(left_count, right_count):
        # 递归出口
        if len(result) == 2*n:
            results.append(''.join(result))
        
        # 添加一个左括号
        if left_count < n:
            result.append("(")
            backtrack(left_count + 1, right_count)
            result.pop()

        # 添加一个右括号
        if right_count < left_count:
            result.append(")")
            backtrack(left_count, right_count + 1)
            result.pop()

    backtrack(0, 0)
    return results

def test():
    n = 1
    r = generate_parentheses(n)
    r = ['"'+e+'"' for e in r]
    print(','.join(r))

if __name__ == "__main__":
    #test()

    n = int(input())
    r = generate_parentheses(n)
    r = ['"'+e+'"' for e in r]
    print(','.join(r))