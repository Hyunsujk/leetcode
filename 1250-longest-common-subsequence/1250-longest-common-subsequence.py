class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l2 = len(text2)
        prev_row = [0] * (l2+1)
        curr_row = [0] * (l2+1)

        for s in text1:
            for i in range(1, l2 + 1):
                if s == text2[i-1]:
                    curr_row[i] = prev_row[i-1] + 1
                else:
                    curr_row[i] = max(prev_row[i], curr_row[i-1])
            prev_row, curr_row = curr_row, prev_row

        return prev_row[-1]

        