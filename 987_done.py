'''
问题描述：给一个正整数，检查它的二进制表示是否具有交替位：
        即，两个相邻的位总是具有不同的值。
示例：
输入: 5
输出: True
解释:
5 的二进制表示为: 101
思路：除二求余，不停地将余数加入链表，判断链表中的数是否交替
'''


def hasAlternatingBits(n):
    # Write your code here
    # 思路：除2求余，不断地将余数加入数组，判断数组是否交替出现0和1即可
    list = []
    while n >= 1:
        mod = n % 2
        list.append(mod)
        n = int(n / 2)

    if not len(list) or len(list) == 1:
        return False
    else:
        for i in range(1, len(list) - 1):
            if list[i] != list[i - 1] and list[i] != list[i + 1]:
                continue
            else:
                return False
        return True

if __name__ == '__main__':
    print(hasAlternatingBits(11))