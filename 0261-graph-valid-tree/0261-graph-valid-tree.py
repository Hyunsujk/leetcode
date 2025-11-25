class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adjList = defaultdict(list)
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()
        
        def dfs(node, parent):
            visited.add(node)
            for neigh in adjList[node]:
                if neigh == parent:
                    continue
                if neigh in visited:
                    return False
                if not dfs(neigh, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n

