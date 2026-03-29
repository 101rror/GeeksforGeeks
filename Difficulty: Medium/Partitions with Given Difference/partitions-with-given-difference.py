class Solution:
    def countPartitions(self, arr, diff):
        tSum = sum(arr)
        
        if (tSum + diff) % 2 != 0 or tSum < diff:
            return 0
            
        tar = (tSum + diff) // 2
        
        dp = [0] * (tar + 1)
        dp[0] = 1
        
        for num in arr:
            for j in range(tar, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[tar]