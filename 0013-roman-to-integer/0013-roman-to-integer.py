I, X, C, M = 'I', 'X', 'C', 'M'
V, L, D = 'V', 'L', 'D'
nums = {I: 1, V: 5, X:10, L:50, C:100, D:500, M: 1000}
class Solution:

    def romanToInt(self, s: str) -> int:
        count = 0
        i = 0
        while i < len(s):
            cur_num = s[i]
            next_num = s[i+1] if i<len(s)-1 else None

            if cur_num in [I, X, C] and next_num:
                if (cur_num == I and next_num in [V, X]) or\
                   (cur_num == X and next_num in [L, C]) or\
                   (cur_num == C and next_num in [D, M]):
                    count += nums[next_num] - nums[cur_num]
                    i += 2
                    continue
            count += nums[cur_num]
            i += 1

        return count

