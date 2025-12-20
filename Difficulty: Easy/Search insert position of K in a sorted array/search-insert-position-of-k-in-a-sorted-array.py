class Solution:
    def searchInsertK(self, arr, k):
        n = len(arr)
        
        if k < arr[0]:
            return 0
        elif k > arr[n-1]:
            return n
            
        for i in range(n):
            if arr[i] == k or arr[i] > k:
                return i
        