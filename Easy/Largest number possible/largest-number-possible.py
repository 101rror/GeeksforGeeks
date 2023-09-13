#User function Template for python3

class Solution:
    def findLargest(self, N, S):
        a = []
        st = ''
        T = S
        tsum = 0
        
        if((N > 1 and S == 0) or (N * 9 < S)):
            return -1
        
        while(N):
            if(S >= 9):
                st += '9'
                S -= 9
            else:
                st += str(S)
                S -
            N -= 1
            
        return st
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends