class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        exist = set()
        missing = set()
        for n in range(1, len(nums)+1):
            missing.add(n)

        duplicate = None
        for n in nums:
            if n in exist:
                duplicate = n
                continue
            exist.add(n)
            missing.discard(n)
        return [duplicate, next(iter(missing))]