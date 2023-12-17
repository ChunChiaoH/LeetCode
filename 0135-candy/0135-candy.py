class Solution:
    def candy(self, ratings: List[int]) -> int:
        # sliding window
        
        
        candy = [1 for _ in ratings]
        idx = [i for i in range(len(ratings))]
        
        # going ->
        # compare the right with the left
        for i, r in zip(idx[1:], ratings[1:]):
            if r > ratings[i-1] and candy[i] <= candy[i-1]:
                candy[i] = candy[i-1] + 1
        
        # goring <-
        # compare the left with the right
        for i, r in zip(idx[::-1][1:], ratings[::-1][1:]):
            if r > ratings[i+1] and candy[i] <= candy[i+1]:
                candy[i] = candy[i+1] + 1
                
        return sum(candy)