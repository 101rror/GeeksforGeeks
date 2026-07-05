class Solution:
    def maxCharGap(self, s: str) -> int:
        n = len(s)
        freq = {}
        mx = -1
          
        for i in range(n):
            if s[i] in freq:
                gap = i - freq[s[i]] - 1
                mx = max(mx, gap)
            else:
                freq[s[i]] = i
          
        return mx
