'''
问题描述：
给一组整数，按照升序排序，使用选择排序，冒泡排序，
插入排序或者任何 O(n2) 的排序算法。

示例：
Input :  [3, 2, 1, 4, 5]
Output :  [1, 2, 3, 4, 5]

'''

'''

知识点：python的sorted函数做了一定的优化，比普通的排序会快很多。

'''

def sortIntegers(A):
    # write your code here
    # # 方法1:自己写的冒泡排序，时间比较慢
    # for i in range(len(A)):
    #     for j in range(len(A)-1, i, -1):
    #         if A[j] < A[j - 1]:
    #             A[j], A[j - 1] = A[j - 1], A[j]
    #         else:
    #             continue
    #
    # return A

    # 方法2：sorted函数，会快很多
    A = sorted(A)
    return A

if __name__ == '__main__':
    print(sortIntegers([3,2,1,4,5]))