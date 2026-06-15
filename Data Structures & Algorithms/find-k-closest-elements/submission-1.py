class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = list()

        for n in arr:
            diff = abs(x - n)
            if len(heap) < k:
                heapq.heappush_max(heap, (diff, n))
                continue
            if heap[0][0] > diff:
                heapq.heappop_max(heap)
                heapq.heappush_max(heap, (diff, n))
                continue
        
        ret = [0] * k
        for i in range(k):
            ret[i] = heap[i][1]

        ret.sort()
        return ret