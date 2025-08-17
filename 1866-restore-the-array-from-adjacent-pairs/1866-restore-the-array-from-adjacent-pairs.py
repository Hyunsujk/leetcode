class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for pair in adjacentPairs:
            one = pair[0]
            two = pair[1]
            adjList[one].append(two)
            adjList[two].append(one)
        
        entry = next(k for k, v in adjList.items() if len(v) == 1)

        res = []
        visited = set()

        def dfs(node):
            res.append(node)
            visited.add(node)
            for neigh in adjList[node]:
                if neigh not in visited:
                    return dfs(neigh)
        
        dfs(entry)
        return res

        