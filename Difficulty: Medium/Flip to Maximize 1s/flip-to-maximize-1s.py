class Solution:
    def maxOnes(self, arr):
        n = len(arr)
        ones, ans = 0, 0
        
        for i in range(n):
            if arr[i] == 1:
                ones += 1
                
        curr = 0
        
        for r in range(n):
            if arr[r] == 0:
                curr += 1
            else:
                curr -= 1
            if curr < 0:
                curr = 0

            ans = max(ans, curr)
            
        return ans + ones
        