# Definition for Node
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Solution:
    def isSubTree(self, root1, root2):
        if not root1:
            return False
            
        def helper(r1, r2):
            if r1 is None and r2 is None:
                return True
            if r1 is None or r2 is None or r1.data != r2.data:
                return False
                
            return helper(r1.left,r2.left) and helper(r1.right,r2.right)
            
            
        if helper(root1, root2):
            return True
            
        return self.isSubTree(root1.left, root2) or self.isSubTree(root1.right, root2)
        