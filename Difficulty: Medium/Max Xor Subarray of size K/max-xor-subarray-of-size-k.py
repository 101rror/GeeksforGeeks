class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)

        curr = 0
        for i in range(k):
            curr ^= arr[i]
        
        maxx = curr
        
        for i in range(k, n):
            curr ^= arr[i - k]
            curr ^= arr[i]
            
            maxx = max(maxx, curr)
        
        return maxx