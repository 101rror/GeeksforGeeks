class Solution:
    def validGroups(self, s):
        n = len(s)
        memo = [[-1] * 901 for _ in range(n)]
        
        def solve(idx: int, prev_sum: int) -> int:
            if idx == n:
                return 1
                
            if memo[idx][prev_sum] != -1:
                return memo[idx][prev_sum]
                
            current_sum = 0
            ways = 0
            
            for i in range(idx, n):
                current_sum += int(s[i])
                
                if current_sum >= prev_sum:
                    ways += solve(i + 1, current_sum)
                    
            memo[idx][prev_sum] = ways
            return ways

        return solve(0, 0)
        