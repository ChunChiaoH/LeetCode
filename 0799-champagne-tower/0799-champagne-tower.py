class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0
        if query_row == 0:
            return min(poured, 1)
        
        prev_row = [poured - 1]
        cur_row = []
        for i in range(1, query_row+1):
            num_glasses = i+1
            cur_row = [0 for _ in range(num_glasses)]
            for j in range(num_glasses):
                if j == 0: # left-most glass
                    cur_row[j] = prev_row[j]/2
                elif j == num_glasses-1: # right-most glass
                    cur_row[j] = prev_row[j-1]/2
                else:
                    cur_row[j] = prev_row[j-1]/2 + prev_row[j]/2
                    
                if i!= query_row:
                    # transfer to throughput if it's not the queried row
                    cur_row[j] = max(cur_row[j]-1, 0)
                # else, cur_row[j] stores how much has been pored into it
                # this is only for the queried row,
                # such that when amount been poured into cur_row[j] is less than 1 can be kept
           
            prev_row = cur_row
            
        return min(cur_row[query_glass], 1)