class Solution:
    def find(self, arr):
        x = 0

        for val in reversed(arr):
            x = (x + val + 1) // 2

        return x
