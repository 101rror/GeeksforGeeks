'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def minTime(self, root, target):
        def find(root,target):
            if not root:
                return (0,0,-10**8)
                
            lh, l, la = find(root.left, target)
            rh, r, ra = find(root.right, target)
            
            if root.data == target:
                return (1 + max(lh, rh), 1, max(lh, rh))
            if l:
                return (1 + max(lh, rh), l + 1, max(la, l + rh))
            if r:
                return (1 + max(lh, rh), r + 1, max(ra, r + lh))
                
            return (1 + max(lh, rh), 0, max(la, ra))
            
        h, d, ans = find(root, target)
        
        return ans
