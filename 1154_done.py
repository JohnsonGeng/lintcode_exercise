'''

问题描述：
给定一个表示某学生出勤情况的字符串，‘A’代表出勤，‘D’代表缺勤，‘L’代表迟到。
若该学生出现两次及以上缺勤或者连续三次及以上迟到则需要接受惩罚。
请你判断该学生是否该接受惩罚并返回布尔类型。

示例：
Input : “AADALLLAD”
Output : true
Explanation : 这名学生违约两次并且连续迟到三次，所以他应该受到惩罚。


'''
def judge(record):
    # Write your code here.

    countD = 0

    for i in range(len(record)):
        if record[i] == 'D':
            countD += 1
        # 连续三天迟到
        elif i < len(record ) -2 and record[i] == record[ i +1] == record[ i +2] == 'L':
            return True
        else:
            continue

    if countD >= 2:
        return True
    else:
        return False