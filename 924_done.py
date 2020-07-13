'''
问题描述：
给出一个单词列表和两个单词单词1,单词2，返回列表中这两个单词之间的最短距离。

示例：
Input：["practice", "makes", "perfect", "coding", "makes"],"coding","practice"
Output：3
Explanation：index("coding") - index("practice") = 3

'''
import time


def shortestDistance1(words, word1, word2):
    # Write your code here

    # 最简单方法，两层for循环，速度比较慢。Bruce-Force
    start = time.time()
    min_distance = len(words)

    for i in range(len(words)):
        if words[i] == word1:
            for j in range(len(words)):
                if words[j] == word2:
                    if abs(i - j) < min_distance:
                        min_distance = abs(i - j)
                else:
                    continue
        else:
            continue
    end = time.time()
    print(end-start)

    return min_distance

def shortestDistance2(words, word1, word2):
    start = time.time()
    # 遍历一遍，每次只和最近的元素进行比较
    min_distance = len(words)

    index_1 = -1
    index_2 = -1

    for i in range(len(words)):
        if word1 == words[i]:
            index_1 = i
            if index_2 > -1:
                min_distance = min(min_distance, abs(i - index_2))
        if word2 == words[i]:
            index_2 = i
            if index_1 > -1:
                min_distance = min(min_distance, abs(i - index_1))
    end = time.time()
    print(end-start)

    return min_distance


if __name__ == '__main__':
    words = ["practice","makes","perfect","coding","makes"]
    word1 = "coding"
    word2 = "practice"
    print(shortestDistance1(words, word1, word2))
    print(shortestDistance2(words, word1, word2))