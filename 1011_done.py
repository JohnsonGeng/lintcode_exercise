'''
问题描述：
把字符串S中的字符从左到右写入行中。
每行最大宽度度为100，如果往后新写一个字符导致该行宽度超过100，则写入下一行。
注意：一个字符的宽度不为1！给定一个数组widths，
其中widths[0]是字符a的宽度，widths[1]是字符b的宽度，...，
widths[25]是字符'z'的宽度。

示例：
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
输出: [3, 60]
解释:
每个字符的宽度都是10. 为了把这26个字符都写进去，需要两个整行和一个用去60长度的行。

思路：直接一个个字符扫描过去，计算该字符需要的长度，如果当前行累积超过100，另起一行。

'''


def numberOfLines(widths, S):
    # Write your code here
    # 思路：直接一个个字符扫描过去，计算该字符需要的长度，如果当前行累积超过100，另起一行。
    lines = 1
    sum_of_chr = 0
    max_chr = 100
    for i in range(len(S)):
        if sum_of_chr + widths[ord(S[i]) - ord('a')] > max_chr:
            lines += 1
            sum_of_chr = 0
            sum_of_chr += widths[ord(S[i]) - ord('a')]
        elif sum_of_chr + widths[ord(S[i]) - ord('a')] == max_chr:
            lines += 1
            sum_of_chr = 0
        else:
            sum_of_chr += widths[ord(S[i]) - ord('a')]
    return [lines, sum_of_chr]

if __name__ == '__main__':
    width = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    S = "bbbcccdddaaa"
    print(numberOfLines(width, S))