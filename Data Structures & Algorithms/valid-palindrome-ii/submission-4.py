class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        step = 0 # 0 - no deletions, 1 - delete right, 2 - delete left
        ll = rr = None

        while l < r:
            # print(f'{s[l]}({l}) - {s[r]}({r}) - {step}')
            if s[l] != s[r]:
                if step == 0:
                    ll = l
                    rr = r
                    r -= 1
                    step = 1
                    continue
                elif step == 1:
                    l = ll + 1
                    r = rr
                    step = 2
                    continue
                else:
                    return False
            l += 1
            r -= 1
        return True