class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [[s[0], 1]]
        for ch in s[1:]:
            if stack and stack[-1][0] == ch:
                if stack[-1][1] == k-1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([ch, 1])
        return ''.join([ch*count for ch, count in stack])
        #stack = ''
        #l = 0
        #for ch in s:
        #    if l >= (k-1) and stack[-1:-k:-1] == ch*(k-1):
        #        stack = stack[:-k+1]
        #        l -= (k-1)
        #    else:
        #        stack += ch
        #        l += 1
        #return stack