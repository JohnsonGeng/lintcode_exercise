'''
问题描述：给一个<Point>的List p，
求满足p[i].x+p[j].x和p[i].y+p[j].y（i < j)都能被2整除的(i,j)对数。
示例：
输入: p = [[1,2],[3,4],[5,6]]
输出: 3
解释:
p[0],p[1],p[2]两两组合，他们x与y之和都能被2整除。
思路：扫描p，计算 <奇数，奇数> <偶数，偶数> <奇数，偶数> <偶数，奇数>的组合有多少个

'''


def pairNumbers(p):
    # Write your code here
    odd_odd = 0
    even_even = 0
    odd_even = 0
    even_odd = 0
    for i in range(len(p)):
        #
        if p[i].x % 2 == 1 and p[i].y % 2 == 1:
            odd_odd += 1
        elif p[i].x % 2 == 0 and p[i].y % 2 == 0:
            even_even += 1
        elif p[i].x % 2 == 1 and p[i].y % 2 == 0:
            odd_even += 1
        else:
            even_odd += 1

    sum = int(
        odd_odd * (odd_odd - 1) / 2 + even_even * (even_even - 1) / 2 + even_odd * (even_odd - 1) / 2 + odd_even * (
                    odd_even - 1) / 2)
    return sum