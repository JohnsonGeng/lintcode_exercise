'''
问题描述：给定一系列的会议时间间隔，
包括起始和结束时间[[s1,e1]，[s2,e2]，…(si < ei)，
确定一个人是否可以参加所有会议。

示例：
输入: intervals = [(0,30),(5,10),(15,20)]
输出: false
解释:
(0,30), (5,10) 和 (0,30),(15,20) 这两对会议会冲突

思路：按照每个会议的开始时间进行排序。
然后再从第二个会议开始每个会议的开始时间和前面会议的结束时间相比较。
如果大于则继续，小于则返回。

'''

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals):
        sorted_intervals = sorted(intervals, key = lambda x:x.start)
        for i in range(1,len(sorted_intervals)):
            if sorted_intervals[i].start >= sorted_intervals[i-1].end:
                continue
            else:
                return False
        return True