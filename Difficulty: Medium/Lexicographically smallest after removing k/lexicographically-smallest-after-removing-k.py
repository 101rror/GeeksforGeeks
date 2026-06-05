class Solution:
    def lexicographicallySmallest(self, s, k):
        n = len(s)
        
        if n & (n - 1) == 0:
            k //= 2
        else:
            k *= 2
            
        if k >= n:
            return "-1"
        
        stack = []
        
        for ele in s:
            while stack and k != 0 and stack[-1] > ele:
                stack.pop()
                k -= 1
            stack.append(ele)
            
        while k:
            stack.pop()
            k -= 1
            
        return ''.join(stack) if k == 0 else "-1"
        