class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, i = 1, 0
        max_len = 1
        while i+l < len(s)+1:
            if len(set(s[i:i+l])) == l:
                max_len = max(max_len, l)
                l += 1
            else:
                i += 1
        return max_len