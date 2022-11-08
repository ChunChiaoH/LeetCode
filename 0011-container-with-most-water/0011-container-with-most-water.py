class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_volume = 0
        while i < j:
            if height[i] < height[j]:
                max_volume = max(max_volume, height[i]*(j-i))
                i += 1
            else:
                max_volume = max(max_volume, height[j]*(j-i))
                j -= 1
        return max_volume