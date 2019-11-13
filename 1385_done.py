'''
问题描述：8是小九的幸运数字，小九想知道在1~n的数中有多少个数字含有8。

示例：
输入: n = 100
输出: 19
解释:
有8,18,28,38,48,58,68,78,80,81,82,83,84,85,86,87,88,89,98。

思路1：1-n每个数判断一下，每个数求余判断。时间复杂度太高。
思路2：有具体公式，这里不给出

'''


def luckyNumber(n):
    # Write your code here
    count = 0
    for i in range(1, n):
        while i > 1:
            mod = i % 10
            if mod == 8:
                count += 1
                break
            else:
                i = int((i - mod) / 10)
    return count