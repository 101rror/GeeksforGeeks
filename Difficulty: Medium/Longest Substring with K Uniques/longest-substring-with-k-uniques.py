class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        freq = {}
        
        left, ans = 0, -1

        for right in range(n):
            ch = s[right]
            freq[ch] = freq.get(ch, 0) + 1

            while len(freq) > k:
                lch = s[left]
                freq[lch] -= 1
                if freq[lch] == 0:
                    del freq[lch]
                    
                left += 1

            if len(freq) == k:
                ans = max(ans, right - left + 1)

        return ans
        
        