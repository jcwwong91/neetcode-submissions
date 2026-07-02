class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        spot = dict()
        for i in range(len(order)):
            spot[order[i]] = i
        
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            same = True
            for j in range(min(len(w1), len(w2))):
                c1, c2 = w1[j], w2[j]
                if spot[c1] > spot[c2]:
                    return False
                if c1 != c2:
                    same = False
                    break
            
            if same and len(w2) < len(w1):
                return False
        
        return True

        