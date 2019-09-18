'''
问题描述：给一个有 2n 个整数的数组，
你的任务是把这些整数分成 n 组，如(a1, b1)，(a2, b2)，...，(an, bn)。
并且使得 i 从 1 到 n 的 min(ai, bi)之和尽可能的大。

示例：输入: [1,4,3,2]
输出: 4
解释: n 是 2, 最大的数对和为 4 = min(1, 2) + min(3, 4)。

思路：先对数组进行升序排序，然后从小到大两两组合，累加即可。

'''


def arrayPairSum(nums):
    # Write your code here
    # 先对数组进行升序排序，然后从小到大两两组合，累加即可
    sum = 0
    sorted_nums = sorted(nums)
    for i in range(0, len(sorted_nums), 2):
        sum += sorted_nums[i]
    return sum