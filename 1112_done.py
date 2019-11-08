'''
问题描述：集合S中原本包含数字1到n。
但不幸的是，由于数据错误集合中的一个数变成了集合中的另一个数。
这导致集合中有两个重复的数，并且集合中缺失了1到n的某个数。
给定数组nums，表示发生错误后的数组，以数组的形式返回重复的数值和缺失的数值。
示例：
1.输入: nums = [1,2,2,4]
  输出: [2,3]
2.输入: nums = [1,3,3,4]
  输出: [3,2]
思路：利用字典存储出现过的元素，重复出现的则为重复出现的元素。然后遍历字典，没有出现的元素则为缺失的元素。
'''

class Solution:
    """
    @param nums: an array
    @return: the number occurs twice and the number that is missing
    """
    def findErrorNums(self, nums):
        # Write your code here
        # 计算列表长度
        length = len(nums)
        hash_dict= {}
        for element in nums:
            if element not in hash_dict.keys():
                hash_dict[element] = 1
            else:
                repeat_num = element
        for i in range(1, length+1):
            if i in hash_dict.keys():
                continue
            else:
                miss_num = i
        return [repeat_num, miss_num]
