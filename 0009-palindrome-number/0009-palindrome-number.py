class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        str_x = str(x)
        len_x = len(str_x)
        i = len_x//2 -1
        j = len_x//2 +1 if len_x%2 == 1 else len_x//2
        # even: 0 1 2 3
        # i start from 1 ==> 4//2 -1
        # j start from 2 ==> 4//2
        # odd: 0 1 2
        # i start from 0 ==> 3//2 -1
        # j start from 2 ==> 3//2 +1
        
        while j <= len_x-1:
            if str_x[i] != str_x[j]:
                return False
            i -= 1
            j += 1
        return True