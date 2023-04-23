# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def buildTree(node, children):
            if len(children) == 1:
                if children[0] > node:
                    node = TreeNode(node)
                    node.right = TreeNode(children[0])
                else:
                    node = TreeNode(node)
                    node.left = TreeNode(children[0])
                return node

            if not children:
                node = TreeNode(node)
                return node

            left = []
            right = []
            for i in children:
                if i < node:
                    left.append(i)
                else:
                    right.append(i)

            curNode = TreeNode(node)
            if left:
                leftBranch = buildTree(left[0], left[1:])
                curNode.left = leftBranch
            if right:
                rightBranch = buildTree(right[0], right[1:])
                curNode.right = rightBranch
            return curNode
            
        return buildTree(preorder[0], preorder[1:])