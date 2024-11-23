#User function Template for python3

class Solution:
    def getMinDiff(self,k, arr):
        arr.sort()
        n = len(arr)
        
        ans = arr[-1] - arr[0]
        
        for i in range(1, n):
            mn = min(arr[0] + k, arr[i] - k)
            mx = max(arr[i - 1] + k, arr[-1] - k)
            
            ans = min(ans, mx - mn)
        
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.getMinDiff(k, arr)
        print(res)
        print("~")

# } Driver Code Ends