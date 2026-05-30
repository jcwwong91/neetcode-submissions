class Solution:
    def partition(self, s: str) -> List[List[str]]:


        def isPalindrone(ss):
            i = 0
            j = len(ss) - 1
            while j > i:
                if ss[i] != ss[j]:
                    return False
                i += 1
                j -= 1
            return True

        def helper(ss: str):
            if len(ss) == 1:
                return [[ss]]

            palindrones = list()
            if isPalindrone(ss):
                palindrones.append([ss])

            
            for i in range(1, len(ss)):
                # left = helper(ss[:i])
                if not isPalindrone(ss[:i]):
                    continue
                right = helper(ss[i:])

                for r in right:
                    palindrones.append([ss[:i]] + r)


            return palindrones

            


        ret = helper(s)
        # print(ret)
        return ret
        