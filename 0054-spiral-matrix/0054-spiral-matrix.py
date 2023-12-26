class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # > V < ^
        # >  0,  1
        # V  1,  0
        # <  0, -1
        # ^ -1,  0
        m, n = len(matrix), len(matrix[0])
        
        def out_of_boundary(y: int, x: int) -> bool:
            return (y < 0 or y >= m) or (x < 0 or x >= n)
        
        visited = set()
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        di = 0
        i, j = 0, 0
        visited.add((0, 0))
        res = [matrix[i][j]]
        
        while len(res) < m*n:
            delta = dir[di]
            if out_of_boundary(i+delta[0], j+delta[1]) or (i+delta[0], j+delta[1]) in visited:
                di = (di+1)%4
                continue
            else:
                i += delta[0]
                j += delta[1]
                visited.add((i, j))
                res.append(matrix[i][j])
        return res
                