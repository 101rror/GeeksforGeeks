class Solution:
    def canSplit(self, arr):
        n = len(arr)
        tSum = sum(arr)
        cSum = 0
        
        for i in range(n):
            if cSum == (tSum - cSum):
                return True
            
            cSum += arr[i]
                
        return False
        