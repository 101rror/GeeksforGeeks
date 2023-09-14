class Solution:
    def perfectSum(self, numbers, length, targetSum):
        dp = [1] + [0] * targetSum

        MOD = (10**9 + 7)

        for number in numbers:
            for currentSum in range(targetSum, number - 1, -1):
                dp[currentSum] = (dp[currentSum] + dp[currentSum - number]) % MOD
        
        return dp[targetSum]
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends