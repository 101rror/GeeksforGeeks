#User function Template for python3
class Solution:

	def immediateSmaller(self,arr,n):
		for i in range(1, n):
		    if arr[i - 1] > arr[i]:
		        arr[i - 1] = arr[i]
		    else:
		        arr[i - 1] = -1
		        
		arr[n - 1] = -1
		        
		return arr


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob = Solution()
        ob.immediateSmaller(arr,n)
        for x in arr:
            print(x, end=" ")
        print()
        print("~")
# } Driver Code Ends