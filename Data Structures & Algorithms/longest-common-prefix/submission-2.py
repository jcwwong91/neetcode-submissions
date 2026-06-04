class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ret = ""
        while True:
            if ret == strs[0]:
                return ret
            
            c = strs[0][len(ret)]
            for i in range(1, len(strs)):
                if len(ret) == len(strs[i]) or c != strs[i][len(ret)]:
                    return ret
            ret += c 
        
        return ret