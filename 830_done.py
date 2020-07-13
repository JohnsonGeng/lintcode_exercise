'''
问题描述：
给出一个字符串，以字符在串中出现的次数为第一关键字，字典序为第二关键字排序字符串。

示例：
Input: str = "bloomberg"
Output: "bbooeglmr"
Explanation:
'b'和'o'出现次数最多，但是'b'字典序较小，排名第一，其次是'o'，以此类推.


'''

'''

知识点：Python中sorted函数的key参数用法，当多关键字排序时，可以使用lambda函数

'''


def stringSort(str):
    # Write your code here

    count_dict = {}
    result = []
    string = ''

    for c in str:
        if count_dict.get(c):
            count_dict[c] += 1
        else:
            count_dict[c] = 1

    for key in count_dict.keys():
        result.append([count_dict[key], key])

    result = sorted(result, key=lambda x: (-x[0], x[1]))

    for ele in result:
        string += ele[1] * ele[0]

    return string

if __name__ == '__main__':
    str = "bloomberg"
    print(stringSort(str))