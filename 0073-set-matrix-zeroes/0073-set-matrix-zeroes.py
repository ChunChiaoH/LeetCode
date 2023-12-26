class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        flag_i = set()
        flag_j = set()
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if num == 0:
                    flag_i.add(i)
                    flag_j.add(j)
                    
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if i in flag_i or j in flag_j:
                    matrix[i][j] = 0