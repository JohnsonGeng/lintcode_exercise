'''
问题描述：给定一个整数，判断它是否为3的幂。

示例1：
输入: n = 0
输出: False

示例2：
输入: n = 9
输出: True

思路：不断除以3看最后是否为1即可


'''



def isPowerOfThree(self, n):
    # Write your code here
    while n>1:
        n /= 3
    if n == 1:
        return True
    else:
        return False