class Solution:
    def countSubstrings(self, s: str) -> int:
        
        palindrones = 0
        def oddPalindrone(center):
            nonlocal palindrones
            l = center - 1
            r = center + 1
            palindrones += 1

            while l >= 0 and r < len(s):
                # print("comparing", s[l], s[r], l, r)
                if s[l] != s[r]:
                    break
                palindrones += 1
                l -= 1
                r += 1

        def evenPalindrone(center):
            nonlocal palindrones
            l = center
            r = center + 1
            while l >= 0 and r < len(s):
                # print("comparing", s[l], s[r], l, r)
                if s[l] != s[r]:
                    # print("breaking", l, r)
                    break
                palindrones += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            oddPalindrone(i)
            evenPalindrone(i)
        
        return palindrones
        
        