class Solution:
    def isSubsetSum (self, arr, sum):
        n = len(arr)
        dp = [False] * (sum + 1)
        dp[0] = True
        
        for num in arr:
            for i in range(sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
                
        return dp[sum]
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(arr, sum) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends