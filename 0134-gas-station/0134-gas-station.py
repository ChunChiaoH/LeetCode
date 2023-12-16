class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #  1  2  4  3  5
        #  3  4  1  5  2
        # -2 -2  3 -2  3
        
        #  5  1  2  3  4
        #  4  4  1  5  1
        #  1 -3  1 -2  3
        
        # the following two approaches are the same
        # except for how they handle the "loop" gas stations.
        
        # approach 1: 
        left = [g-c for g, c in zip(gas, cost)]
        if sum(left) < 0:
            # if the sum of "left" is less than 0, there will be no solution
            # this handles the situation where the solution is at later part of the "left" array
            # with this, the loop problem does not need to be taken care of when iterating through the "left" array
            return -1
        
        j = 0
        cum_sum = 0
        for i, l in enumerate(left):
            # iterate through the "left" array and record an index j
            # whenever the cumulative sum is smaller than 0, the current j is invalid
            # then next possible j is the next index: i+1
            cum_sum += l
            if cum_sum < 0:
                cum_sum = 0
                j = i+1
                
        return j
    
        # approach 2: 
        #left = [g-c for g, c in zip(gas, cost)]
        #
        #j = 0
        #cum_sum = l_cum_sum = 0
        #for i, l in enumerate(left):
        #    # same as approach 1,
        #    # but the loop problem is taken care of in when iterating through the "left" array
        #    # whenever the cum_sum is smaller than 0, it will be added into the "l_cum_sum"
        #    cum_sum += l
        #    if cum_sum < 0:
        #        l_cum_sum += cum_sum
        #        cum_sum = 0
        #        j = i+1
        #
        ## check if the l_cum_sum can becancelled by the cum_sum 
        #return j if l_cum_sum + cum_sum >= 0 else -1
                