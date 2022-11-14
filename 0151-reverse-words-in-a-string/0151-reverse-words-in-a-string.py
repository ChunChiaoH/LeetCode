class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        word = ''
        for i, ch in enumerate(s):
            if ch == ' ':
                if word != '':
                    result.append(word)
                    word = ''
            else:
                word += ch
        result += [word] if word else []
        return ' '.join(result[::-1])