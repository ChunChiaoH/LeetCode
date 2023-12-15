class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        
        for i, n1 in enumerate(nums1):
            tmp = []
            while nums2:
                if nums2[0] <= n1:
                    tmp.append(nums2[0])
                    nums2 = nums2[1:]
                else:
                    break
            #print(nums1, tmp, nums2, '*')
            if tmp:
                nums1[:] = nums1[:i] + tmp + nums1[i:-len(tmp)]
        if nums2:
            nums1[:] = nums1[:-len(nums2)] + nums2 
            #print(nums1, tmp, nums2)
        