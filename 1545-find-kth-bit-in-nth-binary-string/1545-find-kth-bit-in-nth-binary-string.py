class Solution:
    
    lookup = {1:'0'}
    lookup_inv = {1:'1'}
    def invert(self, s: str) -> str:
        return ''.join(['0' if ch == '1' else '1' for ch in s])
    def binary_str(self, n) -> str:
        if n in self.lookup:
            return self.lookup[n]
        else:
            binary = self.binary_str(n-1)
            binary_inv = self.invert(binary)
            self.lookup[n] = binary + '1' + binary_inv[::-1]
            self.lookup_inv[n] = binary_inv[::-1] +'0' + binary[::-1]
            return self.binary_str(n)
    def findKthBit(self, n: int, k: int) -> str:
        s = self.binary_str(n)
        return s[k-1]
