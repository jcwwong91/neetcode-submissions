class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        digit = ""
        cur = ""
        stack = list()
        while i < len(s):
            c = s[i]
            if '0' <= c <= '9':
                digit += c
            elif c == '[':
                stack.append((int(digit), cur))
                digit = ""
                cur = ""
            elif c == ']':
                dupe = cur
                count, cur = stack.pop()
                for _ in range(count):
                    cur = cur + dupe
            else:
                cur = cur + c

            i += 1
        return cur

