class Solution:
    def sumSubMins(self, arr):
        arr.append(0) 
        stack = [-1] 
        ans = 0
        
        for i in range(len(arr)):
            while arr[i] < arr[stack[-1]]:
                idx = stack.pop()
            
                ans += arr[idx] * (idx - stack[-1]) * (i - idx)
                
            stack.append(i)
            
        return ans
        