#User function Template for python3

class Solution:
	def findPeakElement(self, a):
		a = sorted(a, reverse = True)
		
		return a[0]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		a = list(map(int,input().split()))
		ob = Solution();
		ans = ob.findPeakElement(a)
		print(ans)




# } Driver Code Ends