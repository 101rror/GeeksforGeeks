#User function Template for python3

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self, a, n):
        if(n == 0):
            return 0
        if(n == 1):
            return a[0]
            
        dp = [0] * n
        dp[0] = a[0]
        dp[1] = max(a[0], a[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + a[i])
            
        return dp[n - 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends