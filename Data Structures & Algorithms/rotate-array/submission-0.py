class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        modifications = 0
        i = 0
        while modifications < len(nums):
            start = i
            j = (i + k) % len(nums)
            tmp = nums[i]
            while modifications < len(nums):
                tmp2 = nums[j]
                nums[j] = tmp
                tmp = tmp2
                # print(tmp, nums, i, j)
                i = j
                j = (i + k) % len(nums)
                modifications += 1
                if i == start:
                    break
            i += 1


        