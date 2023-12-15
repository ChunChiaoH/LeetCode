class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        cum_shifts = [0 for _ in range(len(s)+1)]
        
        for st, end, d in shifts:
            cum_shifts[st] += -1 if d == 0 else 1
            cum_shifts[end+1] += 1 if d == 0 else -1
            
            #if d == 0:
            #    cum_shifts[st] -= 1
            #    cum_shifts[end+1] += 1
            #else:
            #    cum_shifts[st] += 1
            #    cum_shifts[end+1] -= 1
        
        a_code = ord('a')
        cum_sum = 0
        res = ''
        for i, c in enumerate(s):
            cum_sum += cum_shifts[i]
            new_code = (((ord(s[i]) + cum_sum) - a_code) % 26) + a_code
            res += chr(new_code)
        
        return res