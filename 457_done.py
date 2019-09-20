'''
问题描述：在一个排序数组中找一个数，返回该数出现的任意位置，如果不存在，返回 -1。

示例：
输入：nums = [1,2,2,4,5,5], target = 2
输出：1 或者 2

思路：典型的二分查找问题


'''

def findPosition(nums, target):
    # write your code here
    low = 0
    high = len(nums) - 1
    mid = int((low + high) / 2)
    if not nums:
        return -1
    while low <= high:
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
        mid = int((low + high) / 2)
    return -1

if __name__ == '__main__':
    nums = [1, 2]
    target = 2
    print(findPosition(nums, target))