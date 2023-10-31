class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bin = bin(n)[:1:-1]
        out = sum([2**(31-i)*int(c) for i, c in enumerate(reversed_bin)])
        return out