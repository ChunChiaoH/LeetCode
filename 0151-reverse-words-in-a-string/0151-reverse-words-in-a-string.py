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
                if i == len(s)-1:
                    result.append(word+ch)
                else:
                    word += ch
        return ' '.join(result[::-1])