class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0 for _ in nums]
        # rob the first
        dp[-1] = 0
        dp[-2] = nums[-2]
        
        idxs = [i for i in range(len(nums))][::-1][2:]
        
        cur_max = max(dp[idxs[0]+2:])
        for idx in idxs:
            cur_max = max(cur_max, dp[idx+2])
            dp[idx] = nums[idx] + cur_max
        first = max(dp[:2])
        
        # don't rob the first
        dp = [0 for _ in nums]
        dp[-1] = nums[-1]
        dp[-2] = nums[-2]
        
        idxs = [i for i in range(len(nums))][::-1][2:]
        
        cur_max = max(dp[idxs[0]+2:])
        for idx in idxs:
            cur_max = max(cur_max, dp[idx+2])
            dp[idx] = nums[idx] + cur_max
        no_first = max(dp[1:3])
        
        return max(first, no_first)
        