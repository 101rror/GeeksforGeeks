class Solution:
    def maxIndexDifference(self, s):
        n = len(s)
        dp = [-1] * 26
        ans = -1

        for i in range(n - 1, -1, -1):
            x = i
            idx = ord(s[i]) - ord('a')

            if idx < 25 and dp[idx + 1] != -1:
                x = dp[idx + 1]

            dp[idx] = max(dp[idx], x)

            if s[i] == 'a':
                ans = max(ans, x - i)

        return ans
