class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 1
        f_idx = len(nums)-1
        while i < f_idx:
            if nums[i] == '_':
                break
            if nums[i-1] == nums[i] == nums[i+1]:
                k += 1
                nums[i:] = nums[i+1:] + ['_']
            else:
                i += 1
                
        return len(nums)-k
                