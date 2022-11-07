class Solution:
    def twoSums(self, nums: List[int], target: int) -> Set[int]:
        # a modified version of "1. Two Sum"
        lefts = set()
        output = set()

        nums = nums[::-1] if target > 0 else nums
        for num in nums:
            if abs(num) > abs(target):
                # early stop if exceeds,
                # an example for negs: num=-4 and target=-2
                # an example for poses: num=5 and target=3
                break

            if num not in lefts:
                lefts.add(-target-num)
            else:
                output.add((num, -target-num, target))
        return output
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    # credit to rowe1227 @ LeetCode
        if len(nums) == 3:
            # early stop
            return [nums] if sum(nums) == 0 else []

        nums.sort()
        negs = [num for num in nums if num < 0]
        zs = [0 for num in nums if num == 0]
        poses = [num for num in nums if num > 0]
        
        len_ns, len_zs, len_ps = len(negs), len(zs), len(poses)
        output = {(0, 0, 0)} if len_zs >= 3 else set()
        set_negs, set_poses = set(negs), set(poses)
        
        # one neg and one pos cases
        if len_zs >= 1:
            for num in set_negs:
                if -num in set_poses:
                    output.add((num, 0, -num))

        # two negs + one pos cases
        if len_ns >= 2 and len_ps >= 1:
            for target in set_poses:
                output = output.union(self.twoSums(negs, target))

        # one neg + two poses cases
        if len_ns >= 1 and len_ps >= 2:
            for target in set_negs:
                output = output.union(self.twoSums(poses, target))
        
        return list(output)