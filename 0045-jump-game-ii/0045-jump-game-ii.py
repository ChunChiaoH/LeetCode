class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        dp = [1001 for _ in nums]
        dp[-1] = 0
        dp[-2] = 1 if nums[-2] > 0 else 1000
        
        idxs = [i for i in range(len(nums))][::-1][2:]
        for idx in idxs:
            #search_range = range(1, nums[idx]+1)
            if nums[idx] > 0:
                #search_range_idx = range(1, min(nums[idx]+1, len(nums)-idx+1))
                #search_range = [dp[idx+i] for i in search_range_idx]
                search_range = []
                for i in range(1, nums[idx]+1):
                    if i + idx >= len(nums):
                        break
                    search_range += [i]
                #print(nums[idx])
                #print(nums[idx], idx, search_range)
                dp[idx] = 1 + min([dp[idx+i] for i in search_range])
            #print(dp)
        return dp[0]