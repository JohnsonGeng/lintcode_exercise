'''
问题描述：给定一个由ascii编码的字符串（例如，“ABC”可以编码为“656667”），
您需要编写一个将编码字符串作为输入并返回反转的解码字符串的函数。
注：可以假设答案字符串中只有大写字母。

示例：
输入： "7976766972"
输出： "HELLO"

思路：扫面字符串，取两位数字构成的ASCII码转换成字符并放入列表，反转并连接

思考：如果不限定是大写字母怎么办？

'''


def reverseAsciiEncodedString(encodeString):
    # Write your code here
    i = 0
    result_chr = []
    while i < len(encodeString) - 1:
        result_chr.append(chr(int(encodeString[i]) * 10 + int(encodeString[i + 1])))
        i += 2
    result_chr.reverse()
    return ''.join(result_chr)
