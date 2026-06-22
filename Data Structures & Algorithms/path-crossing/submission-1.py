class Solution:
    def isPathCrossing(self, path: str) -> bool:
        traversed = {(0,0)}
        x = y = 0
        for p in path:
            if p == 'N':
                y += 1
            elif p == 'S':
                y -= 1
            elif p ==  'W':
                x -= 1
            elif p == 'E':
                x +=1
            else:
                raise Exception("Invalid path", p)
            loc = (x, y)
            # print(loc, traversed)
            if loc in traversed:
                return True
            traversed.add(loc)
        return False