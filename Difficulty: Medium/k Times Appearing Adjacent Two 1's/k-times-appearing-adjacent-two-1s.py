class Solution:
    def countStrings(self, n, k): 
        mod = 10**9 + 7
        dp = [[0, 0] for _ in range(k + 1)]
        
        dp[0][0] = dp[0][1] = 1
        
        for _ in range(n - 1):
            for i in reversed(range(1, k + 1)):
                dp[i][0], dp[i][1] = (dp[i][0] + dp[i][1]) % mod, (dp[i][0] + dp[i - 1][1]) % mod
            dp[0][0], dp[0][1] = (dp[0][0] + dp[0][1]) % mod, dp[0][0]
            
        return sum(dp[k]) % mod
