'''
问题描述：两个整数的Hamming距离是对应比特位不同的个数。
给定两个整数x和y，计算两者的Hamming距离。

示例：输入: x = 1 和 y = 4
输出: 2
解释:
1的二进制表示是001
4的二进制表示是100
共有2位不同

思路1：简单粗暴，分别将x和y换算成二进制，统计相对应的位置上不同的比特数即可。
思路2：异或运算，统计异或后的结果中1的个数即可。


'''


def hammingDistance(x, y):
    # write your code here
    # 思路：异或运算，统计异或后的结果中1的个数即可。
    count = 0
    result = x ^ y
    while result >= 1:
        mod = result % 2
        if mod == 1:
            count += 1
        result = int(result / 2)
    return count


if __name__ == '__main__':
    print(hammingDistance(5, 2))