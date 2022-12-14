
class Solution:
    
    def reverse(self, x: int) -> int:
        if x>0:
            BOUNDARY = [i for i in str(pow(2, 31)-1)]
        else:
            BOUNDARY = [i for i in str(pow(2, 31))]

        smaller = False
        str_x = str(abs(x))
        
        if len(str_x) < len(BOUNDARY):
            s = str_x[-1::-1]
        else:
            s = ''
            for i, n in enumerate(str_x[-1::-1]):
                s += n
                if n>BOUNDARY[i] and not smaller:
                    return 0
                elif n<BOUNDARY[i]:
                    smaller = True
                    
        return int(s) if x>=0 else -int(s)