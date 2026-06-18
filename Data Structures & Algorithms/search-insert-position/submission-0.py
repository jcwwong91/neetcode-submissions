class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            n = nums[i]
            if n >= target:
                return i

        return len(nums)