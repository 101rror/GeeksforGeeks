#User function Template for python3

class Solution:
    def maximizeMoney(self, N , K):
        if N % 2 != 0:
            N = (N // 2) + 1
        else:
            N //= 2
        
        return N * K


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K = map(int,input().split())
        
        ob = Solution()
        print(ob.maximizeMoney(N,K))
        print("~")
# } Driver Code Ends