class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        preSum = {0:-1}
        curr, ans = 0, 0
        
        for i in range(n):
            curr += (1 if arr[i] > k else -1)
            if curr <= 0:
                if curr - 1 in preSum:
                    ans = max(ans, i - preSum[curr - 1])
            else:
                ans = max(ans, i + 1)
                
            if curr not in preSum:
                preSum[curr] = i
                
        return ans
        