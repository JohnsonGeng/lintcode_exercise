'''
问题描述：
给定一个数字，在数字的任意位置插入一个5，使得插入后的这个数字最大。

示例：
Input: 234
Output:  5234

'''


class Solution:
    """
    @param a: A number
    @return: Returns the maximum number after insertion
    """

    def InsertFive(self, a):
        # write your code here
        result = []

        # 取出单个字符
        if a > 0:
            flag = 0
            a = str(a)
            for i in range(len(a)):
                if int(a[i]) > 5 and flag == 0:
                    result.append(a[i])
                else:
                    if flag == 0:
                        result.append('5')
                        result.append(a[i])
                        flag = 1
                    else:
                        result.append(a[i])
            sum = int(''.join(result))
        elif a == 0:
            return 50
        elif a < 0:
            a = -a
            a = str(a)
            flag = 0
            for i in range(len(a)):
                if int(a[i]) < 5 and flag == 0:
                    result.append(a[i])
                else:
                    if flag == 0:
                        result.append('5')
                        result.append(a[i])
                        flag = 1
                    else:
                        result.append(a[i])
            sum = int(''.join(result))
            sum = -sum

        return sum