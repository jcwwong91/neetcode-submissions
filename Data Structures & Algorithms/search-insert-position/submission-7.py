class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        if nums[-1] < target:
            return len(nums)
        if nums[0] >= target:
            return 0

        count = 0
        while l <= r:
            
            m = ((r - l) // 2) + l
            # print(f'{nums[l]}({l}) - {nums[m]}({m}) - {nums[r]}({r})')
            if nums[m] == target:
                return m
            elif nums[m] > target:
                if nums[m-1] < target:
                    return m
                r = m - 1
            else:
                l = m + 1

        return l