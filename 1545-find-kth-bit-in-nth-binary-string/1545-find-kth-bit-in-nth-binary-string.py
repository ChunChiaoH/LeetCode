class Solution:
    lookup = {1:'0'}
    lookup_inv = {1:'1'}
    def binary_invstr(self, n: int) -> str:
        if n in self.lookup_inv:
            return self.lookup_inv[n]
        else:
            self.lookup_inv[n] = self.binary_str(n-1) + '0' + self.binary_invstr(n-1)
            return self.lookup_inv[n]
        
    def binary_str(self, n: int) -> str:
        if n in self.lookup:
            return self.lookup[n]
        else:
            self.lookup[n] = self.binary_str(n-1) + '1' + self.binary_invstr(n-1)
            return self.lookup[n]
        
    def findKthBit(self, n: int, k: int) -> str:
        return self.binary_str(n)[k-1]
