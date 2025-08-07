class Solution:
    def minDifference(self, arr):
        total = 24 * 60 * 60
        ans = total
        
        def conv(s):
            a = list(map(int, s.split(":")))
            return a[0] * 60 * 60 + a[1] * 60 + a[2]
            return curr
            
        new = sorted(list(map(conv, arr)))
        
        for i in range(1, len(new)):
            ans = min(ans, new[i] - new[i - 1])
            
        ans = min(ans, total - new[-1] + new[0])
        
        return ans