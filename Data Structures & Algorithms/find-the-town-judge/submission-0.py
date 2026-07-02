class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        reputation = [0] * (n + 1)
        trustCount = [0] * (n + 1)

        for t in trust:
            reputation[t[1]] += 1
            trustCount[t[0]] += 1

        for i in range(1, n+1):
            if trustCount[i] != 0:
                continue
            if reputation[i] != n - 1:
                continue
            return i

        return -1
        