"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        importance = dict()
        totalImportance = 0
        for i in employees:
            graph[i.id] = i.subordinates
            importance[i.id] = i.importance
        
        def dfs(node):
            nonlocal totalImportance
            if not graph[node]:
                totalImportance += importance[node]
                return
            totalImportance += importance[node]
            for neighbor in graph[node]:
                dfs(neighbor)
                
        dfs(id)  
        return totalImportance