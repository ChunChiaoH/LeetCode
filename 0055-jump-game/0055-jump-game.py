class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_idx = len(nums) -1
        dp = [True if i+num >= last_idx else False for i, num in enumerate(nums)]
        if dp[0]:
            return True
        
        for dis, num in enumerate(nums[::-1]):
            step = last_idx - dis
            if dp[step] or num == 0:
                continue
            for n in range(num, 0, -1):
                if dp[n+step] == True:
                    dp[step] = True
                    break
                    
        return dp[0]