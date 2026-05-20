class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        reference = 0
        for i in range(len(nums)):
            reference = reference ^ i
            reference = reference ^ nums[i]

        reference = reference ^ len(nums)

        return reference