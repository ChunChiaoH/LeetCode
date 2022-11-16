class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        left, right = 0, len(nums)-1
        mid = (left + right) // 2
        keep = mid
        while left < right:
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                left = mid
            elif target < nums[mid]:
                right = mid
            mid = (left + right) // 2
            
            if keep == mid:
                mid += 1 
                break
            keep = mid
        return mid if nums[mid] == target else -1