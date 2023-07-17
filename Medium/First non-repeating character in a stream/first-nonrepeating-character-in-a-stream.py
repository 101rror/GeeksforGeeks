#User function Template for python3

class Solution:
	def FirstNonRepeating(self, A):
		ans = []
		ans.append(A[0])
		a = ''
		a += A[0]
		temp = []
		temp.append(A[0])
		
		for i in range(1, len(A)):
		    if(A[i] not in temp):
		        ans.append(A[i])
		        temp.append(A[i])
		    elif(A[i] in ans):
		        ans.remove(A[i])
		    if(len(ans) > 0):
		        a += ans[0]
		    else:
		        a += '#'
		        
	    return a


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends