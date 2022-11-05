class Solution:
    def reverse(self, x: int) -> int:
        upper = pow(2, 31)-1
        lower = -pow(2, 31)
        if x>=0:
            num = int(''.join([i for i in str(x)])[-1::-1])
        else:
            num = -int(''.join([i for i in str(x)[1:]])[-1::-1])
        return num if lower<num<upper else 0