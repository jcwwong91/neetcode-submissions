class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxSize = 0
        start = 0
        end = 1
        seen = {s[0]: 1}
        maxChar = s[0]

        while end < len(s):
            print(start, end, s[start:end+1])
            c = s[end]
            seen[c] = seen.get(c, 0) + 1
            if seen[c] > seen[maxChar]:
                maxChar = c
            
            # print("------", seen)
            if (end - start - seen[maxChar]+1) > k:
                cc = s[start]
                seen[cc] -= 1

                start += 1
                # print("dec", start, end, s[start:end+1])

            end += 1
            maxSize = max(maxSize, end-start)
            

        return maxSize