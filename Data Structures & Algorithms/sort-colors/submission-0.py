class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        r = w = b = 0
        
        for n in nums:
            if n == 0:
                r +=1
            elif n == 1:
                w += 1
            else:
                b += 1

        for i in range(r):
            nums[i] = 0
        
        for i in range(w):
            nums[i + r] = 1

        for i in range(b):
            nums[i + r + w] = 2
