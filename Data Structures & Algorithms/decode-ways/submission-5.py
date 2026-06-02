class Solution:
    def numDecodings(self, s: str) -> int:
        results = [0] * (len(s) + 1)
        if s[0] == '0':
            return 0
        results[0] = 1
        results[1] = 1
        
        for i in range(2, len(s) + 1):
            od = int(s[i-1])
            td = int(s[i-2:i])

            if od >= 1:
                results[i] += results[i-1]

            if 10 <= td <= 26:
                results[i] += results[i-2]
            
            print(od, td)
            
            
        print(results)
        return results[-1]
