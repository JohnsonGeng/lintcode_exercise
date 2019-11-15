'''
问题描述：给定一个整数数组nums，编写一个返回此数组的“中心索引”的方法。
我们将中心索引定义为：中心索引左边的数字之和等于中心索引右边的数字之和。
如果不存在这样的中心索引，我们应该返回-1。 如果有多个中心索引，则应返回最左侧的那个。

示例：
输入:
nums = [1, 7, 3, 6, 5, 6]
输出: 3
解释:
索引3 (nums[3] = 6)左侧所有数之和等于右侧之和。
并且3是满足条件的第一个索引。

思路：分别记录左前缀和以及右前缀和，遍历数组判断左右前缀和是否相等即可。
用于存储前缀和。
'''


def pivotIndex(self, nums):
    # Write your code here
    # 思路：分别记录左前缀和以及右前缀和，遍历数组判断左右前缀和是否相等即可。
    # 用于存储前缀和
    left_prefix = []
    l_prefix = 0
    right_prefix = []
    r_prefix = 0
    # 计算左前缀数组
    for i in range(len(nums)):
        l_prefix += nums[i]
        left_prefix.append(l_prefix)
    # 计算右前缀数组
    for j in range(len(nums) - 1, -1, -1):
        r_prefix += nums[j]
        right_prefix.append(r_prefix)
    right_prefix.reverse()
    # 特殊情况判断---空数组
    if not nums:
        return -1
    # 特殊情况判断---右前缀第二个元素为0
    if right_prefix[1] == 0:
        return 0
    for n in range(1, len(nums) - 1):
        if left_prefix[n - 1] == right_prefix[n + 1]:
            return n
        else:
            continue
    #  # 特殊情况判断---左前缀倒数第二个元素为0
    if left_prefix[-2] == 0:
        return len(right_prefix) - 1
    return -1

if __name__ == '__main__':
    nums = [-1, -1, 0, 1, 1, 0]
    print(pivotIndex(nums))
