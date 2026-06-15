class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sp = 0
        tp = 0

        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                tp += 1
            
            sp += 1

        return len(t) - tp