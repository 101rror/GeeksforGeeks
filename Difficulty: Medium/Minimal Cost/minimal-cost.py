#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution: 
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [float("inf")] * (n + 1)
        dp[1] = 0
        
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if n - j >= 0:
                    dp[i] = min(dp[i], abs(arr[i - 1] - arr[i - 1 - j]) + dp[i - j])
                    
        return dp[n]
        
        
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minimizeCost(k,arr)
        print(res)
        t -= 1


# } Driver Code Ends