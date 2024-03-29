class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # approch 1: 2 binary search
        #def binary_search(arr, t):
        #    if arr[0] == t:
        #        return [True, 0]
        #    left, right = 0, len(arr)-1
        #    mid = (left + right) // 2
        #    while left < right:
        #        if arr[mid] == t:
        #            return [True, mid]
        #        elif arr[mid] < t:
        #            left = mid +1
        #        else:
        #            right = mid-1
        #        mid = (left + right) // 2
        #    return [arr[mid] == t, mid]
        #
        #first_col = [row[0] for row in matrix]
        #found, index1 = binary_search(first_col, target)
        #if found:
        #    return True
        #if first_col[index1] > target:
        #    index1 -= 1
        #found, index2 = binary_search(matrix[index1], target)
        #return found
        
        # approch 2: binary tree (by artod@Leetcode)
        #row, col = len(matrix)-1 , 0
        #while row >= 0 and col <= len(matrix[0])-1:
        #    if matrix[row][col] == target:
        #        return True
        #    elif matrix[row][col] < target:
        #        col += 1
        #    else: # matrix[row][col] > target
        #        row -= 1
        #return False
        
        # approch 3: mix of approach 1 and 2
        def binary_search(nums: List[int], target: int) -> bool:
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid -1
                else:
                    return True
            return False
        
        row, col = 0, len(matrix[0])-1
        while row <= len(matrix)-1 and col >= 0:
            cur = matrix[row][col]
            if cur > target:
                #col -= 1
                # instead of search one by one, do binary search to the whole row
                return binary_search(matrix[row], target)
            elif cur <target:
                row += 1
            else:
                return True
        return False