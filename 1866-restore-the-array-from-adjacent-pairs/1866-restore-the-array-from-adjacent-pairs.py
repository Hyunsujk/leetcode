class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for pair in adjacentPairs:
            adjList[pair[0]].append(pair[1])
            adjList[pair[1]].append(pair[0])
        
        head = next(k for k, v in adjList.items() if len(v) == 1)
        
        visited = set()
        res = []

        def dfs(node):
            visited.add(node)
            res.append(node)
            for neigh in adjList[node]:
                if neigh not in visited:
                    return dfs(neigh)
        
        dfs(head)
        return res