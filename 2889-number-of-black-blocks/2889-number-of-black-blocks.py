class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        rows = m
        cols = n
        counts = defaultdict(int)

        for r, c in coordinates:
            for rc, cc in [(-1, 0), (0, 0), (0, -1), (-1, -1)]:
                nr = r + rc
                nc = c + cc
                if 0 <= nr < rows - 1 and 0 <= nc < cols - 1:
                    counts[(nr, nc)] += 1
        
        res = [0] * 5
        for c in counts.values():
            res[c] += 1
        totalBlocks = (rows-1) * (cols-1)
        res[0] = totalBlocks - sum(res[1:])
        return res
