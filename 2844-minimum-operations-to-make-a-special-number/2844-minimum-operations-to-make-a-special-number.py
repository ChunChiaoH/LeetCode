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

        #find0s = [i for i, n in enumerate(num[::-1]) if n=='0']
        #find2s = [i for i, n in enumerate(num[::-1]) if n=='2']
        #find5s = [i for i, n in enumerate(num[::-1]) if n=='5']
        #find7s = [i for i, n in enumerate(num[::-1]) if n=='7']
        
        # find specials under 100
        #specials = [str(n) for n in range(101) if n%25 == 0]
        #all_digits = specials.join("")
        #specials = ['00', '25', '50', '75']
        #min_operations = {s: len(num) for num in specials}
        #all_digits = set("".join([k for k in min_operations.keys()]))
        ##find_digits
        #
        ##find00
        #min00 = len(num)
        #for i in find0s:
        #    for j in find0s:
        #        if i > j:
        #            min00 = min(min00, i-j-1+j)
        ##find25
        #min25 = len(num)
        #for i in find2s:
        #    for j in find5s:
        #        if i > j:
        #            min25 = min(min25, i-j-1+j)
        ##find50
        #min50 = len(num)
        #for i in find5s:
        #    for j in find0s:
        #        if i > j:
        #            min50 = min(min50, i-j-1+j)
        ##print(min50)
        ##find75
        #min75 = len(num)
        #for i in find7s:
        #    for j in find5s:
        #        if i > j:
        #            min75 = min(min75, i-j-1+j)
#
        #least_o = min(min00, min25, min50, min75)
        #if least_o == len(num):
        #    return least_o-1 if len(find0s) == 1 else least_o
        #else:
        #    return least_o
        
        
        #specials = [str(n) for n in range(100) if n%25 == 0]
        specials = ['00', '25', '50', '75']
        min_operations = {s: len(num) for s in specials}
        #min_operations
        all_digits = {d: [i for i, n in enumerate(num[::-1]) if n== d] 
              for d in set("".join([k for k in min_operations.keys()]))}
        #all_digits
        for k, v in min_operations.items():
            first_digit = all_digits[k[0]]
            second_digit = all_digits[k[1]]
            for i in first_digit:
                for j in second_digit:
                    min_operations[k] = min(min_operations[k], i-j-1+j) if i>j else min_operations[k]
        least_o = min(min_operations.values())
        if least_o == len(num):
            return least_o-1 if len(all_digits['0']) == 1 else least_o
        else:
            return least_o
        