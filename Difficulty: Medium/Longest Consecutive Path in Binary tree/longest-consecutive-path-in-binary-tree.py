'''
Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def longestConsecutive(self, root):
        def dfs(node, val, ln):
            if node is None:
                return ln
                
            cur = ln + 1 if node.data == val + 1 else 1
            
            return max(ln, dfs(node.left, node.data, cur), dfs(node.right, node.data, cur))

        mx = dfs(root, -1, -1)
        
        return mx if mx > 1 else -1
        