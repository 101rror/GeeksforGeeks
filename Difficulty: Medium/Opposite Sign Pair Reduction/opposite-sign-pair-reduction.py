class Solution:
    def reducePairs(self, arr):
        stack = []
        
        for ele in arr:
            cur = ele
            while stack and (stack[-1] < 0 < cur or stack[-1] > 0 > cur):
                cand = stack.pop()
                
                if abs(cand) == abs(cur):
                    cur = None
                    break
                
                cur = max([cur, cand], key = lambda x : abs(x))
                
            if cur != None:
                stack.append(cur)
                
        return stack
        