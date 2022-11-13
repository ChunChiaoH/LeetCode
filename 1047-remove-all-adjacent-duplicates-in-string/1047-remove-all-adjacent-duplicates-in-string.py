class Solution:
    def removeDuplicates(self, s: str) -> str:
        result_stack = ''
        for ch in s:
            if result_stack and result_stack[-1] == ch:
                result_stack = result_stack[:-1]
            else:
                result_stack += ch
        return result_stack
                