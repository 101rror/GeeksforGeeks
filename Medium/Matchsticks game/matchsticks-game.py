#User function Template for python3

class Solution:
    def matchGame(self, N):
        check = (N % 5)
        
        if(check):
            return check
        else:
            return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.matchGame(N))
# } Driver Code Ends