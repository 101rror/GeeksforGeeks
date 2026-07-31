class Solution:
    def __init__(self):
        self.MOD = 10**9 + 7
        self.mp = [0] * 31

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        for i in range(2, 31):
            if i % 4 == 0 or i % 9 == 0 or i == 25:
                continue

            mask = 0
            for j, p in enumerate(primes):
                if i % p == 0:
                    mask |= (1 << j)

            self.mp[i] = mask

    def countSubsets(self, arr):
        one = 0
        cnt = [0] * 31
        dp = [0] * 1024
        dp[0] = 1

        for x in arr:
            if x == 1:
                one += 1
            elif self.mp[x] != 0:
                cnt[x] += 1

        for i in range(2, 31):
            if cnt[i] == 0:
                continue

            for mask in range(1024):
                if mask & self.mp[i]:
                    continue
                dp[mask | self.mp[i]] = (dp[mask | self.mp[i]] + dp[mask] * cnt[i]) % self.MOD

        ans = (sum(dp) - 1) % self.MOD

        if one:
            ans = ans * pow(2, one, self.MOD) % self.MOD

        return ans
        