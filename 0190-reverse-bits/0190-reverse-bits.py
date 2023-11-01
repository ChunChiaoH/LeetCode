class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = res + (n&1)
            n >>= 1
            if i<31:
                res <<= 1
        return res