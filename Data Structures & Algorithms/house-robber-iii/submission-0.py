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
                node.rob = node.val
                node.not_rob = 0
                # print(node.val, node.rob, node.not_rob)
                return
            
            rob = node.val
            not_rob = 0
            if node.left:
                helper(node.left)
                rob += node.left.not_rob
                not_rob += max(node.left.rob, node.left.not_rob)
            if node.right:
                helper(node.right)
                rob += node.right.not_rob
                not_rob += max(node.right.rob, node.right.not_rob)
            
            node.rob = rob
            node.not_rob = not_rob
            # print(node.val, node.rob, node.not_rob)
        helper(root)
        return max(root.rob, root.not_rob)
        
        