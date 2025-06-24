class Solution:
    def maxSubseq(self, s, k):
        n = len(s)
        stack = []
        temp = k
        
        for i in range(n):
            while temp and stack and stack[-1] < s[i]:
                stack.pop()
                temp -= 1
            stack.append(s[i])
            
        return "".join(stack[ : n - k])
        