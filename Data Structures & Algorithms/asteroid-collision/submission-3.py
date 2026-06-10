class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = list()
        for v in asteroids:
            if not stack:
                stack.append(v)
                continue
            
            if stack[-1] < 0:
                stack.append(v)
                continue
            
            # positive stack
            if v > 0:
                stack.append(v)
                continue
            
            destroyed = False
            while stack and stack[-1] > 0:
                if stack[-1] == -v:
                    destroyed = True
                    stack.pop()
                    break
                if stack[-1] > -v:
                    destroyed = True
                    break
                
                stack.pop()
            
            if not destroyed:
                stack.append(v)
            
            # print(stack)
        
        return stack