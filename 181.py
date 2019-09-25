'''
问题描述：
如果要将整数n转换为m，需要改变多少个bit位？

示例：
Input: n = 31, m = 14
Output:  2

Explanation:
(11111) -> (01110) there are two different bits.


'''


def bitSwapRequired(a, b):
    # write your code here
    result = a ^ b
    count = 0
    for i in range(32):
        if result&(result-1) != 0:
            count += 1
            result = result&(result-1)
    return count

if __name__ == '__main__':
    print(bitSwapRequired(1, -1))