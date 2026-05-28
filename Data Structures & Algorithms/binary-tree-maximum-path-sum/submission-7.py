# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = None

        if not root:
            return 0

        def dfs(node):
            nonlocal maxSum

            if not node.left and not node.right:
                v = node.val
                if maxSum is None:
                    maxSum = v
                maxSum = max(maxSum, v)
                # print(node.val)
                return v
            

            leftST = 0
            rightST = 0
            if node.left:
                leftST = dfs(node.left)

            if node.right:
                rightST = dfs(node.right)

            v = max(leftST + node.val, rightST + node.val, node.val)
            maxSum = max(maxSum, leftST + node.val + rightST, v)
            # print(node.val, sums[node], maxSum, leftST, rightST)
            
            return v

        dfs(root)
        return maxSum