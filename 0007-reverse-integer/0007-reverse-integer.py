UPPER = [i for i in str(pow(2, 31)-1)]
LOWER = UPPER[:-1] + ['8']
BOUNDARY = [i for i in str(pow(2, 31)-1)]
class Solution:
    BOUNDARY = [i for i in str(pow(2, 31)-1)]
    def reverse(self, x: int) -> int:
        greater, smaller = 0, 0
        equal = True
        str_x = str(abs(x))
        len_x = len(str_x)
        if len_x < len(UPPER):
            num = int(''.join([i for i in str_x])[-1::-1])
            num = -num if x<0 else num
            return num
        else:
            s = ''
            if x<0:
                self.BOUNDARY = self.BOUNDARY[:-1] + ['8']
            for i, n in enumerate(str_x[-1::-1]):
                
                s += n
                if n == BOUNDARY[i]:
                    equal = True
                elif n>BOUNDARY[i]:
                    if equal and not smaller:
                        return 0
                elif n<BOUNDARY[i]:
                    smaller = True
                    equal = False
                #else:
                #    s += n
                #    if n == LOWER[i]:
                #        equal = True
                #    elif n>LOWER[i]:
                #        if equal and not smaller:
                #            return 0
                #    elif n<LOWER[i]:
                #        smaller = True
                #        equal = False
            return int(s) if x>=0 else -int(s)