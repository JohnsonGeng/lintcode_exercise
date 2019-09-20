'''
问题描述：给出一个字符串。找到字符串中第一个不重复的字符然后返回它的下标。
如果不存在这样的字符，返回 -1。

示例1：
输入 : s = "lintcode"
输出 : 0

示例2：
输入 : s = "lovelintcode"
输出 : 2

思路1:扫描一遍字符串，用字典记录各个字符出现的次数，再扫一次字符串，遇到val为1的key输出下标
缺点：需要扫描两次字符串

思路2：还没想到

'''


def firstUniqChar(s):
    # write your code here
    # 思路1:扫描一遍字符串，用字典记录各个字符出现的次数，再扫一次字符串，遇到val为1的key输出下标
    # 缺点：需要扫描两次字符串
    dict = {}
    for chr in s:
        if dict.get(chr):
            dict[chr] += 1
        else:
            dict[chr] = 1
    for i in range(len(s)):
        if dict[s[i]] == 1:
            return i
        else:
            continue
    return -1
