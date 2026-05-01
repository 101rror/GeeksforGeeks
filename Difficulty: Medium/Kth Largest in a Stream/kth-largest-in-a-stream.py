import heapq

class Solution:
    def kthLargest(self, arr, k):
        heap = []
        ans = []
        
        for num in arr:
            heapq.heappush(heap, num)
            
            if len(heap) > k:
                heapq.heappop(heap)
                
            if len(heap) == k:
                ans.append(heap[0])
            else:
                ans.append(-1)
                
        return ans
        