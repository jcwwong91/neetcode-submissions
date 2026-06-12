class Solution:
    def myPow(self, x: float, n: int) -> float:
        ret = 1
        if n > 0:
            for i in range(n):
                ret = ret * x
        elif n < 0:
            for i in range(-n):
                ret = ret / x
        return ret
        