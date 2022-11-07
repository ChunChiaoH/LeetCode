class Solution:
    def twoSums(self, nums: List[int], target: int) -> Set[int]:
        lefts = set()
        output = set()
        target = -target
        for num in nums:
            if num not in lefts:
                lefts.add(target-num)
            else:
                output.add((num, target-num, -target))
        return output
            
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []
        len_nums = len(nums)
        negs, zs, poses = [], [], []
        for num in nums:
            if num < 0:
                negs.append(num)
            elif num == 0:
                zs.append(0)
            else:
                poses.append(num)
        #negs = [num for num in nums if num < 0]
        #zs = [num for num in nums if num == 0]
        #poses = [num for num in nums if num > 0]
        len_zs = len(zs)
        output = {(0, 0, 0)} if len_zs >= 3 else set()
        
        # one neg and one pos cases
        if len_zs >= 1:
            for num in negs:
                if -num in poses:
                    output.add((num, 0, -num))
        # two negs + one pos cases
        # one neg + two poses cases
        for target in set(poses):
            output = output.union(self.twoSums(negs, target))
        for target in set(negs):
            output = output.union(self.twoSums(poses, target))
        
        return output