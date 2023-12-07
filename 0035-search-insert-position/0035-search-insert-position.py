class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l+r)//2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        if target > nums[mid]:
            return mid+1
        else:
            return mid
        # 0 1 2 3
        #   *
        # 1 3 5 6, target = 2
        # *
        # 1 3 5 6