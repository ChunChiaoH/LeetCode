class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary tree (by artod@Leetcode)
        row, col = len(matrix)-1 , 0
        while row >= 0 and col <= len(matrix[0])-1:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else: # matrix[row][col] > target
                row -= 1
        return False