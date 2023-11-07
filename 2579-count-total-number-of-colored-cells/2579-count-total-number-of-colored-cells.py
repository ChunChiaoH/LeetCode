class Solution:
    def coloredCells(self, n: int) -> int:
        # 1, 5, 13, 25, 41
        #   4  8  12  16
        return 1 + sum([4*(i+1) for i in range(n-1)])