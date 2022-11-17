class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr, t):
            left, right = 0, len(arr)-1
            mid = (left + right) // 2
            while left < right:
                if arr[mid] == t:
                    return [True, mid]
                elif arr[mid] < t:
                    left = mid +1
                else:
                    right = mid-1
                mid = (left + right) // 2
            return [False, mid]
        
        first_col = [row[0] for row in matrix]
        found, index1 = binary_search(first_col, target)
        
        if found:
            return True
        if first_col[index1] > target:
            index1 -= 1
        found, index2 = binary_search(matrix[index1], target)
        return True if matrix[index1][index2] == target else False
                