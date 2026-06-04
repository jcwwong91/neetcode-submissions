class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        candidate_count = 2
        candidates = dict()

        for n in nums:
            if n in candidates:
                candidates[n] += 1
            elif len(candidates) < candidate_count:
                candidates[n] = 1
            else:
                for k in list(candidates.keys()):
                    candidates[k] -= 1
                    if candidates[k] == 0:
                        del(candidates[k])

        ret = list()
        for k in candidates.keys():
            if nums.count(k) > len(nums) / 3:
                ret.append(k)
        return list(ret)