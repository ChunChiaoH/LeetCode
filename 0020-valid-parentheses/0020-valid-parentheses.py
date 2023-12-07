class Solution:
    def isValid(self, s: str) -> bool:
        lens = len(s)
        if lens%2 != 0:
            return False
        
        counter_part = {'(': ')', '[':']', '{':'}'}
        stack = []
        for i, c in enumerate(s):
            if len(stack) > 0 and counter_part.get(stack[-1], '') == c:
                stack.pop()
            else:
                stack.append(c)
                
        return len(stack) == 0