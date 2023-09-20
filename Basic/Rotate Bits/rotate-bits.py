#User function Template for python3

class Solution:
    def rotate(self, N, D):
        D = D % 16
        N = format(N, '016b')
        
        left = N[len(N) - D:] + N[:len(N) - D]
        right = N[D:] + N[:D]
        
        return [int(right, 2),int(left, 2)]
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0])
        print(ans[1])
# } Driver Code Ends