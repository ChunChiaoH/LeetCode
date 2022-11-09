class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i, count = 0, 0
        while i < len(s)-2:
            if len(set(s[i:i+3])) == 3:
                count += 1
            i += 1
        return count