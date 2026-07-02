class Solution:
    def divisibleByK(self, arr, k):
        dp = [False] * k

        for num in arr:
            ndp = dp[:]

            ndp[num % k] = True

            for r in range(k):
                if dp[r]:
                    ndp[(r + num) % k] = True

            dp = ndp

            if dp[0]:
                return True

        return False
        