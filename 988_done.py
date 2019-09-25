'''
问题描述：
你有 n 枚硬币，想要摆放成阶梯形状，即第 k 行恰好有 k 枚硬币
给出 n，找到可以形成的完整楼梯行数。
n 是一个非负整数，且在32位有符号整数范围内。

示例：
输入：n = 5
输出：2
解释：
硬币可以形成以下行：
¤
¤ ¤
¤ ¤
因为第3行不完整，我们返回2。

思路：用sum变量累加求和即可

'''


def arrangeCoins(n):
    # Write your code here
    # 思路：用sum累加即可
    sum = 0
    count = 0
    while sum <= n:
        count += 1
        sum += count
    return count - 1