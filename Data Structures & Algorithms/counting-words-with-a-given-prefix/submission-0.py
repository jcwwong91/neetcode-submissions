class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for w in words:
            found = True
            if len(w) < len(pref):
                continue
            for i in range(len(pref)):
                if pref[i] != w[i]:
                    found = False
                    break
            if found:
                count +=1
        
        return count