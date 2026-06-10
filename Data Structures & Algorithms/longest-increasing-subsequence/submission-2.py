class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            longest = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    longest = max(longest, dp[j])
            dp[i] = longest + 1
            # print(dp)
        return max(dp) 


