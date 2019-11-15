'''
问题描述：
给一整数 n,
我们需要求前n个自然数形成的集合的所有可能子集中所有元素的和。
示例：
输入 : n = 2
输出 : 6
说明 :
可能的子集为 {{1}, {2}, {1, 2}}.
子集的元素和为 1 + 2 + 1 + 2 = 6
思路：
：数学问题，每个数出现2^(n-1)次，1+2+3+……+n的和是n*(n+1)/2
'''

class Solution:
    """
    @param n: the given number
    @return: Sum of elements in subsets
    """
    def subSum(self, n):
        # write your code here
        # 思路：数学问题，每个数出现2^(n-1)次，1+2+3+……+n的和是n*(n+1)/2
        return int((n*(n+1)/2)*(2**(n-1)))