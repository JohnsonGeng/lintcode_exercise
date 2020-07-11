'''
问题描述：给出两个字符串, 你需要修改第一个字符串，
将所有与第二个字符串中相同的字符删除,
并且第二个字符串中不同的字符与第一个字符串的不同字符连接

示例：
Input : s1 = "aacdb", s2 = "gafd"
Output : "cbgf"

'''



def concatenetedString(s1, s2):
    # write your code here
    result_s1 = []
    result_s2 = list(s2)

    # 目前想到蛮力法
    for c in s1:
        if c not in s2:
            result_s1.append(c)
        else:
            while(c in result_s2):
                result_s2.remove(c)

    # 连接
    result_s1.extend(result_s2)

    return ''.join(result_s1)