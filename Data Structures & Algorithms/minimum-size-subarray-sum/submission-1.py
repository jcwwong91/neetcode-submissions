class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        cur = 0
        ret = 0

        while end < len(nums):
            while cur >= target:
                if not ret:
                    ret = end - start
                else:
                    ret = min(ret, end-start)
                cur -= nums[start]
                start += 1
            cur += nums[end]
            end += 1

        while cur >= target:
            if not ret:
                ret = end - start
            else:
                ret = min(ret, end-start)
            cur -= nums[start]
            start += 1
        return ret
