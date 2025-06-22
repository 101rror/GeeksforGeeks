class Solution:
    def largestSubset(self, arr):
        n = len(arr)
        arr.sort()
        dp = [[num] for num in arr ]
        
        for i in range(n):
           for j in range(i):
             if arr[i] % arr[j] == 0:
                if len(dp[j])  + 1 > len(dp[i]):
                    dp [i] = dp[j] + [arr[i]]
                elif len(dp[j]) + 1 == len(dp[i]):
                     candidate = dp[j] + [arr[i]]
                     if candidate > dp[i]:
                        dp[i] = candidate
        
        maxn = max(len(sub) for sub in dp)
        candidate = [sub for sub in dp if len(sub) == maxn]
        
        return max(candidate)