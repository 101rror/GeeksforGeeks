#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:

	def maxProduct(self,arr):
		first = max(arr)
		idx = arr.index(first)
		second = 0
		
		for i in range(len(arr)):
		    if i != idx and arr[i] > second:
		        second = arr[i]
		        
		return first * second
		

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxProduct(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends