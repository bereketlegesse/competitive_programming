# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        totalSum = 0

        def dfs(parent, grandParent, node):
            nonlocal totalSum
            if not node:
                return

            if grandParent % 2 == 0:
                totalSum += node.val
                
            dfs(node.val, parent, node.left)
            dfs(node.val, parent, node.right)

        dfs(1,1,root)
        return totalSum