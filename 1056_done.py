'''
问题描述：给定一串只含有小写形式的、排序过的 letters，
并且给定一个目标字母 target ，请找出在给定字母串中，
大于目标字母的最小的那一个字母。

在本题中，字母是绕回编址的（即“z”后一位重新变为“a”）。
比如说，如果target = 'z'，而给定字母串为letters = ['a', 'b']，
那么答案为“a”。

示例：
输入:
letters = ["c", "f", "j"]
target = "a"
输出: "c"

思路：两种情况 1.没有回绕，那么找到第一个比target大的返回即可 2.即便是回绕，返回第一个就可以了

'''


def nextGreatestLetter(letters, target):
    # Write your code here
    for ch in letters:
        if ch > target:
            return ch
        else:
            continue