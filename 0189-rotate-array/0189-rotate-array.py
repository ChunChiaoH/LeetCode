class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #print('***', len(nums))
        temp = list(nums)
        for _ in range(k):
            cur_num = temp.pop()
            temp = [cur_num]+temp
            #print(nums)
        #print('***', len(nums))
        for i, n in enumerate(temp):
            #print(i)
            nums[i] = n