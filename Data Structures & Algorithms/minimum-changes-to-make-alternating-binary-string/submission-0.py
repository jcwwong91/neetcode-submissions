class Solution:
    def minOperations(self, s: str) -> int:
        
        changes1 = changes2 = 0
        for i in range(len(s)):
            if s[i] == '0':
                if i % 2:
                    changes1 += 1
                else:
                    changes2 += 1
            else:
                if i % 2:
                    changes2 += 1
                else:
                    changes1 += 1

        return min(changes1, changes2)