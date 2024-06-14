class Solution:
    def minimumOperations(self, num: str) -> int:
        if len(num) == 1:
            return 1 if num != '0' else 0
        #rev_num = num[::-1]
        
        # too slow
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
        
        #num = "105"
        find0s = [i for i, n in enumerate(num[::-1]) if n=='0']
        find2s = [i for i, n in enumerate(num[::-1]) if n=='2']
        find5s = [i for i, n in enumerate(num[::-1]) if n=='5']
        find7s = [i for i, n in enumerate(num[::-1]) if n=='7']
        #print(find0s)
        #print(find2s)
        #print(find5s)
        #print(find7s)
        #find00
        min00 = len(num)
        for i in find0s:
            for j in find0s:
                if i > j:
                    min00 = min(min00, i-j-1+j)
        #print(min00)
        #find25
        min25 = len(num)
        for i in find2s:
            for j in find5s:
                if i > j:
                    min25 = min(min25, i-j-1+j)
        #print(min25)
        #find50
        min50 = len(num)
        for i in find5s:
            for j in find0s:
                if i > j:
                    min50 = min(min50, i-j-1+j)
        #print(min50)
        #find75
        min75 = len(num)
        for i in find7s:
            for j in find5s:
                if i > j:
                    min75 = min(min75, i-j-1+j)
        #print(min75)
        least_o = min(min00, min25, min50, min75)
        if least_o == len(num):
            if len(find0s) == 1:
                #print(least_o-1)
                return least_o-1
            else:
                return least_o
        else:
            return least_o