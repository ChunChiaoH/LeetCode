class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        temp = [n for n in nums[-k:]] + [n for n in nums[:-k]]
        
        for i, n in enumerate(temp):
            nums[i] = n