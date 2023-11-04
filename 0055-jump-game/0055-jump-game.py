class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0:
            if len(nums) == 1:
                return True
            return False
        
        for i, num in enumerate(nums[:-1]):
            if num + i >= len(nums):
                return True
            if num == 0:
                temp = nums[:i]
                for j, t in enumerate(temp):
                    if t+j > i:# or (t+j == i and i == len(nums)-1):
                        break
                    if j == len(temp)-1:
                        return False
        return True