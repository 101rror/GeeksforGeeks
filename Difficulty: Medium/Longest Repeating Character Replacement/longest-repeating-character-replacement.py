class Solution:
    def longestSubstr(self, s, k):
        freq = {}
        left = mx = 0

        for right, c in enumerate(s):
            freq[c] = freq.get(c, 0) + 1

            while (sum(freq.values()) - max(freq.values())) > k:
                freq[s[left]] -= 1
                left += 1

            mx = max(mx, right - left + 1)

        return mx
        