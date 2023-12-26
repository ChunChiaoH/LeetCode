class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # >  V  <  ^
        # >  0,  1
        # V  1,  0
        # <  0, -1
        # ^ -1,  0
        
        m, n = len(matrix), len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dir_idx = 0
        i, j = 0, 0
        visited = set()
        
        visited.add((0, 0))
        res = [matrix[i][j]]
        
        def out_of_boundary(y: int, x: int) -> bool:
            return (not (0 <= y < m)) or (not (0 <= x < n))
        
        while len(res) < m*n:
            delta = directions[dir_idx]
            if out_of_boundary(i+delta[0], j+delta[1]) or (i+delta[0], j+delta[1]) in visited:
                dir_idx = (dir_idx+1)%4
                continue
            else:
                i += delta[0]
                j += delta[1]
                visited.add((i, j))
                res.append(matrix[i][j])
        return res
                