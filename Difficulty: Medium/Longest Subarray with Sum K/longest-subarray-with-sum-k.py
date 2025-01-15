# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        n = len(arr)
        if sum(arr) == k:
            return n
        presum = 0
        maxlen = 0
        freq = {}
        
        for i in range(n):
            presum += arr[i]
            
            if presum == k:
                maxlen = i + 1
                
            check = presum - k
                
            if check in freq:
                maxlen = max(maxlen, i - freq[check])
                
            if presum not in freq:
                freq[presum] = i
                
        return maxlen
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends