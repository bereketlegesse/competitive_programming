# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(node, prev):
            nonlocal total 
            if not node.left and not node.right:
                total += (prev*10 + node.val)
                return

            if not node.right:
                cur = (prev * 10 + node.val)
                return dfs(node.left, cur)

            if not node.left:
                cur = (prev * 10 + node.val)
                return dfs(node.right, cur)

            if node.left and node.right:
                cur = (prev * 10 + node.val)
                dfs(node.left, cur)
                return dfs(node.right, cur)

        dfs(root, 0)
        return total