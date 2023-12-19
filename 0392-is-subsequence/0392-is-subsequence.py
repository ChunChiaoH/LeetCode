class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        n, m = len(s), len(t)
        
        while i <= n-1 and j <= m-1:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        if i != n:
            return False
        return True