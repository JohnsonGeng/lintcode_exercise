'''
问题描述：
现在你是棒球比赛分记录员。

给定一个字符串数组，每一个字符串可以是以下4种中的其中一个：

整数 (一个回合的分数): 直接表示这回合你得到的分数。
"+" (一个回合的分数): 表示这回合你获得的分数为前两个 有效 分数之和。
"D" (一个回合的分数): 表示这回合你得到的分数为你上一次获得的有效分数的两倍。
"C" (一种操作，而非一个回合的分数): 表示你上回合的有效分数是无效的，需要移除。
每一轮的操作都是永久性的，可能会影响之前和之后的一轮。
你需要返回在所有回合中获得总分数。

示例：
输入: ["5","2","C","D","+"]
输出: 30
解释:
回合 1: 你可以得到 5 分，和为：5。
回合 2: 你可以得到 2 分，和为：7。
操作 1: 回合 2 的数据无效，所以和为 5。
回合 3: 你可以得到 10 分（回合 2 的数据已经被移除了），和为：15。
回合 4: 你可以得到 5 + 10 = 15 分，和为：30。

思路：使用一个栈来维护每一轮的分数，类似式子的中缀表达式转后缀表达式。

'''


def calPoints(ops):
    # Write your code here
    # 使用一个栈来维护每一轮的分数，类似式子的中缀表达式转后缀表达式
    stack = []
    for op in ops:
        if op == 'D':
            stack.append(stack[-1] * 2)
        elif op == 'C':
            stack.pop(-1)
        elif op == '+':
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))
    return sum(stack)