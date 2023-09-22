#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        idx = []
        ans = []
        
        for i in range(n):
            if(arr[i] == x):
                idx.append(i)
                
        if(len(idx) == 0):
            return [-1, -1]
                
        ans.append(idx[0])
        ans.append(idx[len(idx) - 1])
                
        return ans


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends