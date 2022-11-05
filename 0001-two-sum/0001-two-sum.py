class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lefts = {}
        for i, num in enumerate(nums):
            #if num not in lefts:
            #    lefts[target-num] = i
            #else:
            if num in lefts:
                return [i, lefts[num]]
            lefts[target-num] = i
        