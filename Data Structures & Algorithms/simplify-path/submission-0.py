class Solution:
    def simplifyPath(self, path: str) -> str:
        
        i = 0
        parts = path.split("/")
        stack = list()
        
        for part in parts:
            if part == "." or part == "":
                continue
            if part == "..":
                if stack:
                    stack.pop()
                continue
            stack.append(part)  
        
        return "/" + "/".join(stack)
