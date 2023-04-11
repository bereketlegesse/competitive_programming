# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPathSum = root.val

        def backtrack(node):
            nonlocal maxPathSum
            if not node:
                return 0

            leftPath = backtrack(node.left)
            rightPath  = backtrack(node.right)
            combinedPath = leftPath+rightPath+node.val
            maxPathSum = max(maxPathSum,combinedPath)
            path = node.val + max(leftPath,rightPath)
            maxPathSum = max(maxPathSum,path,node.val)
            return max(node.val,path)

        backtrack(root)
        return maxPathSum