'''
问题描述：给一个数组，如果数组中存在相同数字，
且至少有两个相同数字的距离小于给定值k，输出YES，否则输出NO。

示例：
输入: array = [1,2,3,1,5,9,3] 和 k = 4
输出: "YES"
解释:
index为3的1和index为0的1距离为3，满足题意输出YES。

思路：利用一个字典，记录数据出现的位置，再出现该数据的话
相减看是否小于k值。如果不满足，更新位置值，后移，直到扫描完数组。

'''


def sameNumber(self, nums, k):
    # Write your code here
    index_dict = {}
    for i in range(len(nums)):
        # 第一次出现，记录下索引值
        if nums[i] not in index_dict:
            index_dict[nums[i]] = i
        # 重复出现
        else:
            if i - index_dict[nums[i]] < k:
                return 'YES'
            else:
                # 更新索引值
                index_dict[nums[i]] = i
    return 'NO'