class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for pair in adjacentPairs:
            adjList[pair[0]].append(pair[1])
            adjList[pair[1]].append(pair[0])

        res = []
        for k, v in adjList.items():
            if len(v) == 1:
                res.append(k)
                res.append(v[0])
                break

    
        while len(res) <= len(adjacentPairs):
            for neigh in adjList[res[-1]]:
                if neigh != res[-2]:
                    res.append(neigh)
                    break


        
        return res



        