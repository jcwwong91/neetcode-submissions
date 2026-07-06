class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        total = 0
        prev = None
        for c in s:
            if prev and lookup[prev] < lookup[c]:
                total -= (2 * lookup[prev])
            total += lookup[c]
            prev = c
            print(c, total)

        return total

            