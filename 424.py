'''
问题描述：
求逆波兰表达式的值。
在逆波兰表达法中，其有效的运算符号包括 +, -, *, / 。
每个运算对象可以是整数，也可以是另一个逆波兰计数表达。

示例：
输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ["2", "1", "+", "3", "*"] -> (2 + 1) * 3 -> 9

思路：使用栈实现即可

'''


def evalRPN(tokens):
    # write your code here
    # 思路：逆波兰符直接用栈实现就好了
    stack = []
    ops = ['+', '-', '*', '/']
    op1 = 0
    op2 = 0
    for token in tokens:
        # 说明是数字
        if token not in ops:
            stack.append(int(token-'o'))
        else:
            if token == '+':
                op1 = stack.pop(-1)
                op2 = stack.pop(-1)
                val = op1 + op2
                stack.append(val)
            elif token == '-':
                op1 = stack.pop(-1)
                op2 = stack.pop(-1)
                val = op2 - op1
                stack.append(val)
            elif token == '*':
                op1 = stack.pop(-1)
                op2 = stack.pop(-1)
                val = op1 * op2
                stack.append(val)
            else:
                op1 = stack.pop(-1)
                op2 = stack.pop(-1)
                val = op2 / op1
                stack.append(val)
    return stack[0]

if __name__ == '__main__':
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(tokens))

