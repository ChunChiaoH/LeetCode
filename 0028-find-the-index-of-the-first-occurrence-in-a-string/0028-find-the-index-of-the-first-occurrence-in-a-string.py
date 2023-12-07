class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        needle_len, haystack_len = len(needle), len(haystack)
        #if haystack_len <= needle_len:
        #    return 0 if haystack == needle else -1
        
        for i, c in enumerate(haystack[:len(haystack)-needle_len+1]):
            if c != needle[0]:
                continue
            
            if haystack[i: i+needle_len] == needle:
                return i
        
        return -1