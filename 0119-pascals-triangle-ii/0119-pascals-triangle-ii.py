class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        s = [1]
        for i in range(1, rowIndex+1):
            nums1, nums2 = [0]+s, s+[0]
            s = [n1 + n2 for n1, n2 in zip(nums1, nums2)]
        return s
            