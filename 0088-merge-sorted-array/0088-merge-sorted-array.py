class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        
        for i, n1 in enumerate(nums1):
            # iterate through nums1 to find inserting point
            tmp = []
            while nums2:
                # insert as much as possible at one time
                if nums2[0] <= n1:
                    tmp.append(nums2[0])
                    nums2 = nums2[1:]
                else:
                    break
            
            if tmp:
                # insert
                nums1[:] = nums1[:i] + tmp + nums1[i:-len(tmp)]
                
        if nums2:
            # if any of nums2 left
            nums1[:] = nums1[:-len(nums2)] + nums2
        