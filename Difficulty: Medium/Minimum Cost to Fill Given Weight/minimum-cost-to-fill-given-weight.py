class Solution:
    def minimumCost(self, cost, w):
        n = len(cost)
        dp = [float('inf')]*(w + 1)
        dp[0] = 0

        for i in range(n):
            if cost[i] == -1:
                continue

            wt = i + 1

            for j in range(wt, w + 1):
                if dp[j - wt] != float('inf'):
                    dp[j] = min(dp[j], cost[i] + dp[j - wt])

        return -1 if dp[w] == float('inf') else dp[w]
