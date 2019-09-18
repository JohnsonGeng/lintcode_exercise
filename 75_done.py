'''
问题描述：
你给出一个整数数组(size为n)，其具有以下特点：
相邻位置的数字是不同的
A[0] < A[1] 并且 A[n - 2] > A[n - 1]
假定P是峰值的位置则满足A[P] > A[P-1]且A[P] > A[P+1]，
返回数组中任意一个峰值的位置。

示例：
	输入:  [1, 2, 1, 3, 4, 5, 7, 6]
	输出:  1 or 6

	解释:
	返回峰顶元素的下标

思路：二分法搜索


'''


def findPeak(A):
    # write your code here
    # 思路1:死找
    # 这个算法时间复杂度过高，会超时
    # for i in range(1,len(A)-1):
    #     if A[i] > A[i-1]  and A[i] > A[i+1]:
    #         return i
    #     else:
    #         continue

    # 思路2:折半查找
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
            return mid
        # 到右边去找
        elif A[mid] > A[mid - 1] and A[mid] < A[mid + 1]:
            low = mid + 1
        # 到左边去找
        elif A[mid] < A[mid - 1] and A[mid] > A[mid + 1]:
            high = mid - 1
        # 随便去一边找
        else:
            low =  mid - 1


if __name__ == '__main__':
    A = [100,102,104,7,9,11,4,3]
    print(findPeak(A))