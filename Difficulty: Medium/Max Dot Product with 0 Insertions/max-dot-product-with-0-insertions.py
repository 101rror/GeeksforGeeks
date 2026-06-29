class Solution:
    def maxDotProduct(self, a, b):
        n = len(b)
        dp = [0] * (n + 1)

        for i, x in enumerate(a):
            for j in range(min(i + 1, n) - 1, -1, -1):
                dp[j + 1] = max(dp[j + 1], dp[j] + x * b[j])

        return dp[n]
        