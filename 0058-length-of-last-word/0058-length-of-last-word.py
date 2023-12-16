class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = ''
        for c in s[::-1]:
            if c == ' ':
                if res != '':
                    break
            else:
                res += c
        return len(res)
            