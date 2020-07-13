'''
问题描述：
给出两个数组，写出一个方法求出它们的交集。

示例：
Input : nums1 = [1, 2, 2, 1], nums2 = [2, 2],
Output : [2]


'''

'''

知识点：Python中dict和set是哈希表，进行in操作会快很多。
而list和tuple只是简单的数组，只是暴力循环。

'''


def intersection(nums1, nums2):
    # write your code here

    # 方法1：太耗时了，无法通过
    # result = []

    # for ele in nums1:
    #     if ele in nums2 and ele not in result:
    #         result.append(ele)
    #     else:
    #         continue

    # result = sorted(result)

    # 方法2：用集合

    set1 = set()
    set2 = set()

    for ele1 in nums1:
        set1.add(ele1)
    for ele2 in nums2:
        if ele2 in set1:
            set2.add(ele2)
    result = list(set2)

    return result