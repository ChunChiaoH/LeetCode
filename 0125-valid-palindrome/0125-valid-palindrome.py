class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = 'a'+s+'a'
        n = len(s)
        i, j = 0, n-1
        res = True
        
        def isAlphanumeric(c: str) -> bool:
            if ord('A') <= ord(c) <= ord('Z'):
                return True
            if ord('a') <= ord(c) <= ord('z'):
                return True
            if ord('0') <= ord(c) <= ord('9'):
                return True
            
            return False
        
        while i < j:
            while not s[i].isalnum():#isAlphanumeric(s[i]):
                i += 1
            while not s[j].isalnum():#isAlphanumeric(s[j]):
                j -= 1
            
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        
        if i == j and s[i] != s[j]:
            return False
        return True