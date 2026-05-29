class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = [()]
        nums.sort()

        seen = set()
        for n in nums:
            toAppend = list()
            for v in ret:
                vv = v + (n,)
                if vv in seen:
                    continue
                seen.add(vv)
                toAppend.append(vv)
                
            ret.extend(toAppend)
            # print(ret)
        return ret
                
            
            
        