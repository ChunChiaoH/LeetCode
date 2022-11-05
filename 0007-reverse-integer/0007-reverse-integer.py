
class Solution:
    BOUNDARY = [i for i in str(pow(2, 31)-1)]
    def reverse(self, x: int) -> int:
        greater, smaller = 0, 0
        equal = True
        str_x = str(abs(x))
        len_x = len(str_x)
        if len_x < len(self.BOUNDARY):
            s = ''.join([i for i in str_x])[-1::-1]
        else:
            s = ''
            if x<0:
                self.BOUNDARY = self.BOUNDARY[:-1] + ['8']
            for i, n in enumerate(str_x[-1::-1]):
                s += n
                if n == self.BOUNDARY[i]:
                    equal = True
                elif n>self.BOUNDARY[i]:
                    if equal and not smaller:
                        return 0
                elif n<self.BOUNDARY[i]:
                    smaller = True
                    equal = False
                    
        return int(s) if x>=0 else -int(s)