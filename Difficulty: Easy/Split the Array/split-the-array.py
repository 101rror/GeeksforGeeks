#User function Template for python3
class Solution:
	def countgroup(self,arr):
	    n = len(arr)
		xor = 0
		
		for num in arr:
		    xor = xor ^ num
		    
		return 0 if xor > 0 else 2**(n - 1) - 1


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countgroup(arr)
        print(res)
        t -= 1

# } Driver Code Ends