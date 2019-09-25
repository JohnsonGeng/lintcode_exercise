'''
问题描述：我们有两个特殊的字符。
第一个字符可以用一位 0 来表示。第二个字符可以用两位(10 或者 11)表示。

现在给出一个字符串表示若干位。
返回最后一个字符是否必定为一位字符。给出的字符串总是以 0 结尾。

示例：
输入:
bits = [1, 0, 0]
输出: True
解释:
解码它的唯一方法是两位字符和一位字符。所以最后一个字符是一位字符。

思路：
从头到尾扫描字符串，遇到0后移一位，遇到1后移两位，移到倒数第二位为止。
1.最后一位是1，那么最后一位肯定不是一位字符，返回False
2.最后一位是0
    倒数第二位为1，那么最后一位不是一位字符，返回False
    倒数第二位为0，那么最后一位肯定是一位字符，返回True。

'''


def isOneBitCharacter(bits):
    # Write your code here
    i = 0
    if bits[-1] == 1:
        return False
    while i <= len(bits) - 2:
        if i == len(bits) - 2 and bits[i] == 1:
            return False
        if bits[i] == 0:
            i += 1
        else:
            i += 2
    return True