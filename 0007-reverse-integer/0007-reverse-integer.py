
class Solution:
    
    def reverse(self, x: int) -> int:
        if x>0:
            BOUNDARY = [i for i in str(pow(2, 31)-1)]
        else:
            BOUNDARY = [i for i in str(pow(2, 31))]

        equal, smaller = True, False
        str_x = str(abs(x))
        len_x = len(str_x)
        if len_x < len(BOUNDARY):
            s = ''.join([i for i in str_x])[-1::-1]
        else:
            s = ''
                
            for i, n in enumerate(str_x[-1::-1]):
                s += n
                if n == BOUNDARY[i]:
                    equal = True
                    
                elif n>BOUNDARY[i]:
                    if equal:
                        return 0
                    else:
                        if not smaller:
                            return 0
                        
                elif n<BOUNDARY[i]:
                    smaller = True
                    equal = False
                    
        return int(s) if x>=0 else -int(s)