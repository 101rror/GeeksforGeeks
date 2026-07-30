class Solution:
    def maxSubsetXOR(self, arr):
        dp = [0] * 21
        
        for x in arr:
            for i in range(20, -1, -1):
                if (x >> i) & 1:
                    if dp[i]:
                        x ^= dp[i]
                    else:
                        dp[i] = x
                        break
        ans = 0
        
        for i in range(20, -1, -1):
            ans = max(ans, ans ^ dp[i])
            
        return ans
        