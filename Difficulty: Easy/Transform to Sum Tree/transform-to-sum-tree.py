''' Structure for Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

'''
class Solution:
    def toSumTree(self, root):
        def convert(node):
            if node is None:
                return 0
            
            val = node.data
            left = convert(node.left)
            right = convert(node.right)
            
            node.data = left + right
            
            return val + node.data
        
        convert(root)
        