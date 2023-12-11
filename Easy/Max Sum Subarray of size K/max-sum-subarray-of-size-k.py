#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        tsum = sum(Arr[:K])
        mx = tsum

        for i in range(K, N):
            tsum = tsum - Arr[i - K] + Arr[i]
            mx = max(mx, tsum)

        return mx

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends