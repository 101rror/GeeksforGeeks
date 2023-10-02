#User function Template for python3

class Solution:
	def distinctSubsequences(self, S):
		mod = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        last = {}
    
        for i in range(1, n + 1):
            dp[i] = (2 * dp[i - 1]) % mod
    
            if s[i - 1] in last:
                dp[i] = (dp[i] - dp[last[s[i - 1]] - 1] + mod) % mod
    
            last[s[i - 1]] = i
    
        return (dp[n] - 1) % mod + 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.distinctSubsequences(s)
		print(answer)

# } Driver Code Ends