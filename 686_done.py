'''
问题描述：从句子中删除多余空。
示例：
Input: s = "The  sky   is blue"
Output: "The sky is blue"
思路：
先去除左右两边的空格。然后遍历字符串，遇到一个空格的时候判断后面是否还有空格即可。
'''


def removeExtra(s):
    # write your code here
    # 思路：先去除左右两边的空格。然后遍历字符串，遇到一个空格的时候判断后面是否还有空格即可。
    new_str = ''
    # index_left = 0
    # index_right = len(s)
    # 删除左边的空格字符
    # for i in range(len(s)):
    #     if s[i] == ' ':
    #         continue
    #     else:
    #         index_left = i
    #         break
    # # 删除右边的空格字符
    # for j in range(len(s)):
    #     if s[len(s) - (j + 1)] == ' ':
    #         continue
    #     else:
    #         index_right = len(s) - j - 1
    #         break
    # s = s[index_left:index_right]
    # 删除中间多余的字符
    s = s.strip(' ')
    for i in range(len(s) - 1):
        if s[i] != ' ' and s[i + 1] != ' ':
            new_str += s[i]
            continue
        if s[i] != ' ' and s[i + 1] == ' ':
            new_str += s[i]
            new_str += s[i + 1]
        if s[i] == ' ' and s[i + 1] == ' ':
            continue
        if s[i] == ' ' and s[i + 1] != ' ':
            continue
    if not s:
        return new_str
    else:
        new_str += s[-1]
        return new_str

if __name__ == '__main__':
    s = "  low               ercase  "
    print(removeExtra(s))
