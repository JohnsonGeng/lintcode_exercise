'''
问题描述：计算在一个 32 位的整数的二进制表示中有多少个 1。
示例：
输入：32
输出：1
解释：
32(100000)，返回 1。

思路：与1（00000.......00000001）,可以得到最后一位是1还是0，不停地左移1位。

'''


def countOnes(num):
    # write your code here

    # 注：这个方法不行，遇到负数的二进制会有问题
    # 思路：不断地求余，统计1的个数
    # count = 0
    # while num >= 1:
    #     mod = num%2
    #     num = int(num/2)
    #     if mod == 1:
    #         count += 1
    #     else:
    #         continue
    # return count

    # 思路：与1（00000.......00000001）,可以得到最后一位是1还是0，不停地左移1位
    count = 0
    for i in range(32):
        count += num & 1
        num >>= 1
    return count
