class Solution:
    
    lookup = {1:'0'}
    lookup_inv = {1:'1'}
    def invert(self, s: str) -> str:
        return ''.join(['0' if ch == '1' else '1' for ch in s])
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
            #binary = self.binary_str(n-1)
            #binary_inv = self.invert(binary)
            self.lookup[n] = self.binary_str(n-1) + '1' + self.binary_invstr(n-1)#binary + '1' + binary_inv[::-1]
            #self.lookup_inv[n] = binary + '0' + binary_inv[::-1]
            return self.lookup[n]
    def findKthBit(self, n: int, k: int) -> str:
        s = self.binary_str(n)
        #print(self.lookup)
        #print(self.lookup_inv)
        return s[k-1]
