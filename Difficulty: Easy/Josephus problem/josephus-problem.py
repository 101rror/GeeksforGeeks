class Solution:
    def josephus(self, n, k):
        ans = []
        
        for i in range(1, n + 1):
            ans.append(i)
            
        x = 0
        while len(ans) > 1:
            x = (x + k - 1) % len(ans)
            ans.pop(x)
            
        return ans[0]