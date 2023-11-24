#User function Template for python3

#User function Template for python3
class Solution:

	def nthRowOfPascalTriangle(self,n):
	    mod=10**9+7
	    
	    if n == 1:
	        return [1]
	        
	    else:
	        arr = [1]
	        for i in range(1, n):
	            ans = [1]
	            for j in range(i - 1):
	                ans.append((arr[j + 1] + arr[j]) % mod)
	            ans.append(1)
	            arr = ans
	            
	        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    ob = Solution()
	    ans=ob.nthRowOfPascalTriangle(n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends