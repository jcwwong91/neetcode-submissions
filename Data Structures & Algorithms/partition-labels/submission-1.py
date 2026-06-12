class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ends = dict()
        for i in range(len(s)):
            c = s[i]
            ends[c] = i
        
        
        ret = list()
        first = last = -1
        for i in range(len(s)):
            c = s[i]
            j = ends[c]
            if first < 0 or last < i:
                if first >= 0:
                    ret.append(last - first + 1)
                first = i
                last = j
            
            if j > last:
                last = j

        ret.append(last - first + 1)  

        return ret