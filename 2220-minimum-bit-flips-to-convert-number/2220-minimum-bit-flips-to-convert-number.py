class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # 1 0 > 1
        # 0 1 > 1
        # 0 0 > 0
        # 1 1 > 0
        # XOR
        longer = max(len(bin(start)), len(bin(goal))) - 2
        count = 0
        for _ in range(longer):
            count = count+1 if (start&1) ^ (goal&1) else count
            start >>= 1
            goal >>= 1
        return count