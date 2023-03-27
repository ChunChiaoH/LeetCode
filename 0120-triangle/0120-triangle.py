class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for j in range(n-1-1, -1, -1):
            #row = triangle[j]
            for i in range(j+1):#row:
                triangle[j][i] += min(triangle[j+1][i], triangle[j+1][i+1])
            #print(triangle)
        
        return triangle[0][0]