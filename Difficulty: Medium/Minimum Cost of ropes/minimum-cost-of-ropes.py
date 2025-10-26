from heapq import heapify, heappop, heapreplace

class Solution:
   def minCost(self, arr):
        n = len(arr)
        heapify(arr)
        ans = 0
        
        for _ in range(n - 1):
            c = heappop(arr) + arr[0]
            ans += c
            heapreplace(arr, c)
            
        return ans