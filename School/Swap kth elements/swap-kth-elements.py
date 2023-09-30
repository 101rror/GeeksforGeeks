#User function Template for python3
class Solution:
	
	def swapKth(self,arr, n, k):
		arr[k - 1], arr[n - k] = arr[n - k], arr[k - 1]
	            
	    return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3






if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.swapKth(arr, n, k)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends