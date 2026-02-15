#User function Template for python3

class Solution:
    def findMinDiff(self, arr, m):
        n = len(arr)
        
        if m == 0 and n == 0:
            return 0
            
        arr.sort()
        diff = float('inf')
        
        for i in range(n - m + 1):
            x = arr[i + m - 1] - arr[i]
            diff = min(diff, x)
        
        return diff if diff >= 0 else -1