class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()
        def helper(node):
            q = deque([node])
            while q:
                n = q.popleft()
                visited.add(n)
                for neigh in adjList[n]:
                    if neigh not in visited:
                        q.append(neigh)
        
        count = 0
        for i in range(n):
            if i not in visited:
                helper(i)
                count += 1
        
        return count