class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        data = dict()
        for word in words:
            for l in word:
                data[l] = data.get(l, 0) + 1
        
        for v in data.values():
            if v % len(words) != 0:
                return False
        
        return True
        