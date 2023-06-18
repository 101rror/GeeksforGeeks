class Solution:
    def distributeTicket(self, N : int, K : int) -> int:
        left, right = 1, N
        
        while (True):
            if (left + K >= right):
                return right
            left += K
            
            if (right - K <= left):
                return left
            right -= K
            
        return right
        

#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    
    N, K = map(int, input().split())
    
    obj = Solution()
    res = obj.distributeTicket(N, K)
    
    print(res)
# } Driver Code Ends