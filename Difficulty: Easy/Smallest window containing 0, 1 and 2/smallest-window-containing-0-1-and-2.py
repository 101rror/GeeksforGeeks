class Solution:
    def smallestSubstring(self, s):
        n = len(s)
        left = 0
        freq = {}
        ans = float('inf')
        
        for right in range(n):
            freq[s[right]] = freq.get(s[right], 0) + 1
            
            while len(freq) == 3:
                ans = min(ans, right - left + 1)
                freq[s[left]] -= 1
                
                if freq[s[left]] == 0:
                    del freq[s[left]]
                    
                left += 1
            
        return ans if ans != float('inf') else -1
        