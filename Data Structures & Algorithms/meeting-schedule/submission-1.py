"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda interval: interval.end)
        time = -1
        for interval in intervals:
            if interval.start >= time:
                time = interval.end
            else:
                return False
        
        return True
        
