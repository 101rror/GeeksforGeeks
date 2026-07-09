class Solution:
    def countKdivPairs(self, arr, k):
        mp = {i : 0 for i in range(k)}

        count = 0

        for num in arr:
            g = k - (num % k)
            g = g % k
            count += mp[g]
            mp[num % k] += 1

        return count
