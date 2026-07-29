from collections import Counter

class Solution:
    def minSubsets(self, arr):
        counter = Counter(arr)
        ans = 0

        for num in arr:
            if num - 1 in counter:
                continue
            ans += 1

        return ans
