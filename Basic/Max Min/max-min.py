class Solution:
    def findSum(self,A,N): 
        mx = max(A)
        mn = min(A)
        
        sum = (mx + mn)
        
        return sum



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
# } Driver Code Ends