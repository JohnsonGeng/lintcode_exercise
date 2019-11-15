'''
问题描述：
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，
并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
示例：
Input: "Hello"
Output: "hello"
思路：
判断ascii码是否在65-91之间即可，然后加上32变成小写字符。
'''

class Solution:
    """
    @param str: the input string
    @return: The lower case string
    """
    def toLowerCase(self, str):
        # Write your code here
        # 思路：判断ascii码是否在65-91之间即可，然后加上32变成小写字符
        new_str = ''
        for char in str:
            if 65 <= ord(char) and ord(char) <= 91:
                new_str += chr(ord(char)+32)
            else:
                new_str += char
        return new_str
