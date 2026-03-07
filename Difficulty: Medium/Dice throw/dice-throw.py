class Solution:
    def noOfWays(self, m, n, x):
        dp = [0] * (x + 1)
        dp[0] = 1
        
        for _ in range(n):
            ndp = [0] * ( x + 1)
            for s in range(x + 1):
                if dp[s] != 0:
                    for face in range(1, m + 1):
                        if s + face <= x:
                            ndp[s + face] += dp[s]
                            
            dp = ndp
            
        return dp[x]