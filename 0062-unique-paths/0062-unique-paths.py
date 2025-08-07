class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        above_row = [1]*n

        for i in range(m-1):
            current_row = [1]*n
            for k in range(1, len(current_row)):
                current_row[k] = current_row[k-1] + above_row[k]

            above_row = current_row

        return above_row[-1] 