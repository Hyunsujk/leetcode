class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        rank = defaultdict(int)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            
            if rootX == rootY:
                return False

            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootY] > rank[rootX]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True

        for a, b in edges:
            if a not in parent:
                parent[a] = a
            if b not in parent:
                parent[b] = b
            
            if not union(a, b):
                return [a, b]