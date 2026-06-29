class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        ret = list()
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            # outside
            if firstList[i][1] < secondList[j][0]:
                i += 1
                continue
            if secondList[j][1] < firstList[i][0]:
                j += 1

            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            ret.append((start, end))


            if firstList[i][1] < secondList[j][1]:
                i +=1
            elif firstList[i][1] > secondList[j][1]:
                j += 1
            else:
                i += 1
                j += 1
        return ret