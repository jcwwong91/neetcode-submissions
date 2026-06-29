# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        def helper(node):
            if not node.left and not node.right:
                return (node.val, 0)
            
            rob = node.val
            not_rob = 0
            if node.left:
                r, nr = helper(node.left)
                rob += nr
                not_rob += max(r, nr)
            if node.right:
                r, nr = helper(node.right)
                rob += nr
                not_rob += max(r, nr)
            
            return (rob, not_rob)
        return max(helper(root))
        
        