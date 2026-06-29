class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = list()
        heapq.heappush_max(heap, (a, "a"))
        heapq.heappush_max(heap, (b, "b"))
        heapq.heappush_max(heap, (c, "c"))

        ret = [""]
        prev = None
        dupe = False
        while heap:
            v, c = heapq.heappop_max(heap)
            if v <= 0:
                continue
            dupe = c == ret[-1]
            ret.append(c)
            v -= 1
            # print(ret, v, c)

            if prev:
                heapq.heappush_max(heap, prev)
            
            if v > 0:
                if dupe:
                    prev = (v, c)
                    continue
                prev = None
                heapq.heappush_max(heap, (v, c))
            else:
                prev = None


        return "".join(ret)

        