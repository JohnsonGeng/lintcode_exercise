'''
问题描述：给定一个字符串表示学生出勤记录，记录仅由下列三个字符组成：

'A' : 缺席（Absent）.
'L' : 迟到（Late）.
'P' : 到场（Present）.
如果学生的出勤情况不包含 超过一个'A'(缺席) 或者 超过连续两个'L'(迟到) ，那么他就应该受到奖励。

返回该学生是否会受到奖励。

示例：输入: "PPALLP"
输出: True

思路：循环扫描字符串，计数'A'出现的次数，同时利用下标判断'L'是都连续出现3次

'''

def checkRecord(s):
    # Write your code here
    index = 0
    absent_count = 0
    while index <= len(s) - 1:
        if s[index] == 'A':
            absent_count += 1
            if absent_count > 1:
                return False
            index += 1
        elif index > 1 and s[index] == 'L' and s[index - 1] == 'L' and s[index - 2] == 'L':
            return False
        else:
            index += 1
            continue
    return True