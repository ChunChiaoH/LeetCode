class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        freq1 = {}
        freq2 = {}
        
        ## compute frequency table
        for d in word1:
            freq1[d] = 1 if d not in freq1 else freq1[d]+1
        for d in word2:
            freq2[d] = 1 if d not in freq2 else freq2[d]+1
        
        all_alphabets = sorted(list(set(word1 + word2)))
        for a1 in all_alphabets:
            for a2 in all_alphabets:
                if (a1 not in freq1) or (a2 not in freq2):
                    continue
                # swap a1(from word1) with a2(from word2)
                freq1[a1] -= 1
                freq2[a1] = freq2[a1]+1 if a1 in freq2 else 1
                freq1 = {k:v for k, v in freq1.items() if v>0}
                    
                freq1[a2] = freq1[a2]+1 if a2 in freq1 else 1
                freq2[a2] -= 1
                freq2 = {k:v for k, v in freq2.items() if v>0}
                
                if len(freq1) == len(freq2):
                    return True
                
                # swap back
                freq1[a1] = freq1[a1]+1 if a1 in freq1 else 1
                freq2[a1] = freq2[a1]-1
                freq2 = {k:v for k, v in freq2.items() if v>0}
                
                freq1[a2] = freq1[a2]-1
                freq2[a2] = freq2[a2]+1 if a2 in freq2 else 1
                freq1 = {k:v for k, v in freq1.items() if v>0}
                
        return False
                
                    
