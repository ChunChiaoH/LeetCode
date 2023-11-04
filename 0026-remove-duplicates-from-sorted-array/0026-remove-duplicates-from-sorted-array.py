class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        slow, fast = 1, 1
        max_fast = len(nums)
        max_k = len(set(nums))
        while k < max_k:
            if nums[slow-1] == nums[fast]:
                fast += 1
            else: # nums[slow-1] != nums[fast]
                nums[slow] = nums[fast]
                slow +=1
                fast += 1
                k += 1
        return k
