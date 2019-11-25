'''
问题描述：
给定一个整数数组，其中1 ≤ a[i] ≤ n (n =数组的大小)，
一些元素出现两次，其他元素出现一次。
找到 [1,n] 中所有没有出现在此数组中的元素。

示例：
输入:
[4,3,2,7,8,2,3,1]
输出:
[5,6]

思路：
使用python中的集合来存放元素

'''

class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """
    def findDisappearedNumbers(self, nums):
        # write your code here
        # 思路：使用python中的集合来存放元素
        s = set()
        result = []
        for num in nums:
            s.add(num)
        for i in range(1, len(nums)+1):
            if i in s:
                continue
            else:
                result.append(i)
        return result