class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0:
            if len(nums) == 1:
                return True
            return False
        
        prev0 = 0
        for i, num in enumerate(nums):
            if num == 0:
                temp = nums[:i]
                for j, t in enumerate(temp):
                    if t+j > i or (t+j == i and i == len(nums)-1):
                        print(i, j)
                        break
                    if j == len(temp)-1:
                        print(i, j)
                        return False
        return True