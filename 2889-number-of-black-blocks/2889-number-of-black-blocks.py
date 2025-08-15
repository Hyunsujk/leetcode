class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        rows = m
        cols = n
        black_cells = set(map(tuple, coordinates))
        block_counts = defaultdict(int)

        for x, y in black_cells:
            for xm in (0, -1):
                for ym in (0, -1):
                    topX = x + xm
                    topY = y + ym
                    if 0 <= topX < rows - 1 and 0 <= topY < cols - 1:
                        block_counts[(topX,topY)] += 1

        res = [0] * 5

        for count in block_counts.values():
            res[count] += 1
        
        total_blocks = (rows-1) * (cols-1)
        res[0] = total_blocks - sum(res[1:])
        
        return res

        