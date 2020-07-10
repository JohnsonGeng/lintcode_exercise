'''
问题描述：设计一种方法，通过给重复字符计数来进行基本的字符串压缩。
例如，字符串 aabcccccaaa 可压缩为 a2b1c5a3 。
而如果压缩后的字符数不小于原始的字符数，则返回原始的字符串。
可以假设字符串仅包括 a-z 的字母。

示例：
Input:str = "aabcccccaaa"
Output:"a2b1c5a3"

Input:"aabbcc"
Output:"aabbcc"

'''


def compress(originalString):
    # write your code here

    result = []
    count = 0

    # 空串直接返回
    if originalString == '':
        return originalString

    last_str = originalString[0]

    # 统计字符串中每个字符个数
    for s in originalString:
        cur_str = s
        if last_str == cur_str:
            count += 1
        else:
            result.append(last_str)
            result.append(str(count))
            count = 1
        last_str = cur_str
    result.append(last_str)
    result.append(str(count))

    # 比较返回哪一个字符串
    newString = ''.join(result)
    if len(newString) < len(originalString):
        return newString
    else:
        return originalString

if __name__ == '__main__':
    print(compress('aabcccccaaa'))