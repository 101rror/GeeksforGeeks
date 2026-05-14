class Solution:
    def search(self, a, b):
        n, m = len(a), len(b)

        dp = [0] * m
        j = 0

        for i in range(1, m):
            while j > 0 and b[i] != b[j]:
                j = dp[j - 1]

            if b[i] == b[j]:
                j += 1
                dp[i] = j

        ans = []
        j = 0

        for i in range(n):
            while j > 0 and a[i] != b[j]:
                j = dp[j - 1]

            if a[i] == b[j]:
                j += 1

            if j == m:
                ans.append(i - m + 1)
                j = dp[j - 1]

        return ans
        