class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]

        for n in nums:
            toAppend = list()
            for v in ret:
                vv = v.copy()
                vv.append(n)
                toAppend.append(vv)
                
            ret.extend(toAppend)
            #print(ret)
        return ret
                
            
            