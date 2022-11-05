UPPER = [i for i in str(pow(2, 31)-1)]
LOWER = UPPER[:-1] + ['8']
#BOUNDARY = [i for i in str(pow(2, 31))]
class Solution:
    
    def reverse(self, x: int) -> int:
        greater, smaller = 0, 0
        equal = True
        #print(LOWER, UPPER)
        str_x = str(abs(x))
        len_x = len(str_x)
        if len_x < len(UPPER):
            num = int(''.join([i for i in str_x])[-1::-1])
            num = -num if x<0 else num
            return num
        else:
            s = ''
            for i, n in enumerate(str_x[-1::-1]):
                #if greater == 0:
                #    if n>UPPER[i]:
                #        greater = True
                #if smaller == 0:
                #    if n<UPPER[i]:
                #        smaller = True
                if x>=0:
                    s += n
                    if n == UPPER[i]:
                        equal = True
                    elif n>UPPER[i]:
                        if equal and not smaller:
                            #continue
                            return 0
                        else:
                            continue
                    elif n<UPPER[i]:
                        smaller = True
                        equal = False
                else:
                    s += n
                    if n == LOWER[i]:
                        equal = True
                    elif n>LOWER[i]:
                        if equal and not smaller:
                            return 0
                            #continue
                        else:
                            continue
                            #return 0
                    elif n<LOWER[i]:
                        smaller = True
                        equal = False
            return int(s) if x>=0 else -int(s)
        
        #print(lower, upper)
        #if x >= 0:
        #    num = int(''.join([i for i in str(x)])[-1::-1])
        #else:
        #    num = -int(''.join([i for i in str(x)[1:]])[-1::-1])
        #return num if lower<num<upper else 0