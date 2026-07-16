from functools import lru_cache

class Solution:
    def countWays(self, n, sum):

        @lru_cache(None)
        def dp(pos, rem):
            if pos == n:
                return 1 if rem == 0 else 0
            if rem < 0:
                return 0

            ans = 0
            start = 1 if pos == 0 else 0
            
            for d in range(start, 10):
                if d <= rem:
                    ans += dp(pos + 1, rem - d)
                    
            return ans

        ans = dp(0, sum)

        return ans if ans > 0 else -1
