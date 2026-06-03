class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp1 = [0] * len(nums) # rob first house
        dp2 = [0] * len(nums) # don't rob first house

        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        dp2[1] = nums[1]

        for i in range(2, len(nums)-1, 1):

            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])
            dp2[i] = max(dp2[i-2] + nums[i], dp2[i-1])
        
        dp1[-1] = dp1[-2]
        dp2[-1] = max(dp2[-3] + nums[-1], dp2[-2])

        # print(dp1)
        # print(dp2)

        return max(dp1[-1], dp2[-1])