#User function Template for python3
import collections

class Solution:
	def countPairsWithDiffK(self,arr, k):
    	count = 0
    	counter = collections.Counter(arr)
    	
    	for num in arr:
    	    if num + k in counter:
    	        count += counter[num + k]
    	        
    	
    	return count




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends