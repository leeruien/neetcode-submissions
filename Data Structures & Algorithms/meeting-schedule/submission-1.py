"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x:x.start)
        # second start time will always be after the first start time
        index = 0
        length = len(intervals)
        if length ==0: return True
        for i in intervals:
            start = i.start
            end = i.end
            if index+1 <= length - 1:
                start2 = intervals[index + 1].start
                end2 = intervals[index + 1].end
                if start2 >= end:
                    index += 1
                    continue
                else: return False
            else: return True



