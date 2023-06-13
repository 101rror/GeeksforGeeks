class Solution:
	def kLargest(self,arr, n, k):
		arr = sorted(arr, reverse = True)
		ans = []
		
		for i in range(0, k):
		    ans.append(arr[i])
		    
		    
		return ans
		
		
#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends