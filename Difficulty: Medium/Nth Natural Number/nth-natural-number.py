#User function Template for python3

class Solution:
    def findNth(self,n):
        def solve(n):
            if n < 9:
                return n
            else:
                return 10 * solve(n // 9) + n % 9
                
        return solve(n)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)

# } Driver Code Ends