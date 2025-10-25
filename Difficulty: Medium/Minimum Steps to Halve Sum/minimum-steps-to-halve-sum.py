from heapq import *

class Solution:
  def minOperations(self, arr):
    minheap = []
    c, tsum = 0, sum(arr)
    tar = tsum / 2
    
    for num in arr:
        heappush(minheap, -num)
    
    while minheap:
        if tsum <= tar:
            return c
        num = -heappop(minheap) / 2
        tsum -= num
        c += 1
        heappush(minheap, -num)
        
    return 0