'''
问题描述：
给出n个数和m个询问，每个询问包含两个整数L,R，
对于每个询问输出有多少数满足取值范围在[L, R]

示例：
输入：a=[1,2,3,4,5,6],q=[[1,2],[1,5]]
输出： [2,5]
说明：
对于第一个询问，a[0],a[1]是合法的
对于第二个询问，a[0],a[1],a[2],a[3]是合法的

思路：
直接暴力法。但是效率比较低

'''

class Solution:
    """
    @param a: the array a
    @param q: the queries q
    @return: for each query, return the number of legal integers
    """
    def getAns(self, a, q):
        # write your code here
        # 思路：直接暴力法。不知道会不会时间超时
        result_list = []
        for query in q:
            count = 0
            for num in a:
                if num >= query[0] and num <= query[1]:
                    count += 1
            result_list.append(count)
        return result_list