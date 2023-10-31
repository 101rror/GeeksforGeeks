#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
	    idx = 0
	    
	    for i in range(0, n):
	        if(arr[i] != 0):
	            arr[idx] = arr[i]
	            idx += 1
	            
	    while(idx < n):
	        arr[idx] = 0
	        idx += 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends