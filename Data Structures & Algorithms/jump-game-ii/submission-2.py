class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        jumps = 0
        while i < (len(nums) - 1):
            # print("cur", i, (len(nums)- 1))
            bestPos = None
            bestJumpPos = None
            for j in range(1, nums[i] + 1):
                pos = i + j
                jumpPos = pos + nums[pos] if pos < len(nums) else len(nums) - 1
                jumpPos = min(jumpPos, len(nums)-1)
                if not bestJumpPos or jumpPos >= bestJumpPos:
                    bestJumpPos = jumpPos
                    bestPos = pos
            jumps += 1
            # print(f'jump {jumps} from {i}({nums[i]}) to {bestPos}({nums[bestPos]})')
            i = bestPos

        return jumps