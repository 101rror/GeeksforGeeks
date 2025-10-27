from heapq import*

class Solution:
    def kSmallestPair(self, arr1, arr2, k):
        m, n = len(arr1), len(arr2)
        
        h = [(arr1[0] + arr2[j], 0, j) for j in range(n)]
        
        heapify(h)
        ans = []
        
        while h and len(ans) < k:
            _, i, j = h[0]
            
            ans.append((arr1[i], arr2[j]))
            i += 1
            
            if i < m:
                heapreplace(h, (arr1[i] + arr2[j], i, j))
            else:
                heappop(h)
                
        return ans
