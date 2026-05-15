class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = list()
        for i in range(n + 1):
            bit = 1
            count = 0
            while bit <= n:
                if bit & i:
                    count += 1
                bit = bit << 1
            ret.append(count)
        return ret