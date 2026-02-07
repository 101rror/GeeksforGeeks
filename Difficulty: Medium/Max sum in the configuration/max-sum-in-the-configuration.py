class Solution:
    def maxSum(self, arr): 
        n = len(arr)
        tSum = sum(arr)
        cSum = 0
        
        for i in range(n):
            cSum += i * arr[i]
            
        mSum = cSum
        
        for i in range(1, n):
            cSum = cSum + tSum - n * arr[n - i]
            mSum = max(mSum, cSum)
        
        return mSum