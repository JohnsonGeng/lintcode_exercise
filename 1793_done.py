'''
问题描述：给定了一系列销售数字，求最小索引元素的索引是什么。
使得最小索引元素的左侧和右侧的所有元素的总和相等。该阵列可能无法重新排序。
例如，给定数组sales = [1,2,3,4,6]，我们看到1 + 2 + 3 = 6，
使用基于零的索引，sales [3] = 4是寻求的值。索引是3。

示例：
输入 : [1, 2, 3, 4, 6]
输出 : 3

思路：分别计算左右结点的累积和，然后遍历sales判断某个位置的左右前缀和是否相等

'''


def BalancedSalesArray(sales):
    # write your code here
    # 分别计算左右结点的累积和，然后遍历sales判断某个位置的左右前缀和是否相等
    left_prefix = []
    right_prefix = []
    sum_left = 0
    sum_right = 0
    for i in range(len(sales)):
        sum_left += sales[i]
        left_prefix.append(sum_left)
    sales.reverse()
    for j in range(len(sales)):
        sum_right += sales[j]
        right_prefix.append(sum_right)
    sales.reverse()
    right_prefix.reverse()
    for k in range(1, len(sales) - 1):
        if left_prefix[k - 1] == right_prefix[k + 1]:
            return k
        else:
            continue
    return -1

if __name__ == '__main__':
    sales = [1, 2, 3, 4, 6]
    print(BalancedSalesArray(sales))