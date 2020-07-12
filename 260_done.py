'''
问题描述：
给定一个 n * n 的矩阵，如果每一条从左上到右下的斜线上的数值相同，
返回 true， 否则返回false。

示例：
Input：
1，2，3
5，1，2
6，5，1
Output：
True

'''

# 这个速度有点慢，不知道为啥
def judgeSame1(matrix):
    # write your code here.

    # 从最右边的斜线开始遍历即可
    i = len(matrix) - 2
    while (i >= 0):
        # 右上角
        right_i = i
        right_j = 0
        while (right_i < len(matrix) - 1):
            if matrix[right_i][right_j] == matrix[right_i + 1][right_j + 1]:
                pass
            else:
                return False
            # 向右下角移动
            right_i += 1
            right_j += 1
        # 左下角
        left_i = 0
        left_j = i
        while (left_j < len(matrix) - 1):
            if matrix[left_i][left_j] == matrix[left_i + 1][left_j + 1]:
                pass
            else:
                return False
            # 向右下角移动
            left_i += 1
            left_j += 1
        i -= 1

    return True

# 这个快一些
def judgeSame1(matrix):
    # write your code here.
    length = len(matrix)
    for i in range(length):
        left = matrix[0][i]
        right = matrix[i][0]
        for j in range(i, length):
            if left != matrix[j - i][j]:
                return False
            if right != matrix[j][j - i]:
                return False

    return True