class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = dict()
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        
        heap = list()
        for c, v in counts.items():
            heapq.heappush_max(heap, (v, c))

        ret = ""
        prev = None
        while heap:
            v, c = heapq.heappop_max(heap)
            ret = ret + c
            if prev:
                heapq.heappush_max(heap, prev)
            if v > 1:
                prev = (v-1, c)
            else:
                prev = None
        if prev:
            return ""
        return ret
