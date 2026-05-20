class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = list()
        for interval in intervals:
            # Before
            if newInterval and interval[1] < newInterval[0]:
                ret.append(interval)
                continue

             # After
            if not newInterval or newInterval[1] < interval[0]:
                if newInterval:
                    ret.append(newInterval)
                    newInterval = None
                ret.append(interval)
                continue

            

            # Overlapping
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])
            # ecompass
            # Overlapping end

        if newInterval:
            ret.append(newInterval)

        return ret
        