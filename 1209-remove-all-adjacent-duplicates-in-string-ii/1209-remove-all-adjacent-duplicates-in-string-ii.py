class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = ''
        for ch in s:
            if len(stack) >= (k-1) and stack[-1:-k:-1] == ch*(k-1):
                stack = stack[:-k+1]
            else:
                stack += ch
        return stack