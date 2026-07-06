class Solution:
    def maxPathSum(self, a, b):
        n, m = len(a), len(b)
        i = j = 0
        sum1 = sum2 = ans = 0

        while i < n and j < m:
            if a[i] < b[j]:
                sum1 += a[i]
                i += 1
            elif a[i] > b[j]:
                sum2 += b[j]
                j += 1
            else:
                ans += max(sum1, sum2) + a[i]
                sum1 = sum2 = 0
                i += 1
                j += 1

        while i < n:
            sum1 += a[i]
            i += 1

        while j < m:
            sum2 += b[j]
            j += 1

        ans += max(sum1, sum2)

        return ans
