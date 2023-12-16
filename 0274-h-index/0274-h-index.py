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
            # h-index criteria
            if v >= k:
                if k > max_h:
                    max_h = k
        for v, k in freq:
            if k <= v:
                if k > max_h:
                    max_h = k
        
        return max_h