from heapq import heapify, heapreplace

class Solution:
    def minTime(self, ranks, n):
        heap = [(r, 1, r) for r in ranks]
        heapify(heap)
        
        for _ in range(n - 1):
            time, count, rank = heap[0]
            heapreplace(heap, (time + (count + 1) * rank, count + 1, rank))
            
        return heap[0][0]