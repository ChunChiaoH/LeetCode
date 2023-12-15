class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        #           p9
        #            8
        #           3 3
        #         .5 2 .5
        #        0  1 1  0
        if poured == 0:
            return 0
        if query_row == 0:
            return min(poured, 1)
        
        prev_row = [poured - 1]
        cur_row = []
        queried = []
        for i in range(1, query_row+1):
            num_glasses = i+1
            cur_row = [0 for _ in range(num_glasses)]
            for j in range(num_glasses):
                if j == 0:
                    cur_row[j] = prev_row[j]/2
                elif j == num_glasses-1:
                    cur_row[j] = prev_row[j-1]/2
                else:
                    cur_row[j] = prev_row[j-1]/2 + prev_row[j]/2
                
                #if i == query_row:
                #    queried += [1] if cur_row[j] >= 1 else [cur_row[j]]
                if i!= query_row:
                    cur_row[j] = max(cur_row[j]-1, 0)
                #else:
                #    cur_row[j] = min(cur_row[i], 1)
           
            prev_row = cur_row
            
        
        return min(cur_row[query_glass], 1)