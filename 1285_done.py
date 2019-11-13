'''
问题描述：
给定一个整数（32位有符号整数），写一个方法判断这个数字是否为4的乘方。

示例1：
输入：num = 16
输出：True

示例2：
输入：num = 5
输出：False

思路：和2的幂类似

'''


def isPowerOfFour(num):
    # Write your code here
    # 思路：和2的幂类似
    # 如果是4的乘方不可能小于0
    if num <= 0:
        return False
    while num > 1:
        num /= 4
    if int(num) == 1:
        return True
    else:
        return False