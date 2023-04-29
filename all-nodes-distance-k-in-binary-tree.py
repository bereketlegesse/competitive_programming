# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def traverse(node):
            if node.left:
                graph[node.left.val].append(node.val)
                graph[node.val].append(node.left.val)
                traverse(node.left)
            if node.right:
                graph[node.right.val].append(node.val)
                graph[node.val].append(node.right.val)
                traverse(node.right)

        traverse(root)
        queue = deque()
        queue.append(target.val)
        visited = set()

        while queue and k:
            curLen = len(queue)
            k -= 1
    
            for _ in range(curLen):
                node = queue.popleft()
                visited.add(node)
                for child in graph[node]:
                    if child in visited:
                        continue
                    queue.append(child)
                    
        return list(queue)