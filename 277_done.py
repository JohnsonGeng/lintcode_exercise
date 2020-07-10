'''
问题描述：给出一系列单词 words，以及两个不同的单词 wordA 和 wordB，
请找出最近的两个 wordA 和 wordB 的间距。
如果 words 中不存在 wordA 或 wordB，那么返回 -1

示例：
Input：["hello","world","say","hello"]
"hello"
"world"
Output：1

'''


def wordSpacing(words, wordA, wordB):
    # write your code here.
    # 时间复杂度是O(n*n)的版本

    # 不存在返回-1
    if wordA not in words or wordB not in words:
        return -1

    # 遍历取下标
    wordA_index = []
    wordB_index = []
    for i in range(len(words)):
        if words[i] == wordA:
            wordA_index.append(i)
        elif words[i] == wordB:
            wordB_index.append(i)
        else:
            continue

    # 暴力求解距离
    min_len = 100000
    for eleA in wordA_index:
        for eleB in wordB_index:
            if abs(eleA - eleB) < min_len:
                min_len = abs(eleA - eleB)
            else:
                continue

    return min_len