#User function Template for python3

class Solution:
    def cutRod(self, price, N):
       dp = [0]*(N+1)
       
       for i in range(1, N+1):
           dp[i] = price[i-1]
           
           for j in range(1, i+1):
               dp[i] = max(dp[i],dp[j] + dp[i-j])
               
       return dp[-1] 
       

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends