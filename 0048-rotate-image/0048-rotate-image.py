class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 0 0 => 0 n-0: 2
        # 0 1 => 1 n-0: 2
        # 0 n => n n-0: 2
        # 1 0 => 0 n-1: 1
        # 1 1 => 1 n-1: 1
        # 1 2 => 2 n-1: 1
        n = len(matrix[0])
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if str(matrix[i][j])[0] != ' ':
                    matrix[i][j], matrix[j][-(i+1)], matrix[-(i+1)][-(j+1)], matrix[-(j+1)][i] = \
                    ' '+str(matrix[-(j+1)][i]), ' '+str(matrix[i][j]), ' '+str(matrix[j][-(i+1)]), ' '+str(matrix[-(i+1)][-(j+1)])
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                matrix[i][j] = int(matrix[i][j].strip())