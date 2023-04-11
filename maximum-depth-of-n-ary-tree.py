"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        stack = []
        stack.append((root, 1))
        maxDep = 0
        while stack:
            node, depth = stack.pop()
            maxDep = max(maxDep, depth)
            for child in node.children:
                stack.append((child, depth + 1))
                
        return maxDep