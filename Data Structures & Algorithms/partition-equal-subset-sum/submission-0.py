class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target = sum(nums) / 2
        if not target.is_integer():
            return False
        target = int(target)
        
        dp = set()
        dp.add(nums[0])
        if nums[0] > target:
            return False
        if nums[0] == target:
            return True

        for i in range(1, len(nums)):
            toAdd = set()
            if nums[i] == target:
                return True
            toAdd.add(nums[i])
            for v in dp:
                newSum = v + nums[i]
                if newSum > target:
                    continue
                if newSum == target:
                    return True
                
                toAdd.add(newSum)
            dp.update(toAdd)
            # print(dp)
        return False