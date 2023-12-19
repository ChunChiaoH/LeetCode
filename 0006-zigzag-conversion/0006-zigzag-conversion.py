class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ["" for _ in range(numRows)]
        counter_idx = [n for n in range(numRows)]
        counter_idx += counter_idx[::-1][1:-1]
        counter_len = len(counter_idx)
        
        for i, c in enumerate(s):
            res[counter_idx[i%counter_len]] += c
            
        return ''.join(res)
            
            