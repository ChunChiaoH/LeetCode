class Solution:
    def minimumOperations(self, num: str) -> int:
        if len(num) == 1:
            return 1 if num != '0' else 0

        rev_num = num[::-1]
        has_0 = has_5 = False
        min_ops = len(rev_num)
        
        for i, digit in enumerate(rev_num):
            if not has_0:
                if digit == '0':
                    has_0 = True
            else:
                if digit == '0' or digit == '5':
                    min_ops = min(min_ops, i-1)
                    
        for i, digit in enumerate(rev_num):
            if not has_5:
                if digit == '5':
                    has_5 = True
            else:
                if digit == '2' or digit == '7':
                    min_ops = min(min_ops, i-1)
        
        if min_ops == len(rev_num) and has_0:
            return min_ops -1
        else:
            return min_ops
        