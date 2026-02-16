class Solution:
    def canAttend(self, arr):
        n = len(arr)
        arr.sort()
        
        start = arr[0][0]
        end = arr[0][1]
        
        for i in range(1, n):
            if arr[i][0] >= end:
                start = arr[i][0]
                end = arr[i][1]
            else:
                return False
            
        
        return True
        