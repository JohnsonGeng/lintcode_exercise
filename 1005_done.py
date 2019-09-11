'''
问题描述：平面上有一系列点。返回由其中三个点可以形成的三角形最大面积。
示例：
输入： points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
输出： 2
解释：
这五个点如图所示，红色三角形面积最大。

思路：暴力法三重循环

'''


def largestTriangleArea(points):
    # write your code here
    max_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                area = 1/2 * abs(points[i][0] * (points[j][1] - points[k][1]) + points[j][0] * (
                            points[k][1] - points[i][1]) + points[k][0] * (points[i][1] - points[j][1]))
                if area > max_area:
                    max_area = area
                else:
                    continue
    return max_area

if __name__ == '__main__':
    points = [[4, 6], [6, 5], [3, 1]]
    print(largestTriangleArea(points))