# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        idxs = dict()
        for i in range(len(inorder)):
            v = inorder[i]
            idxs[v] = i

        pi = 0

        def getSubTree(l, r):

            if l == r:
                return None

            nonlocal pi
            if pi >= len(preorder):
                return None
            v = preorder[pi]
            # print("processing", v, "(", pi, ")",inorder[l:r])
            pi = pi + 1
            if l + 1 == r:
                # print(v, "is leaf")
                return TreeNode(v)
            

            ii = idxs[v]

            # print(v, "left", inorder[l:ii])
            # print(v, "right", inorder[ii+1:r])
            left = getSubTree(l, ii)
            right = getSubTree(ii + 1, r)
            # print(v, "left", left, "right", right)

            return TreeNode(v, left=left, right=right)

            
        root = getSubTree(0, len(inorder))
        return root