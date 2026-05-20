class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def mergeInterval(i1, i2):
            return [min(i1[0], i2[0]), max(i1[1], i2[1])]

        intervals.sort()
        ret = list()
        for interval in intervals:
            # print(ret)
            if not ret:
                ret.append(interval)
                continue

            if ret[-1][1] < interval[0]:
                ret.append(interval)
                continue

            ret[-1] = mergeInterval(ret[-1], interval)

        return ret
        