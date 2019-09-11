'''
问题描述：给一个整数，返回其 7进制 的字符串表示
示例：
输入: num = 100
输出: 202

思路：思路：先判断正负号，取绝对值，然后除7求余加入列表，
     最后将列表逆序再连接即可。

'''


def convertToBase7(num):
    # Write your code here
    # 思路：先判断正负号，取绝对值，然后除7求余加入列表，最后将列表逆序再连接即可。
    positive = False
    result = []
    if num >= 0:
        positive = True
    #为了方便起见，以正数进行除7求余
    num = abs(num)
    while num >= 1:
        mod = num % 7
        result.append(str(mod))
        num = int(num / 7)
    print(result)
    if positive:
        result.reverse()
        #注意：join的方法处理的列表中的元素必须都是字符类型，如果是数字会报错
        return ''.join(result)
    else:
        result.append('-')
        result.reverse()
        return ''.join(result)

if __name__ == '__main__':
    num = -7
    print(convertToBase7(num))