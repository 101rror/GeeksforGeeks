class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        stack = []
        count = 0
        
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
                
            nxt = stack[-1] if stack else n
            count += nxt - i
            stack.append(i)
            
        return count
        