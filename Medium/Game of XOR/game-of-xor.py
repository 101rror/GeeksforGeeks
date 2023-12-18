#User function Template for python3

class Solution:
    def gameOfXor(self, N , A):
        ans = 0
        
        for i, e in enumerate(A):
            if (i + 1) * (N - i) % 2 == 0:
                ans ^= 0
            else:
                ans ^= e
                
        return ans 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.gameOfXor(N,A))
# } Driver Code Ends