class Solution:
    def nextGreater(self, arr):
        narr = arr + arr
        ans = [-1] * len(arr)
        stack = []
        
        for i in range(len(narr)):
            while stack and narr[stack[-1]] < narr[i]:
                idx = stack.pop()
                if idx < len(ans):
                    ans[idx] = narr[i]
                    
            stack.append(i)
            
        return ans