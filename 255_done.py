'''
问题描述：
给出一个源字符串sourceString和一个目标字符串数组targetStrings，
判断目标字符串数组中的每一个字符串是否是源字符串的子串

示例：
Input : sourceString = "abc" ，targetStrings = ["ab","cd"]
Output : [true, false]

'''


def whetherStringsAreSubstrings(sourceString, targetStrings):
    # write your code here

    result = []

    # 方法1:直接用python的in判断
    for string in targetStrings:
        if string in sourceString:
            result.append(True)
        else:
            result.append(False)

    # TODO
    # 方法2:KMP算法

    return result