class Solution:
    def findPosition(self, n):
        if n & (n - 1) == 0:
            return n.bit_length()
            
        return -1