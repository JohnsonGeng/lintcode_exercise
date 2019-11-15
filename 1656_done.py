'''
问题描述：
给定n个整数和两个正整数L,R，输出有多少个数的数值范围在[L, R]之间。

示例：
Input: a=[1,2,3,4,5,6],L=3,R=5
Output: 3
Explaination:
Only a[2],a[3],a[4] are in range of [3,5].

思路1:可以先排序再找，可以节省查找的时间，但是排序的时间无法避免最快O(nlog2n)
思路2：暴力查找，一个个查找即可。
'''

class Solution:
    """
    @param a: the array a
    @param L: the integer L
    @param R: the integer R
    @return: Return the number of legal integers
    """
    def getNum(self, a, L, R):
        # Write your code here
        # 思路1:可以先排序再找，可以节省查找的时间，但是排序的时间无法避免最快O(nlog2n)
        # 思路2：暴力查找，一个个查找即可。
        # 这里实现暴力查找
        count = 0
        for i in range(len(a)):
            if a[i] >= L and a[i] <= R:
                count += 1
        return count