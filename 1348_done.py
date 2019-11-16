'''
问题描述：
给定Excel工作表中显示的列名称，返回其对应的列号。
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
示例：
输入: "AB"
输出: 28
思路：相当于将一个26进制数转换为10进制数。
'''

def titleToNumber(s):
    # write your code here
    # 思路：相当于将一个26进制数转换为10进制数
    order = 0
    for i in range(len(s)):
        order += (ord(s[i]) - ord('A') + 1) * (26 ** (len(s) - i - 1))
    return order




if __name__ == '__main__':
    s = 'AB'
    print(titleToNumber(s))
