class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = list()

        def helper(current, stack, begin):
            nonlocal ret
            for i in range(begin, len(nums), 1):
                n = nums[i]
                stack.append(n)
                current += n
                if current < target:
                    helper(current, stack, i)
                if current == target:
                    # print(current, stack)
                    ret.append(stack.copy())
                
                current -= n
                stack.pop()

        helper(0, [], 0)
        return ret