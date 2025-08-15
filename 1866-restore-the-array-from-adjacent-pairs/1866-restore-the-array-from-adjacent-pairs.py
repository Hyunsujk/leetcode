class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for n1, n2 in adjacentPairs:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        head = next(k for [k, v] in adjList.items() if len(v) == 1)

        res = []
        def dfs(node, prev):
            res.append(node)
            for neigh in adjList[node]:
                if neigh != prev:
                    dfs(neigh, node)
        
        dfs(head, None)
        return res


        

        