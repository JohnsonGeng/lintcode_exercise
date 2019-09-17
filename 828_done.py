'''
问题描述：给定一个模式串pattern和一个字符串str，
请问str和pattern是否遵循相同的模式。
这里遵循模式指的是一个完全匹配，
即在pattern中的每个不同的字母和str中每个非空的单词之间有一个双向映射的模式对应。

示例1：
输入: pattern = "abba" and str = "dog cat cat dog"
输出: true
解释:
str的模式是 abba

示例2：
输入: pattern = "abba" and str = "dog cat cat fish"
输出: false
解释:
str的模式是 abbc

思路：首先将字符串逐个拆分，放入列表。利用字典建立映射关系即可。
但是注意！！！映射关系必须是双向的
'''


def wordPattern(pattern, teststr):
    # write your code here
    # 首先将字符串逐个拆分，放入列表。利用字典建立映射关系即可，但是记得是双向映射！
    word_list = teststr.split()
    pattern_to_teststr_dict = {}
    teststr_to_pattern_dict = {}
    # 如果二者长度不一样那肯定不是一个模式
    if len(pattern) != len(word_list):
        return False
    for i in range(len(pattern)):
        if pattern[i] in pattern_to_teststr_dict.keys():
            if pattern_to_teststr_dict[pattern[i]] == word_list[i]:
                continue
            else:
                return False
        else:
            pattern_to_teststr_dict[pattern[i]] = word_list[i]

    for j in range(len(word_list)):
        if word_list[j] in teststr_to_pattern_dict.keys():
            if teststr_to_pattern_dict[word_list[j]] == pattern[j]:
                continue
            else:
                return False
        else:
            teststr_to_pattern_dict[word_list[j]] = pattern[j]

    return True

if __name__ == '__main__':
    pattern = 'abba'
    teststr = 'dog dog dog dog'
    print(wordPattern(pattern, teststr))