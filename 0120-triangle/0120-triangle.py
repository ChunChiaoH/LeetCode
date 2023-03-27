class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for j in range(n-1-1, -1, -1):
            for i in range(j+1):
                triangle[j][i] += min(triangle[j+1][i], triangle[j+1][i+1])
        return triangle[0][0]