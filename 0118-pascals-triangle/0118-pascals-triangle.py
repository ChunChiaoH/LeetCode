class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []
        
        for n in range(numRows):
            half = []
            for j in range((n//2)+1):
                if j == 0:
                    half.append(1)
                else:
                    half.append(tri[n-1][j] + tri[n-1][j-1])
                    
            if n%2 == 0:
                row = half + half[::-1][1:]
            else: #n%2 == 1
                row = half + half[::-1]
            tri.append(row)
            
        return tri