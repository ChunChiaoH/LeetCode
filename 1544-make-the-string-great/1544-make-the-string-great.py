class Solution:
    def makeGood(self, s: str) -> str:
        stack = ''
        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack = stack[:-1]
            else:
                stack += ch
        return stack