class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for _ in nums]
        last_idx = len(nums) -1
        for i, num in enumerate(nums[::-1]):
            if num >= i:
                dp[i] = True
            else:
                # current index - [1, num]
                dp[i] = any([dp[i-j] for j in range(1, num+1)])
        return dp[-1]
        
        #if nums[0] == 0:
        #    if len(nums) == 1:
        #        return True
        #    return False
        
        #for i, num in enumerate(nums):
        #    #print(num + i >= len(nums))
        #    #print(num, i, len(nums))
        #    if num + i >= len(nums)-1:
        #        #print(num + i >= len(nums)-1)
        #        #print(num + i, len(nums)-1)
        #        return True
        #    if num == 0:
        #        temp = nums[:i]
        #        for j, t in enumerate(temp):
        #            if t+j > i:
        #                break
        #            if j == len(temp)-1:
        #                return False
        #return False