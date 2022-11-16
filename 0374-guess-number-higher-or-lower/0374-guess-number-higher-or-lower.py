# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n-1
        mid = (left + right) // 2
        while left < right:
            print(left, mid, right)
            if guess(mid+1) == 0:
                return mid+1
            elif guess(mid+1) == 1:
                left = mid + 1
            else:
                right = mid - 1
            mid = (left + right) // 2
        return mid+1