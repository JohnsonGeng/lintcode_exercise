'''
问题描述：给出一串整数流和窗口大小，计算滑动窗口中所有整数的平均值。

示例：
MovingAverage m = new MovingAverage(3);
m.next(1) = 1 // 返回 1.00000
m.next(10) = (1 + 10) / 2 // 返回 5.50000
m.next(3) = (1 + 10 + 3) / 3 // 返回 4.66667
m.next(5) = (10 + 3 + 5) / 3 // 返回 6.00000

思路：用数组记录下当前窗口中的数，计算平均值返回即可。

注意：如果不用一个变量保存当前窗口的累计值，
而是最后调用sum函数的话，会导致时间超时。

'''


class MovingAverage:
    """
    @param: size: An integer
    """

    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.window = []
        self.sum = 0

    """
    @param: val: An integer
    @return:  
    """

    def next(self, val):
        # write your code here
        if len(self.window) == self.size:
            self.sum -= self.window[0]
            self.window.pop(0)
            self.window.append(val)
            self.sum += val
        else:
            self.window.append(val)
            self.sum += val
        return (self.sum / len(self.window))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)


if __name__ == '__main__':
    obj = MovingAverage(10)
    print(obj.next(1))
    print(obj.next(2))
    print(obj.next(3))
    print(obj.next(4))
    print(obj.next(5))
    print(obj.next(6))
    print(obj.next(8))
    print(obj.next(9))
    print(obj.next(10))
    print(obj.next(7))
