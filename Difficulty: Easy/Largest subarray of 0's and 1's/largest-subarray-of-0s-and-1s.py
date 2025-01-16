class Solution:
    def maxLen(self, arr):
        n = len(arr)
        
        for i in range(n):
            if arr[i] == 0:
                arr[i] -= 1
        
        maxlen = 0
        presum = 0
        freq = {}
        
        for idx, num in enumerate(arr):
            presum += num
            
            if presum == 0:
                maxlen = max(maxlen, idx + 1)
            if presum in freq:
                maxlen = max(maxlen, idx - freq[presum])
            else:
                freq[presum] = idx
                
        return maxlen
#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends