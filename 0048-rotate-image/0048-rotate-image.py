class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)//2
        for i, row in enumerate(matrix[:n+1]):
            for j, num in enumerate(row[:n+1]):
                if str(matrix[i][j])[0] != ' ':
                    matrix[i][j], matrix[j][-(i+1)], matrix[-(i+1)][-(j+1)], matrix[-(j+1)][i] = \
                    ' '+str(matrix[-(j+1)][i]), ' '+str(matrix[i][j]), ' '+str(matrix[j][-(i+1)]), ' '+str(matrix[-(i+1)][-(j+1)])
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                matrix[i][j] = int(matrix[i][j].strip())