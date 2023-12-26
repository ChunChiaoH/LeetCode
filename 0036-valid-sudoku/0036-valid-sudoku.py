class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        record_flags = {str(i+1): [set(), set(), set()] for i in range(9)}
        
        for i, row in enumerate(board):
            for j, e in enumerate(row):
                # 0: 1 2 3 
                # 1: 4 5 6
                # 2: 7 8 9
                grid_num = (i//3)*3 + (j//3) + 1
                if e in record_flags:
                    if i in record_flags[e][0]:
                        return False
                    if j in record_flags[e][1]:
                        return False
                    if grid_num in record_flags[e][2]:
                        return False
                    record_flags[e][0].add(i)
                    record_flags[e][1].add(j)
                    record_flags[e][2].add(grid_num)
        return True