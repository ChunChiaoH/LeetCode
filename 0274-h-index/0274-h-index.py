class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        freq = [[citations[0], n]]
        
        for i, c in enumerate(citations[1:], 1):
            if c == citations[i-1]:
                freq.append(freq[-1])
            else:
                freq.append([c, n-i])
        
        max_h = 0
        for k, v in freq:
            # h-index is very much like pick the minimum square
            # so it has to be taken care from to edges of a squre(k and v)
            
            # h-index criteria
            if v >= k:
                if k > max_h:
                    max_h = k
                    
        for v, k in freq:
            if v >= k:
                if k > max_h:
                    max_h = k
        
        return max_h