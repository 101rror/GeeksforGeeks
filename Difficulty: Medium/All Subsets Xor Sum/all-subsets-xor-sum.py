class Solution:
    def subsetXORSum(self, arr):
        n = len(arr) - 1
        bitOR = 0
        
        for x in arr:
            bitOR |= x
            
        ans = bitOR * (1 << n)
            
        return ans