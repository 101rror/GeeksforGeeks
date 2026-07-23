class Solution:
    def canRepresentBST(self, arr):
        stack = []
        root = float('-inf')

        for x in arr:
            if x < root:
                return 0

            while stack and stack[-1] < x:
                root = stack.pop()

            stack.append(x)

        return 1
        