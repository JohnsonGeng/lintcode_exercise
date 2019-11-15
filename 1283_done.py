'''
问题描述：
写一个方法，接受给定字符串作为输入，
返回将这个字符串逐个字符翻转后的新字符串。
示例：
输入："hello world"
输出："dlrow olleh"
思路：

'''

class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def reverseString(self, s):
        # write your code here
        # 方法1：从后往前取字符既可
        reverse_string = ''
        for i in range(len(s)):
            reverse_string += s[len(s)-(i+1)]
        return reverse_string
        # 方法2：直接列表操作返回
        # return s[::-1]