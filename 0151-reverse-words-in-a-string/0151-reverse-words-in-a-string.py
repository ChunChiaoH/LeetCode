class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        word = ''
        strip_s = s.strip()
        ls = len(strip_s)
        
        for i, ch in enumerate(strip_s):
            if ch == ' ':
                if word != '':
                    result.append(word)
                    word = ''
            else:
                word += ch
                if i == ls-1:
                    result.append(word) 
                    
        return ' '.join(result[::-1])