class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        left, right = 0, len(nums)-1
        mid = (left + right) // 2
        keep = mid
        while left < right:
            if nums[mid] == target:
                print('D')
                break
            elif nums[mid] < target:
                left = mid
                mid = (left + right) // 2
                print('A')
                if keep == mid:
                    mid += 1
                    break
            elif target < nums[mid]:
                right = mid
                mid = (left + right) // 2
                print('B')
                if keep == mid:
                    mid -= 1
                    break
            keep = mid
            print(mid)
        print(mid)
        return -1 if nums[mid] != target else mid