#User function Template for python3

class Solution:
	def nthPoint(self,n):
	    if n == 0:
		    return 0
	    if n == 1 or n == 2 or n == 3:
	        return n
	        
	    mod = (10**9 + 7)

		one = 1
		two = 2
		res = 0
		ans = []
		
		ans.append(0)
		ans.append(one)
		ans.append(two)
		
		res = 0
		for _ in range(3, n + 1):
		    res = (one + two) % mod
		    one = two
		    two = res
		    ans.append(res)
		    
		result = (ans[n] % mod)
		
		return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthPoint(n)
		print(ans)
# } Driver Code Ends