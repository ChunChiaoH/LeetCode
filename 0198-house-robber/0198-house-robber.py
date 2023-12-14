class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0 for _ in nums]
        dp[-1] = nums[-1]
        dp[-2] = nums[-2]
        
        idxs = [i for i in range(len(nums))][::-1][2:]
        
        for idx in idxs:
            dp[idx] = nums[idx] + max(dp[idx+2:])
        
        return max(dp[:2])
        