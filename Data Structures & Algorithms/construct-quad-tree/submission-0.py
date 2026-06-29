"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def helper(x, y, size):
            val = None
            leaf = True
            for i in range(size):
                for j in range(size):
                    v = grid[x+i][y+j]
                    if val is None:
                        val = v
                    elif val != v:
                        leaf = False
            
            if leaf:
                return Node(val, True, None, None, None, None)
            
            newSize = size // 2
            return Node(
                True, 
                False,
                helper(x, y, newSize),
                helper(x, y+newSize, newSize),
                helper(x+newSize, y, newSize),
                helper(x+newSize, y+newSize, newSize)
            )


        
        return helper(0, 0, len(grid))
        