class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(tri[i-1][j] + tri[i-1][j-1])
            tri.append(row)
            
        return tri