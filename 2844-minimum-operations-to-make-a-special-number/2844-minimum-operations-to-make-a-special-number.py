class Solution:
    def minimumOperations(self, num: str) -> int:
        if len(num) == 1:
            return 1 if num != '0' else 0
        
        # too slow
        #rev_num = num[::-1]
        #def search(i, cur):
        #    if i == len(rev_num):
        #        return len(rev_num)-1 if cur == '0' else len(rev_num)
        #        
        #    if rev_num[i] != '0' and int(rev_num[i]+cur) % 25 == 0:
        #        return i - len(cur)
        #    else:
        #        return min(search(i+1, rev_num[i]+cur), search(i+1, cur))
        #    
        #return search(0, '')

        specials = ['00', '25', '50', '75']
        min_operations = {s: len(num) for s in specials}
        # min_operations: {'00': len(num), '25': len(num), ...}
        
        all_digits = {d: [i for i, n in enumerate(num[::-1]) if n== d] 
              for d in set("".join([k for k in min_operations.keys()]))}
        # all_digits: {'0': [indices of 0s in num], '2': indices of 2s in num, ...}
        
        for k in min_operations:
            first_digit = all_digits[k[0]]
            second_digit = all_digits[k[1]]
            for d in first_digit:
                if any(n < d for n in second_digit):
                    min_operations[k] = min(min_operations[k], d-1)                
            #for i in first_digit:
            #    for j in second_digit:
            #        if j>=i:
            #            continue
            #        min_operations[k] = min(min_operations[k], i-j-1+j)
                    
        least_o = min(min_operations.values())
        if least_o == len(num):
            return least_o-1 if len(all_digits['0']) == 1 else least_o
        else:
            return least_o
        