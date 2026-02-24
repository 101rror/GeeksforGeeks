class Solution:
    def equalSumSpan(self, a1, a2):
        n = len(a1)
        
        preSum = 0
        mx = 0
        freq = {}
        
        for i in range(n):
            preSum += (a1[i] - a2[i])
            
            if preSum == 0:
                mx = i + 1
            
            if preSum in freq:
                mx = max(mx, i - freq[preSum])
            else:
                freq[preSum] = i
        
        return mx
        