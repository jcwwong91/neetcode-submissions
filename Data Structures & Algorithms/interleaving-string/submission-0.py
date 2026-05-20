class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s3) != len(s1) + len(s2):
            return False
        if len(s3) == 0:
            return True

        results = list()
        for i in range(len(s1)+1):
            results.append([None] * (len(s2) + 1))

        results[-1][-1] = True

        for i in range(len(s1)-1, -1, -1):
            results[i][-1] = results[i+1][-1] and s1[i] == s3[len(s2) + i]

        for i in range(len(s2)-1, -1, -1):
            results[-1][i] = results[-1][i+1] and s2[i] == s3[len(s1) + i]
    
        for i in range(len(s1)-1, -1, -1):
            for j in range(len(s2)-1, -1, -1):
                pos = i + j
                results[i][j] = (s3[pos] == s1[i] and results[i+1][j]) or (s3[pos] == s2[j] and results[i][j+1])



        # printResults(results)
        return results[0][0]



def printResults(results):
    print("----------------------")
    for row in results:
        print(row)