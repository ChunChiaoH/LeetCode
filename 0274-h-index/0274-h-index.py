class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        freq = [[citations[0], n]]
        # freq is an ordered frequency table
        
        for i, c in enumerate(citations[1:], 1):
            if c != citations[i-1]:
                freq += [[c, n-i]]
        
        max_h = 0
        for k, v in freq:
            # h-index is very much like picking the minimum square
            # so it has to be taken care from to edges of a squre(k and v)
            
            if v >= k:
                # h-index criteria, the usual edge
                max_h = k if k>max_h else max_h
            if k >= v:
                # "rotated" h-index criteria, the other edge
                max_h = v if v>max_h else max_h
        
        return max_h