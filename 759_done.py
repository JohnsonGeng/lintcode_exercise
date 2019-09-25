'''
问题描述：计算在时钟中以 h:m 时刻的时针和分针之间的角度。

示例：
Input: h = 12, m = 0.
Output: 0

思路：计算时针和分针之间差（划算成分钟计算，如2点换算成2*5=10）
如果是负值利用求余实现，再转换成180度的比值，计算角度

'''


def timeAngle(h, m):
    # write your code here
    distance = ((h * 5 - m + 5 * (m / 60))+60)%60
    if distance >= 30:
        distance = 60 - distance
    rate = distance / 30
    return 180 * rate

if __name__ == '__main__':
    print(timeAngle(2, 57))