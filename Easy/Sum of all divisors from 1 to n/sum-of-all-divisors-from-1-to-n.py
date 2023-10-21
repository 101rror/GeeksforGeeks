#User function Template for python3


class Solution:
    def sumOfDivisors(self, N):
    	def div(n):
    	    tsum = 0
    	    for i in range(1, n + 1):
    	        if(n % i == 0):
    	            tsum += i
    	            
    	    return tsum
    	            
    	ans = 0
    	
        for i in range(1, N + 1):
            ans += (i * (N // i))
            
        return ans
    	        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
# } Driver Code Ends