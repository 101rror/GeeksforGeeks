#User function Template for python3

class Solution:
	def seriesSum(self,n):
	    n = (n * (n + 1)) // 2
	    
	    return n
 


#{ 
 # Driver Code Starts
                               #Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.seriesSum(n)
        print(ans)
        tc=tc-1
# } Driver Code Ends