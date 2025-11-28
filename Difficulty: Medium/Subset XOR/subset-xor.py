class Solution:
    def subsetXOR(self, n : int):
        ans = []
        total = 0
        
        for i in range(1, n + 1):
            total ^= i
            
        if total == n:
            ans = list(range(1, n + 1))
        else:
            x = total ^ n
            ans = [i for i in range(1, n + 1) if i != x]
            
        return ans
        
