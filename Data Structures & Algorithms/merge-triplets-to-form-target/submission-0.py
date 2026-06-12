class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first, second, third = False, False, False
        for (a, b, c) in triplets:
            if a == target[0] and b <= target[1] and c <= target[2]:
                first = True
            if a <= target[0] and b == target[1] and c <= target[2]:
                second = True
            if a <= target[0] and b <= target[1] and c == target[2]:
                third = True
        
        return first and second and third