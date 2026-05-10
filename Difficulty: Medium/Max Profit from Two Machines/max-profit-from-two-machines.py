class Solution:
    def maxProfit(self, x, y, a, b):
        n = len(a)
        ans = 0
        
        tasks = list(range(n))
        tasks.sort(key=lambda task: abs(a[task] - b[task]), reverse=True)
        
        for task in tasks:
            if (a[task] >= b[task] and x > 0) or y == 0:
                ans += a[task]
                x -= 1
            else:
                ans += b[task]
                y -= 1
                
                
        return ans
