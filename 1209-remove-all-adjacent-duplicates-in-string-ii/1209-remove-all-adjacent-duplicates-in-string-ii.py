class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = ''
        l = 0
        for ch in s:
            if l >= (k-1) and stack[-1:-k:-1] == ch*(k-1):
                stack = stack[:-k+1]
                l -= (k-1)
            else:
                stack += ch
                l += 1
        return stack