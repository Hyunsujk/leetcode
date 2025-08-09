"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        visited = {}

        def helper(n):
            if n in visited:
                return visited[n]

            if n not in visited:
                copy = Node(n.val)
                visited[n] = copy

                for neighbor in n.neighbors:
                    copy.neighbors.append(helper(neighbor))
                
                return copy
        
        return helper(node)

        