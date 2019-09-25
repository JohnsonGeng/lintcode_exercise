'''
问题描述：我们正在玩猜数游戏。 游戏如下：
我从 1 到 n 选择一个数字。 你需要猜我选择了哪个号码。
每次你猜错了，我会告诉你这个数字与你猜测的数字相比是大还是小。
你调用一个预定义的接口 guess(int num)，它会返回 3 个可能的结果(-1，1或0):
-1代表这个数字小于你猜测的数
1代表这个数字大于你猜测的数
0代表这个数字等于你猜测的数

示例：
输入 : n = 10, 我选择了 4 (但是你不知道)
输出 : 4

思路：典型的二分查找问题

'''


import random
class Guess:
    # 具体Guess类的源代码没有给出，自己写了一个
    def __init__(self, n):
        self.num = random.randint(1, n)

    def guess(self,compare_num):
        if compare_num == self.num:
            return 0
        elif compare_num > self.num:
            return -1
        else:
            return 1


def guessNumber(n):
    # Write your code here
    low = 1
    high = n
    mid = int((low + high) / 2)
    while low <= high:
        if Guess.guess(mid) == 0:
            return mid
        elif Guess.guess(mid) == -1:
            high = mid - 1
        else:
            low = mid + 1
        mid = int((low + high) / 2)