'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxSum(self, root): 
        ans = float('-inf')
        
        def dfs(n):
            nonlocal ans
            if not n:
                return 0
                
            left = dfs(n.left)
            right = dfs(n.right)
            s = n.data
            
            if left > 0:
                s += left
            if right > 0:
                s += right
                
            ans = max(ans, s)
            
            return max(0, n.data, n.data+left, n.data+right)

        dfs(root)
        return ans