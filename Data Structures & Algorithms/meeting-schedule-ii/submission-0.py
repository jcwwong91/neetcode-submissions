"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

START = 1
END = 0

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        events = list()

        for interval in intervals:
            heapq.heappush(events, (interval.start, START))
            heapq.heappush(events, (interval.end, END))


        maxRooms = 0
        rooms = 0
        while events:
            ev = heapq.heappop(events)
            if ev[1] == START:
                rooms += 1
                maxRooms = max(maxRooms, rooms)
            else:
                rooms -= 1

        return maxRooms


        