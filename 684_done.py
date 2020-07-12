'''
问题描述：给出两个字符串，你需要找到缺少的字符串

示例：
Input : str1 = "This is an example", str2 = "is example"
Output : ["This", "an"]

'''


def missingString(str1, str2):
    # Write your code here
    result = []
    # 方法1:直接对字符串进行切割
    str1_list = str1.split()
    str2_list = str2.split()

    for str in str1_list:
        if str not in str2_list:
            result.append(str)

    return result