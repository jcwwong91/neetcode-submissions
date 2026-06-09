class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        ret = ""
        while p1 < len(word1) and p2 < len(word2):
            ret = ret + str(word1[p1]) + str(word2[p2])
            p1 += 1
            p2 += 1
        
        if p1 < len(word1):
            ret = ret + word1[p1:]

        if p2 < len(word2):
            ret = ret + word2[p2:]
        return ret
        