'''
问题描述：实现一个leftpad库，如果不知道什么是leftpad可以看样例

示例1：
输入:
leftpad("foo", 5)
输出:
"  foo"

示例2：
输入:
leftpad("foobar", 6)
输出:
"foobar"

思路：计算填充后长度，求得与原始长度的差，最后拼接字符即可。
'''


def leftPad(self, originalStr, size, padChar=' '):
    # write your code here
    padSize = size - len(originalStr)
    temp_str = padChar * padSize
    return temp_str + originalStr

