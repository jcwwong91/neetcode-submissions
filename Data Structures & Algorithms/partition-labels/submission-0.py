class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ends = dict()
        for i in range(len(s)):
            c = s[i]
            ends[c] = i
        
        
        intervals = list()
        for i in range(len(s)):
            c = s[i]
            j = ends[c]
            if not intervals or intervals[-1][1] < i:
                intervals.append([i, j])
            
            if j > intervals[-1][1]:
                intervals[-1][1] = j

        ret = list()
        for (i,j) in intervals:
            ret.append(j-i+1)            

        return ret