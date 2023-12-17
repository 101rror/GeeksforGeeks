class Solution:
	def findMaxSum(self,arr, n):
		ans, pre, cur = 0, 0 ,0 
		
		for i in range(n):
		    cur = pre + arr[i]
		    pre = ans
		    ans = max(cur, ans)
		    
		return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends