class Solution:
    def minimumOperations(self, num: str) -> int:
        if len(num) == 1:
            return 1 if num != '0' else 0

        #min_operations = {s: len(num) for s in ['00', '25', '50', '75']}
        ## min_operations: {'00': len(num), '25': len(num), ...}
        #
        #all_digits = {d: [i for i, n in enumerate(num[::-1]) if n== d] 
        #      for d in set("".join([k for k in min_operations.keys()]))}
        ## all_digits: {'0': [indices of 0s in num], '2': indices of 2s in num, ...}
        #
        #for k in min_operations:
        #    first_digit = all_digits[k[0]]
        #    second_digit = all_digits[k[1]]
        #    if (not first_digit) or (not second_digit):
        #        continue
        #    for d in first_digit:
        #        if d > min(second_digit):
        #            min_operations[k] = min(min_operations[k], d-1)
        #            break
        #            
        #least_o = min(min_operations.values())
        #if least_o == len(num):
        #    return least_o-1 if len(all_digits['0']) == 1 else least_o
        #else:
        #    return least_o
        i = 0
        has_0 = False
        has_5 = False
        rev_num = num[::-1]
        count = len(rev_num)
        while i< len(rev_num):
            if rev_num[i] == '0' and not has_0:
                has_0 = True
                i += 1
                continue
                
            if (rev_num[i] == '5' or rev_num[i] == '0') and has_0:
                count = min(count, i-1)
            i += 1
            
        j = 0
        while j< len(rev_num):
            if rev_num[j] == '5' and not has_5:
                j += 1
                has_5 = True
                continue
                
            if (rev_num[j] == '7' or rev_num[j] == '2') and has_5:
                count = min(count, j-1)
            j += 1
        
        if count == len(rev_num) and has_0:
            return count -1
        else:
            return count
        