class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top_r = 0
        bottom_r = len(matrix)-1

        while top_r <= bottom_r:
            temp = matrix[top_r]
            matrix[top_r] = matrix[bottom_r]
            matrix[bottom_r] = temp
            top_r += 1
            bottom_r -= 1

        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        return matrix