class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #  1  2  4  3  5
        #  3  4  1  5  2
        # -2 -2  3 -2  3
        
        #  5  1  2  3  4
        #  4  4  1  5  1
        #  1 -3  1 -2  3
        
        left = [g-c for g, c in zip(gas, cost)]
        #if sum(left) < 0:
        #    return -1
        
        j = 0
        cum_sum = 0
        l_cum_sum = 0
        for i, l in enumerate(left):
            cum_sum += l
            if cum_sum < 0:
                l_cum_sum += cum_sum
                cum_sum = 0
                j = i+1
        
        #return j
        #print(left)
        #print(l_cum_sum, cum_sum)
        if l_cum_sum + cum_sum >= 0:
            return j
        else:
            return -1
                