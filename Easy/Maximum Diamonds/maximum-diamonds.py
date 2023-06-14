#User function Template for python3
from sortedcontainers import SortedList

class Solution:
    def maxDiamonds(self, A, N, K):
        A = SortedList(A)
        Tsum = 0
        
        while(K):
            x = A.pop()
            Tsum += x
            A.add(x // 2)
            K -= 1
            
        return Tsum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxDiamonds(A,N,K))
# } Driver Code Ends