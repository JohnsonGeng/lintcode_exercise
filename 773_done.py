'''
问题描述：
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例：
Input : s = "anagram", t = "nagaram"
Output : true

'''

'''

知识点：Python中dict的get方法找不到元素返回None

'''


def isAnagram(s, t):
    # write your code here

    # 哈希表保存每个字符出现次数
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    # 统计字符串出现次数
    for i, j in zip(s, t):
        if count_s.get(i):
            count_s[i] += 1
        else:
            count_s[i] = 1
        if count_t.get(j):
            count_t[j] += 1
        else:
            count_t[j] = 1

    # 遍历字典，看频率是否一致
    for key in count_s:
        if count_t.get(key):
            if count_s[key] == count_t[key]:
                continue
        else:
            return False
    return True

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))