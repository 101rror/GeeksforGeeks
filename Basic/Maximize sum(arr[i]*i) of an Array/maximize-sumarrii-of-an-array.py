#User function Template for python3

class Solution:
    def Maximize(self, a, n): 
        tsum = 0
        a = sorted(a)
        mod = 1000000007
        
        for i in range(1, n):
            tsum += a[i] * i
            
        return tsum % mod



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    print(ob.Maximize(arr, n))
    
# } Driver Code Ends