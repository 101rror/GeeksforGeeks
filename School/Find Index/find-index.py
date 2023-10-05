#User function Template for python3

class Solution:
    def findIndex (self,a, N, key ):
        ans = []
        
        for i in range(N):
            if(a[i] == key):
                ans.append(i)
                
        if(len(ans) == 1):
            ans.append(ans[0])
            return ans
        if(len(ans) == 0):
            ans.append(-1)
            ans.append(-1)
            return ans
        if(len(ans) > 1):
            x = ans[0]
            y = ans[len(ans) - 1]
            ans.clear()
            ans.append(x)
            ans.append(y)
            return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    key=int(input())
    ob = Solution()
    ans=ob.findIndex(a, n, key )
    print(*ans)
    
# } Driver Code Ends