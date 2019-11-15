'''
问题描述：
判断给出的年份 n 是否为闰年. 如果 n 为闰年则返回 true。
示例：
输入 : n = 2008
输出 : true
思路：简单的if判断即可
'''

class Solution:
    """
    @param n: a number represent year
    @return: whether year n is a leap year.
    """
    def isLeapYear(self, n):
        # write your code here
        # 思路：简单的if判断即可
        if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
            return True
        else:
            return False