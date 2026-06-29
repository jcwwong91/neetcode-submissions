# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def helper(node):
            if not node.left and not node.right:
                return node.val == target
            
            if node.left and helper(node.left):
                node.left = None
            if node.right and helper(node.right):
                node.right = None
            
            return not node.left and not node.right and node.val == target

        if helper(root):
            return None

        return root
        