class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            v = abs(nums[i]) - 1
            if v < 0 or v >= len(nums):
                # print("skip", i)
                continue
            
            if nums[v] == 0:
                nums[v] = -1
            elif nums[v] > 0:
                nums[v] = -nums[v]
            # print(i, nums)
        
        # print(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1

        