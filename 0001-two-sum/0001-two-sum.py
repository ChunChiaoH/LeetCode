class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lefts = {}
        for i, num in enumerate(nums):
            if num in lefts:
                return [i, lefts[num]]
            else:
                lefts[target-num] = i
        