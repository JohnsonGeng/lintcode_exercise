'''
问题描述：
在霍格沃茨魔法学校里面，有一个简单的时间魔法，
可以将当前的时间转换到最大的时间，但是只能修改几个固定的位置。
最长时间是23:59，最短时间是00:00，表示时间的格式为hh:mm
例如：现在是"2?:2?"，那么可以转换的最大时间为"23:29"

示例：
输入: "?4:5?"
输出: "14:59"
样例解释: 返回最大的时间。

思路：
很简单，对应第几位取能取得的最大的数就好了，但是注意特殊情况



'''


def timeMagic(newTime):
    # 思路：很简单，对应第几位取能取得的最大的数就好了，但是注意特殊情况
    newTime = list(newTime)
    for i in range(len(newTime)):
        if newTime[i] == '?':
            if i == 0:
                if newTime[i + 1] == '?':
                    newTime[i] = '2'
                else:
                    if int(newTime[i + 1]) <= 3:
                        newTime[i] = '2'
                    else:
                        newTime[i] = '1'
            elif i == 1:
                if int(newTime[i - 1]) == 2:
                    newTime[i] = '3'
                else:
                    newTime[i] = '9'
            elif i == 3:
                newTime[i] = '5'
            else:
                newTime[i] = '9'
        else:
            continue
    return ''.join(newTime)


if __name__ == '__main__':
    newTime = '??:??'
    print(timeMagic(newTime))