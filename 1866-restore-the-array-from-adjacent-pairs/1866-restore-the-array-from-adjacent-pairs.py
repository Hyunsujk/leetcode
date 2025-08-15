class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for n1, n2 in adjacentPairs:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        head = next(k for [k, v] in adjList.items() if len(v) == 1)

        res = [head]
        visited = set([head])

        while len(res) < len(adjList):
            last = res[-1]
            for neigh in adjList[last]:
                if neigh not in visited:
                    res.append(neigh)
                    visited.add(neigh)
                    break

        return res


        

        