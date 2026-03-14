'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque


class Solution:
    def topView(self, root):
        left, right = [], []
        q = deque([(root, 0)])
        
        while q:
            node, i = q.popleft()
            
            if node is None:
                continue
            if i < 0:
                if -i > len(left):
                    left.append(node.data)
            else:
                if i == len(right):
                    right.append(node.data)
                    
            q.append((node.left, i - 1))
            q.append((node.right, i + 1))
            
        left.reverse()
        left.extend(right)
        
        return left
        