'''
问题描述：
给定一个用字符串S表示的许可证，其中仅仅包含了数字、字母和短横线。
字符串被N个短横线“-”切分为了N+1组。
给定一个数字K，要求重新整理字符串的格式，
使得除了第一组之外的每个组正好K个字符，第一组长度可以比K小，
但也至少要包含一个字符。
此外，对于两个组之间必须要插入一个短横线，所有的小写字母都要转换为大写字母。

示例：
输入: S = "5F3Z-2e-9-w", K = 4
输出: "5F3Z-2E9W"
解释: 字符串S切分为两个部分, 每个部分有4个字符。
注意原串中两个额外的横线是多余的，可以删掉。

思路：
先遍历一遍S，把除-以外的字符全部去除。然后重新构造。

'''

class Solution:
    """
    @param S: a string
    @param K: a integer
    @return: return a string
    """
    def licenseKeyFormatting(self, S, K):
        # write your code here
        # 思路：先遍历一遍S，把除-以外的字符全部去除。然后重新构造
        char_list = []
        for char in S:
            if char != '-':
                if ord(char) >= 97:
                    char_list.append(chr(ord(char)-32))
                else:
                    char_list.append(char)
        mod = len(char_list) % K
        key = ''.join(char_list[:mod])
        key += '-'
        char_list = char_list[mod:]
        for i in range(len(char_list)):
            key += char_list[i]
            if (i+1) % K == 0 :
                key += '-'
        return key.strip('-')