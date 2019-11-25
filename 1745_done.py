'''
问题描述：
如果数组是单调递增或单调递减的，那么它是单调的。
如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。
如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
当给定的数组 A 是单调数组时返回 true，否则返回 false。

示例1：
输入：[1,2,2,3]
输出：true

示例2：
输入：[1,3,2]
输出：false

思路：这题比较坑，需要反着来。你无法确定到底是升序还是降序
所以设两个布尔变量来保存升序还是降序，一旦遍历过程中不符合要求，
那么将布尔类型的变量置为False。

'''


def isMonotonic(A):
    # Write your code here.
    # 一个元素的特殊情况
    increase = True
    decrease = True
    if len(A) == 1:
        return True

    # 单调递增
    for i in range(len(A) - 1):
        if A[i] <= A[i + 1]:
            continue
        else:
            increase = False
            break

    # 单调递减
    for j in range(len(A) - 1):
        if A[j] >= A[j + 1]:
            continue
        else:
            decrease = False
            break

    return increase or decrease

if __name__ == '__main__':
    A = [1, 3, 2]
    print(isMonotonic(A))