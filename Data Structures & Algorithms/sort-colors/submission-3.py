class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        r = i = 0
        b = len(nums) - 1

        i = 0
        while i <= b:
            if nums[i] == 0:
                nums[i] = nums[r]
                nums[r] = 0
                r += 1
            elif nums[i] == 2:
                nums[i] = nums[b]
                nums[b] = 2
                b -= 1
                i -= 1
            i += 1
