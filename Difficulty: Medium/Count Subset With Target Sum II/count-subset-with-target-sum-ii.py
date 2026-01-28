from collections import Counter

class Solution:
    def countSubset(self, arr, k):
        n = len(arr)
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        def subSum(nums):
            tSum = [0]
            for x in nums:
                tSum += [s + x for s in tSum]
            return tSum

        lSum = subSum(left)
        rSum = subSum(right)

        counter = Counter(rSum)

        ans = 0
        for s in lSum:
            ans += counter[k - s]

        return ans
