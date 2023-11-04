class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        slow, fast = 1, 1
        max_slow = len(set(nums)) -1
        max_fast = len(nums)
        while fast < max_fast:
            if nums[slow-1] == nums[fast]:
                fast += 1
            else: # nums[slow-1] != nums[fast]
                nums[slow] = nums[fast]
                slow +=1
                fast += 1
                k += 1
        #print(k)
        #print(nums)
        return k

#  0 1 2
# [1 2 2]

