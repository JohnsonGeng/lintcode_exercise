'''
问题描述：写一个方法，接受给定字符串作为输入，并且只翻转字符串中的元音字母。

示例：
输入 : s = "hello"
输出 : "holle"

思路：
从左右两边开始,类似快速排序，交换元素即可

'''


def reverseVowels(s):
    # write your code here
    # 思路：从左右两边开始,类似快速排序，交换元素即可
    s = list(s)
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    low = 0
    high = len(s) - 1
    while low < high:
        while s[low] not in vowel_list and low < high:
            low += 1
        while s[high] not in vowel_list and low < high:
            high -= 1
        s[low], s[high] = s[high], s[low]
        low += 1
        high -= 1
    return ''.join(s)


if __name__ == '__main__':
    s = "lintcode"
    print(reverseVowels(s))