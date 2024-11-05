#User function Template for python3
class Solution:
	def firstAlphabet(self, S):
		ans = ''
		ans += S[0]
		
		for i in range(len(S)):
		    if S[i] == ' ':
		        ans += S[i + 1]
		        
		return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.firstAlphabet(S)
		
		print(answer)


# } Driver Code Ends