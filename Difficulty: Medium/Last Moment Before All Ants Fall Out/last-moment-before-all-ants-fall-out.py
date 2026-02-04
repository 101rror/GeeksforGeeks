class Solution:
    def getLastMoment(self, n, left, right):
        maxl = max(left, default = 0)
        maxr = min(right, default = n)
        
        return max(maxl - 0, n - maxr)