class Solution:
    def countSubstring(self, s):
        n = len(s)
        dp = [0]*(2 * n + 1)
        ans = cur = end = 0
        dp[n] = 1
        
        for i in range(n):
            if(s[i] == '1'):
                end += dp[n + cur]
                cur += 1
            else:
                end -= dp[n + cur - 1]
                cur -= 1            
            ans += end
            dp[n + cur] += 1    
            
        return ans
        