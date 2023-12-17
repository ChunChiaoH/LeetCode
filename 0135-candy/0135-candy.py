class Solution:
    def candy(self, ratings: List[int]) -> int:
        # sliding window
        # s  : 1 0 2
        # c1 : 2 1 2
        # c2 : 2 1 2
        
        # s  : 1 2 2
        # c1 : 1 2 1
        # c2 : 1 2 1
        
        # s  : 5 2 3 1 3 5
        # c1 : 1 1 2 1 2 3
        # c2 : 2 1 2 1 2 3
        
        candy = [1 for _ in ratings]
        idx = [i for i in range(len(ratings))]
        
        for i, r in zip(idx[1:], ratings[1:]):
            if r > ratings[i-1] and candy[i] <= candy[i-1]:
                candy[i] = candy[i-1] + 1
                
        for i, r in zip(idx[::-1][1:], ratings[::-1][1:]):
            if r > ratings[i+1] and candy[i] <= candy[i+1]:
                candy[i] = candy[i+1] + 1
                
        return sum(candy)