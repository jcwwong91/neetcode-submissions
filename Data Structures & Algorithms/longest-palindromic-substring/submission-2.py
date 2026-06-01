class Solution:
    def longestPalindrome(self, s: str) -> str:

        def oddPalindrone(center):
            l = center - 1
            r = center + 1

            while l >= 0 and r < len(s):
                # print("comparing", s[l], s[r], l, r)
                if s[l] != s[r]:
                    break
                    
                l -= 1
                r += 1

            return s[l+1:r]

        def evenPalindrone(center):
            l = center
            r = center + 1

            while l >= 0 and r < len(s):
                # print("comparing", s[l], s[r], l, r)
                if s[l] != s[r]:
                    # print("breaking", l, r)
                    break
                l -= 1
                r += 1

            return s[l+1:r]

        ret = s[:1]
        for i in range(len(s)):
            odd = oddPalindrone(i)
            if len(odd) > len(ret):
                ret = odd

            even = evenPalindrone(i)
            if len(even) > len(ret):
                ret = even
            

        return ret
        