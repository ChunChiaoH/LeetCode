class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #   1  2  3  4  5
        #   1  1  2  6 24
        # 120 60 20  5  1
        # 120 60 40 30 24
        
        l = len(nums)
        p = 1
        res = [1 for _ in nums]
        for i, n in enumerate(nums):
            res[i] = p
            p *= n
        
        p = 1
        for i, n in enumerate(nums[::-1]):
            res[l-1-i] *= p
            p *= n
        return res