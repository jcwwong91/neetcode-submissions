class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = dict()
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        frequency = [None] * (len(nums) + 1)
        for kk, v in counts.items():
            # print(kk, v, frequency)
            if not frequency[v]:
                frequency[v] = list()
            frequency[v].append(kk)

        # print(frequency)
        ret = list()
        for i in range(len(frequency)-1, -1, -1):
            # print(i, ret, len(ret), k, len(ret) >= k)
            if len(ret) >= k:
                break
            
            if frequency[i]:
                ret = ret + frequency[i]
        
        return ret

        