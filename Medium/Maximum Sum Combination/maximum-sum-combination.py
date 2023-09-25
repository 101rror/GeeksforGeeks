#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

import heapq

class Solution:
    def maxCombinations(self, N, K, A, B):
        A = sorted(A, reverse = True)
        B = sorted(B, reverse = True)
        ans = []
        heap = []
        
        for i in range(N):
            heapq.heappush(heap, (-(A[i] + B[0]), 0))
       
        while(K > 0):
            cur = heapq.heappop(heap)
            ans.append(-cur[0]) 
           
            if cur[1] < N - 1:
                nxt = -(-cur[0] - B[cur[1]] + B[cur[1] + 1])
                heapq.heappush(heap, (nxt, cur[1] + 1))
               
            K -= 1
       
        return ans
            
            
        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, K = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxCombinations(N, K, A, B)
        for val in res:
            print(val, end =' ')
        print()
# } Driver Code Ends