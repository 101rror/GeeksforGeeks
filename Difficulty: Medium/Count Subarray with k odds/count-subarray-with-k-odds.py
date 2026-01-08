from collections import defaultdict

class Solution:
    def countSubarrays(self, arr, k):
        freq = defaultdict(int)
        freq[0] = 1
        
        odd, count = 0, 0

        for num in arr:
            if num % 2 == 1:
                odd += 1

            if odd - k in freq:
                count += freq[odd - k]

            freq[odd] += 1

        return count
        