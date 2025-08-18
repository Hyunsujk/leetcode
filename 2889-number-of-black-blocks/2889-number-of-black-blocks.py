class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        subblock_set = defaultdict(int)

        for [x, y] in coordinates:
            for x_change in [0, -1]:
                for y_change in [0, -1]:
                    top_row = x + x_change
                    top_col = y + y_change
                    if 0 <= top_row < m - 1 and 0 <= top_col < n - 1:
                        subblock_set[(top_row, top_col)] += 1
        
        res = [0] * 5
        for count in subblock_set.values():
            res[count] += 1
        
        res[0] = (m-1)*(n-1) - sum(res[1:])

        return res



        