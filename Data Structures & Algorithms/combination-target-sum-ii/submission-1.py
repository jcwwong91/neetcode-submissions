class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ret = list()
        def helper(begin, stack, current):
            nonlocal ret
            for i in range(begin, len(candidates), 1):
                n = candidates[i]
                if i > begin and n == candidates[i-1]:
                    continue

                current += n
                stack.append(n)
                if current < target:
                    # print(current, stack)
                    helper(i + 1, stack, current)
                if current == target:
                    # print(current, stack, "added")
                    ret.append(stack.copy())
                
                stack.pop()
                current -= n

        helper(0, list(), 0)
        return ret