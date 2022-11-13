class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = ''
        for ch in s:
            if len(stack) >= (k-1):
                if stack[-1:-k:-1] == ch*(k-1):
                    stack = stack[:-k+1]
                else:
                    stack += ch
            else:
                stack += ch
        return stack
    #3*abc + 3bca