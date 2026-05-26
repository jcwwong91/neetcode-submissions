class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        handCount = int(len(hand) / groupSize)

        frequency = dict()
        for n in hand:
            frequency[n] = frequency.get(n, 0) + 1

        for i in range(handCount):
            heap = list()
            for k, v in frequency.items():
                heapq.heappush(heap, (v, k))
            v, k = heapq.heappop(heap)
            # print(k, v)
            for j in range(groupSize):
                idx = k + j
                frequency[idx] = frequency.get(idx, 0) - 1
                if frequency[idx] < 0:
                    # print(f'Missing in hand {i} starting {v}, on {idx}')
                    return False
                elif frequency[idx] == 0:
                    del(frequency[idx])

        
        return True
        