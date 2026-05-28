class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tchars = dict()
        remaining = dict()
        for c in t:
            remaining[c] = remaining.get(c, 0) + 1
            tchars[c] = tchars.get(c, 0) + 1

        l = 0
        r = 0   
        schars = dict()
        ret = ""

        while r < len(s):
            c = s[r]
            if c not in tchars:
                r += 1
                continue
            
            schars[c] = schars.get(c, 0) + 1
            if c in remaining:
                remaining[c] -= 1
                if remaining[c] == 0:
                    del(remaining[c])

            while len(remaining) == 0:
                ss = s[l:r+1]
                # print(ss)
                if ret == "" or len(ss) < len(ret):
                    ret = ss
                
                cc = s[l]
                if cc in tchars:
                    schars[cc] = schars[cc] - 1
                    if schars[cc] == 0:
                        del(schars[cc])
                    if schars.get(cc, 0) < tchars[cc]:
                        remaining[cc] = remaining.get(cc, 0) + 1
                l += 1

                


            r += 1


        
        return ret