class Solution:
    def checkValidString(self, s: str) -> bool:

        low = 0
        high = 0

        for i in range(len(s)):
            c = s[i]
            if c == '(':
                low = max(low, 0) + 1
                high += 1
            elif c == ')':
                low = max(low -1, 0)
                high -= 1
            elif c == '*':
                low = max(low -1, 0)
                high += 1
            
            if high < 0:
                return False


        
        return low <= 0 <= high