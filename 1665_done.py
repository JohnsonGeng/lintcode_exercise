'''
问题描述：给出一个十进制数num，现在你需要把它转成二进制数，并返回1的个数和位置。
示例：
输入: 10
输出: [2,1,3]
解释: 10转成2进制为1010，总共有2个1，所以ouptput数组第一个是2。
然后1的位置是第1个和第3个，所以后续两个数为1，3.
思路：
求余存入列表，并将列表逆序即可，统计其中1的个数和位置。
'''

class Solution:
    """
    @param num: the num
    @return: the array subject to the description
    """
    def calculateNumber(self, num):
        # Write your code here.
        # 思路：求余存入列表，并将列表逆序即可，统计其中1的个数和位置。
        binary_list = []
        result = []
        count = 0
        while num >= 1:
            residue = num % 2
            binary_list.append(residue)
            num = int(num/2)
        # 将列表逆
        binary_list.reverse()
        for i in range(len(binary_list)):
            if binary_list[i] == 1:
                count += 1
                result.append(i+1)
        result.insert(0, count)
        return result