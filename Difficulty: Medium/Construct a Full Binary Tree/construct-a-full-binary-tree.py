''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def constructBinaryTree(self, pre, preMirror):
        n = len(pre)

        pos = {}
        for i, x in enumerate(preMirror):
            pos[x] = i

        def build(preL, preR, mirL, mirR):
            if preL > preR:
                return None

            root = Node(pre[preL])

            if preL == preR:
                return root

            leftRoot = pre[preL + 1]
            idx = pos[leftRoot]

            rightSize = idx - mirL - 1
            leftSize = preR - preL - rightSize

            root.left = build(preL + 1, preL + leftSize, idx, mirR)
            root.right = build(preL + leftSize + 1, preR, mirL + 1, idx - 1)

            return root

        return build(0, n - 1, 0, n - 1)
        