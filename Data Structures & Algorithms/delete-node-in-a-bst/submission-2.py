# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None
        node = root
        parent = None
        while node:
            if node.val == key:
                break
            parent = node
            if key < node.val:
                node = node.left
            else:
                node = node.right

        if not node:
            return root

        if not node.left or not node.right:
            child = node.left if node.left else node.right
            if parent:
                if parent.left == node:
                    parent.left = child
                else:
                    parent.right = child
            else:
                if node.left:
                    return node.left
                else:
                    return node.right
        else:
            toDelete = node
            par = None
            node = node.right
            while node.left:
                par = node
                node = node.left    
            if par:
                par.left = node.right
            node.left = toDelete.left
            if toDelete.right != node:
                node.right = toDelete.right

            if toDelete == root:
                return node

            if parent.left == toDelete:
                parent.left = node
            else:
                parent.right = node
            
        return root

        