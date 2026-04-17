class Solution:
    def canFormPalindrome(self, s):
        freq = {}
        
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1 
                
        odd = 0
        
        for val in freq.values():
            if val & 1 == 1:
                odd += 1
                
        return odd < 2
        