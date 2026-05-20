class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        reference = 0
        for i in range(len(nums)+1):
            reference = reference ^ i
        
        for n in nums:
            reference = reference ^ n

        
        return reference