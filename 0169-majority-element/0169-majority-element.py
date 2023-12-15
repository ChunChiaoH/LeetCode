class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = 1 if num not in freq else freq[num] +1
        
        max_freqv = 0
        max_freqk = ''
        for k, v in freq.items():
            if v > max_freqv:
                max_freqv = v
                max_freqk = k
                
        return max_freqk