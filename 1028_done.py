'''

问题描述：X是一个好数当且仅当单独旋转每一个数位180度之后，能够得到一个合法的不同于X的数。
每一个数位必须被旋转我们不能选择不管它。
如果每一个数位在旋转之后仍然是一个数位，那么这个数字是合法的。
0,1和8旋转保持不变; 2和5旋转后互相变换; 6和9旋转后互相变换，其余数字旋转后不会变成任何数字所以是不合法的。
现在给定一个正数 N，多少1 到 N 之间的数X是好的?

示例：
Input : 10
Ouptput : 4
Explanation :
在[1, 10]之内存在4个好数：2, 5, 6, 9.
注意1和10不是好数，因为它们在旋转之后没有变化。
样例2:

'''


'''

知识点：熟练使用set

'''
def rotatedDigits1(N):
    # write your code here
    # 存在3，4，7的都不是好数
    # 仅存在0，1，8的也不是好数

    illegal_list = ['3', '4', '7']
    # unchange_list = ['0', '1', '8']
    legal_list = ['2', '5', '6', '9']
    result = []
    count = 0

    for i in range(1, N+1):
        # 转换成字符串
        str_num = str(i)
        # 对其中的每一个字符进行判断
        flag_illegal = False
        flag_legal = False
        for c in  str_num:
            if c in illegal_list:
                flag_illegal = True
                break
            if c in legal_list:
                flag_legal = True
        if flag_legal and not flag_illegal:
            count += 1
            result.append(int(str_num))

    print(result)

    return count

def rotatedDigits2(N):

    count = 0
    result = []
    for i in range(1, N + 1):
        # 转换成字符串
        num_set = set(list(str(i)))
        if '3' in num_set or '4' in num_set or '7' in num_set:
            continue
        if '2' in num_set or '5' in num_set or '6' in num_set or '9' in num_set:
            count += 1
            result.append(i)

    print(result)

    return count

if __name__ == '__main__':
    print(rotatedDigits1(6610))
    print(rotatedDigits2(6610))