class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = 'a'+s+'a'
        n = len(s)
        i, j = 0, n-1
        
        while i < j:
            while not s[i].isalnum():
                i += 1
            while not s[j].isalnum():
                j -= 1
            
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        
        #if i == j and s[i] != s[j]:
        #    return False
        return True