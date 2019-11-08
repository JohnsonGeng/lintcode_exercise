'''
问题描述：给定一个整数数组，找到三个元素，使乘积最大，返回该积。
示例：
1. 输入: [1,2,3]
   输出: 6
2. 输入: [1,2,3,4]
   输出: 24
思路：
    考虑全正、全负以及有正有负的情况
    1.全正取列表中最大的三个元素
    2.全负取列表中最小的三个元素
    3.有正有负的话去最小的两个以及最大的一个元素（不必考虑0）
'''

class Solution:
    """
    @param nums: an integer array
    @return: the maximum product
    """
    def maximumProduct(self, nums):
        # Write your code here
        # 首先将数组进行排序
        sorted_nums = sorted(nums)
        # 元素全小于0的情况
        if max(sorted_nums)<0:
            return sorted_nums[0]*sorted_nums[1]*sorted_nums[2]
        # 元素全大于0的情况
        elif min(sorted_nums)>0:
            return sorted_nums[-1]*sorted_nums[-2]*sorted_nums[-3]
        # 有正有负的情况
        else:
            return sorted_nums[0]*sorted_nums[1]*sorted_nums[-1]