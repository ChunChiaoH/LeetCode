class Solution:
    def reverseBits(self, n: int) -> int:
        res = n&1
        n >>= 1
        for i in range(31):
            res <<= 1
            res = res + (n&1)
            n >>= 1
        return res