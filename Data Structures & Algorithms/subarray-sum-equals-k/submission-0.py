class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = {0:1}
        cur = 0
        results = 0
        for n in nums:
            cur += n
            target = cur - k
            results += prefixes.get(target,0)
            # print(n, cur, target, prefixes)
            prefixes[cur] = prefixes.get(cur, 0) + 1
        return results

        