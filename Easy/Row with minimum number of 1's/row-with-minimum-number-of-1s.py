#User function Template for python3

class Solution:
    def minRow(self,n,m,a):
        if not a:
            return 1
            
        row = a[0].count(1)
        ans = 0
        
        for i in range(len(a)):
            x = a[i].count(1)
            
            if x < row:
                row = x
                ans = i
                
        ans += 1
        
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.minRow(N,M,A))
# } Driver Code Ends