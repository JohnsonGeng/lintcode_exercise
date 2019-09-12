'''
问题描述：给定两个字符串 s 和 t ，确定它们是否是同构的。
两个字符串是同构的如果 s 中的字符可以被替换得到 t。
所有出现的字符必须用另一个字符代替，同时保留字符串的顺序。
没有两个字符可以映射到同一个字符，但一个字符可以映射到自己。

示例：
输入 : s = "egg", t = "add"
输出 : true
说明 :
e -> a, g -> d。

思路：：要开辟 两个字典！！ 来存放元素之间的映射关系，
因为有可能在一个字典中一个元素映射到了两个元素上
如 s->t  a->t, 这是一遍循环无法判断的。

'''


def isIsomorphic(s, t):
    # write your code here
    # 思路：要开辟 两个字典！！ 来存放元素之间的映射关系，
    # 因为有可能在一个字典中一个元素映射到了两个元素上
    # 如 s->t  a->t, 这是一遍循环无法判断的。

    dict_s = {}
    dict_t = {}
    for i in range(len(s)):
        if s[i] not in dict_s.keys():
            dict_s[s[i]] = t[i]
        else:
            if dict_s[s[i]] == t[i]:
                continue
            else:
                return False
    for i in range(len(t)):
        if t[i] not in dict_t.keys():
            dict_t[t[i]] = s[i]
        else:
            if dict_t[t[i]] == s[i]:
                continue
            else:
                return False
    return True