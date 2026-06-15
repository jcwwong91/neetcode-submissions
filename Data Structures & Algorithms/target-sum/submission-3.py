class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = dict()
        dp[0] = 1
        
        for n in nums:
            ndp = dict()
            for cur, count in dp.items():
                ndp[cur + n] = ndp.get(cur+n,0) + count
                ndp[cur - n] = ndp.get(cur-n,0) + count
            dp = ndp
            
        return dp.get(target,0)
