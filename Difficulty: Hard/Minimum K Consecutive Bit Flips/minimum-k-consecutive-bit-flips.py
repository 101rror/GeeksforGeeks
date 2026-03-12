class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        dp = [0] * n
        flip, ans = 0, 0

        for i in range(n):
            if i >= k:
                flip ^= dp[i-k]

            if arr[i] ^ flip == 0:
                if i + k > n:
                    return -1

                ans += 1
                flip ^= 1
                dp[i] = 1

        return ans
        