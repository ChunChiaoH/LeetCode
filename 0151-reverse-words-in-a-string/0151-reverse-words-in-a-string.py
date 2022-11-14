class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        word = ''
        while s[0] == ' ':
            s = s[1:]
        while s[-1] == ' ':
            s = s[:-1]
        s = s + ' '
        for i, ch in enumerate(s):
            if ch == ' ':
                if word != '':
                    result.append(word)
                    word = ''
            else:
                word += ch
        result += [word] if word else []
        return ' '.join(result[::-1])