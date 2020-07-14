'''
问题描述：
给出了两个A和B的列表，从A映射到B，B是由A的一种回文构词法构成通过随机化A中元素的顺序来实现的。
我们想要找到一个指数映射P，从A到B，映射P[i] = j表示A出现在B中的第i个元素。
这些列表A和B可能包含重复。如果有多个答案，输出任何一个。

示例：
Input : A =[12, 28, 46, 32, 50] 和 B =[50, 12, 32, 46, 28]
Output : [1, 4, 3, 2, 0]
Explanation :
P[0] = 1，因为A的第0个元素出现在B[1]， P[1] = 4，因为A的第一个元素出现在B[4]，以此类推。


'''


def anagramMappings(A, B):
    # Write your code here
    # 方法1：暴力法即可
    mapping = []
    for ele_a in A:
        for i in range(len(B)):
            if ele_a == B[i]:
                index = i
            else:
                continue
        mapping.append(index)

    # TODO
    # 方法2:使用哈希表，时间复杂度O(n+n)

    return mapping
