class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for n, m in adjacentPairs:
            adjList[n].append(m)
            adjList[m].append(n)
        
        head = next(n for n, neigh in adjList.items() if len(neigh) == 1)

        arr = []
        visited = set()

        def dfs(node):
            arr.append(node)
            visited.add(node)
            for neigh in adjList[node]:
                if neigh not in visited:
                    return dfs(neigh)

        dfs(head)
        return arr
