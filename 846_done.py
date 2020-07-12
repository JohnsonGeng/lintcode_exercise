'''
问题描述：
给定 n 个学生的学号(从 1 到 n 编号)以及他们的考试成绩，
表示为(学号，考试成绩)，请将这些学生按考试成绩降序排序，
若考试成绩相同，则按学号升序排序。

示例：
输入: array = [[2,50],[1,50],[3,100]]
输出: [[3,100],[1,50],[2,50]]

'''


def multiSort1(array):
    # Write your code here
    # 这里采用冒泡排序
    for i in range(len(array) - 1):
        for j in range(len(array) - 1, 0, -1):
            if array[j][1] > array[j - 1][1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            elif array[j][1] == array[j - 1][1]:
                if array[j][0] < array[j - 1][0]:
                    array[j], array[j - 1] = array[j - 1], array[j]
                else:
                    continue
            else:
                continue

    return array

# python自带排序
def multiSort2(array):
    array = sorted(array, key=lambda x: (-x[1], x[0]))
    return array

