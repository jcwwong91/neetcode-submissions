class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()
        for i in range(len(nums)):
            v = nums[i]
            if v in seen:
                diff = abs(i - seen[v])
                if diff <= k:
                    return True
            seen[v] = i
        return False