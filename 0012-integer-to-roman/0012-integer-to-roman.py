nums = [{1: 'I', 4: 'IV', 5: 'V', 9: 'IX'},
        {1: 'X', 4: 'XL', 5: 'L', 9: 'XC'},
        {1: 'C', 4: 'CD', 5: 'D', 9: 'CM'}, {1:'M'}]

class Solution:
    def intToRoman(self, num: int) -> str:
        decomposed_num = [int(i) for i in str(num)][-1::-1]
        s = ''
        i = 0
        for n in decomposed_num:
            if n in [4, 5, 9]:
                s = nums[i][n] + s
            elif 0 <= n < 4:
                s = ''.join([nums[i][1] for _ in range(n)]) + s
            else:# 5 < n < 9:
                s = nums[i][5] + ''.join([nums[i][1] for _ in range(n-5)]) + s
                
            i += 1
        return s