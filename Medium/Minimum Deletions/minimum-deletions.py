#User function Template for python3

class Solution:
    def minimumNumberOfDeletions(self,S):
        n = len(S)
        
        def lcs(s):
            n1 = len(s)
            dp = [[0]*(n1 + 1) for i in range(n1 + 1)]
            rev = s[::-1]
            
            for i in range(1, n1 + 1):
                for j in range(1, n1 + 1):
                    if s[i - 1] == rev[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i][j - 1],dp[i - 1][j])
            return dp[n][n]
            
        return n - lcs(S)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends