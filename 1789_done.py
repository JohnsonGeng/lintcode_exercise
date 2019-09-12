'''
问题描述：给出一组用户名，如果有重复的请求在用户名后添加数字区别，返回修改后的数组。

示例：
输入：["aa", "bb", "cc", "bb", "aa", "aa", "aa"]
输出：["aa","bb","cc","bb1","aa1","aa2","aa3"]
解释：
"bb"第二次出现输出为"bb1"
"aa"第二次出现输出为"aa1"
"aa"第三次出现输出为"aa2"
"aa"第四次出现输出为"aa3"

思路：思路：利用字典记录某个元素出现了多少次，扫描数组，
     查看字典中是否出现，并加上出现次数即可

'''


def DistinguishUsername(names):
    # Write your code here
    # 思路：利用字典记录某个元素出现了多少次，扫描数组，查看字典中是否出现，并加上出现次数即可
    # 创建字典记录某个元素出现了多少次
    dict = {}
    for i in range(len(names)):
        # 第一次出现
        if names[i] not in dict.keys():
            dict[names[i]] = 0
        # 重复出现
        else:
            dict[names[i]] += 1
            names[i] = names[i] + str(dict[names[i]])
    return names