'''
问题描述：写一个函数，其以无符号整数为输入，
而输出对应二进制数所具有的“1”的位数（也被称为汉明权重）。
示例：
输入：n = 11
输出：3
解析：11(10) = 1011(2), 返回 3
思路：
除2求余即可放入数组即可。统计数组中1的个数。
'''

class Solution:
    """
    @param n: an unsigned integer
    @return: the number of â1' bits
    """
    def hammingWeight(self, n):
        # write your code here
        # 思路：除2求余即可放入数组即可。
        binary_list = []
        residue = 0
        count = 0
        while n >= 1:
            residue = n % 2
            binary_list.append(residue)
            n = int(n/2)
        for ele in binary_list:
            if ele == 1:
                count += 1
        return count