class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        res = set()
    
        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)
    
        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)
    
        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))
    
        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))
    
        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))
    
        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))
    
        return res
#    def twoSums(self, nums: List[int], target: int) -> Set[int]:
#        # a modified version of "1. Two Sum"
#        lefts = set()
#        output = set()
#
#        nums = nums[::-1] if target > 0 else nums
#        for num in nums:
#            if abs(num) > abs(target):
#                # early stop if exceeds,
#                # an example for negs: num=-4 and target=-2
#                # an example for poses: num=5 and target=3
#                break
#
#            if num not in lefts:
#                lefts.add(-target-num)
#            else:
#                output.add((num, -target-num, target))
#        return output
#    
#    def threeSum(self, nums: List[int]) -> List[List[int]]:
#    # credit to rowe1227 @ LeetCode
#        if len(nums) == 3:
#            # early stop
#            return [nums] if sum(nums) == 0 else []
#
#        nums.sort()
#        negs = [num for num in nums if num < 0]
#        zs = [0 for num in nums if num == 0]
#        poses = [num for num in nums if num > 0]
#        
#        len_ns, len_zs, len_ps = len(negs), len(zs), len(poses)
#        output = {(0, 0, 0)} if len_zs >= 3 else set()
#        set_negs, set_poses = set(negs), set(poses)
#        
#        # one neg and one pos cases
#        if len_zs >= 1:
#            for num in poses:
#                if num + negs[0] > 0:
#                    break
#                if -num in set_negs:
#                    output.add((num, 0, -num))
#
#        # two negs + one pos cases
#        if len_ns >= 2 and len_ps >= 1:
#            for target in set_poses:
#                if target + negs[-1] < 0:
#                    continue
#                output = output.union(self.twoSums(negs, target))
#
#        # one neg + two poses cases
#        if len_ns >= 1 and len_ps >= 2:
#            for target in set_negs:
#                if target + poses[0] > 0:
#                    continue
#                output = output.union(self.twoSums(poses, target))
#        
#        return list(output)