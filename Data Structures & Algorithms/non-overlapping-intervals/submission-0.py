class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        removals = 0
        time = -50001
        intervals = sorted(intervals, key=lambda i: i[1])
        for interval in intervals:
            s, e = interval[0], interval[1]
            if s >= time:
                time = e
            else:
                removals += 1


        return removals