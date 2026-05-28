# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sums = dict()
        maxSum = None

        if not root:
            return 0

        def dfs(node):
            nonlocal maxSum

            if not node.left and not node.right:
                sums[node] = node.val
                if maxSum is None:
                    maxSum = sums[node]
                maxSum = max(maxSum, sums[node])
                # print(node.val)
                return
            

            leftST = 0
            rightST = 0
            if node.left:
                dfs(node.left)
                leftST = sums[node.left]
            if node.right:
                dfs(node.right)
                rightST = sums[node.right]

            sums[node] = max(leftST + node.val, rightST + node.val, node.val)
            maxSum = max(maxSum, leftST + node.val + rightST, sums[node])
            # print(node.val, sums[node], maxSum, leftST, rightST)
            
            return

        dfs(root)
        return maxSum