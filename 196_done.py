'''
问题描述：
给出一个包含 0 .. N 中 N 个数的序列，
找出0 .. N 中没有出现在序列中的那个数。
注意：可以改变序列中数的位置。（也就是说数组中元素不是有序的）

示例：
输入:[0,1,3]
输出:2

思路1：当成数学问题。如果这n+1个数都有的话，和应该是n*(n+1)/2。
    但是现在少了一个数，总和为sum。那么差的那个数就是n*(n+1)/2 -sum。
    时间复杂度为O(N)。
思路2：排序，并逐个比较查找，时间复杂度为O(logN)。


'''


def findMissing1(nums):
    # write your code here
    # 思路1:如果这n+1个数都有的话，和应该是n*(n+1)/2。
    # 但是现在少了一个数，总和为sum
    # 差的那个数就是n*(n+1)/2-sum
    count = 0
    N = len(nums)
    for num in nums:
        count += num
    return int(N*(N+1)/2)-count

def findMissing2(nums):
    # 思路2：排序，并逐个比较查找，时间复杂度为O(logN)
    sorted_nums = sorted(nums)
    for i in range(len(sorted_nums)):
        if i == sorted_nums[i]:
            continue
        else:
            return i
    return i + 1