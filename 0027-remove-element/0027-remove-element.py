class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        i = 0
        n = len(nums)
        #for i, num in enumerate(nums):
        while i < n:
            if nums[i] == val:
                nums[:] = nums[:i] + nums[i+1:] + ['']
                c += 1
                continue
            i += 1
        return len(nums) - c