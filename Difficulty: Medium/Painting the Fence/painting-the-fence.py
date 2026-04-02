class Solution:
    def countWays(self,n,k):
        mod = 10**9 + 7
        dp = [k, k**2, k**3 - k] + [0]*(n - 3)

        for i in range(3, n):
            dp[i] = (k * dp[i - 1] - (k - 1) * dp[i - 3]) % mod
        
        return dp[n - 1]
