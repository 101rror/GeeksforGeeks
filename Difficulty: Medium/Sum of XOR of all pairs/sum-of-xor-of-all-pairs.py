class Solution:
    def sumXOR(self, arr):
        n = len(arr)
        ans = 0
        
        for i in range(32):
            ones = sum((x >> i) & 1 for x in arr)
            ans += ones * (n - ones) * (1 << i)
            
        return ans