class Solution:
    def countWays(self, s1, s2):
        m = len(s1)
        n = len(s2)
        mod = 10**9 + 7
        
        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        def recu(i, j):
            if i == m:
                if j == n:
                    return 1
                return 0

            if j == n:
                return 1

            if dp[i][j] != -1:
                return dp[i][j]

            if s1[i] == s2[j]:
                dp[i][j] = (recu(i + 1, j + 1) + recu(i + 1, j)) % mod
            else:
                dp[i][j] = recu(i + 1, j) % mod

            return dp[i][j]

        return recu(0, 0)
        