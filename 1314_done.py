'''
问题描述：给定一个整数，写一个函数来确定它是否是2的幂。

示例：
输入: n = 3
输出: false

思路1：不断除以2，如果循环结束为1， 那么返回true，否则返回false
思路2：如果一个数是2的幂，那么其二进制只有一个1

'''


def isPowerOfTwo1(n):
    # Write your code here
    # 思路1:不断除以2，如果循环结束为1， 那么返回true，否则返回false
    while n > 1:
        n /= 2
    if int(n) == 1:
        return True
    else:
        return False

def isPowerOfTwo2(n):
    # Write your code here
    # 思路2:如果一个数是2的幂，那么其二进制只有一个1
    if n & (n - 1) == 0:
        return True
    else:
        return False