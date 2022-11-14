class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        r = {}
        for ch in s:
            r[ch] = r.get(ch, 0) + 1
        for ch in t:
            if ch in r and r[ch]>0:
                r[ch] -= 1
            else:
                return ch