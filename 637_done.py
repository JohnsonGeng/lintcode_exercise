'''
问题描述：给定一个非空字符串 word 和缩写 abbr，返回字符串是否可以和给定的缩写匹配。
比如一个 “word” 的字符串仅包含以下有效缩写：
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2",
"1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

示例：
输入 : s = "internationalization", abbr = "i12iz4n"
输出 : true

思路：扫描缩写单词，遇到字母则加1，遇到数字加上数字的值，注意连续的数字计算

时间太长，需要再刷！！！！！！
'''


def validWordAbbreviation(word, abbr):
    # write your code here
    # 思路：扫描缩写单词，遇到字母则加1，遇到数字加上数字的值，注意连续的数字
    i = 0
    count = 0
    # 用于计算连续的数字
    continue_bit = 0
    digits = 0
    if abbr[0] == '0':
        return False
    while i <= len(abbr) - 1:
        # 如果是字母，那么计数加1
        if ord(abbr[i]) >= ord('a') and ord(abbr[i]) <= ord('z'):
            count += 1
        # 如果是数字，判断是几位数字
        else:
            # 如果没到末尾并且后面还是数字
            if i + 1 <= len(abbr) - 1 and ord(abbr[i + 1]) >= ord('0') and ord(abbr[i + 1]) <= ord('9'):
                digits += int(abbr[i]) * 10
            else:
                if abbr[i] == '0' and ord(abbr[i-1]) >= ord('a') and ord(abbr[i-1]) <= ord('z'):
                    return False
                else:
                    digits += int(abbr[i])
                    count += digits
                    digits = 0
        i += 1
    if count == len(word):
        return True
    else:
        return False


if __name__ == '__main__':
    word = "a"
    abbr = '01'
    print(validWordAbbreviation(word, abbr))