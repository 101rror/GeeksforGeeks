class Solution:
    def isPower(self, x, y):
        if x == 1: 
            return y == 1
            
        if y == 1:
            return True
        
        while y % x == 0:
            y = y // x
            
        return y == 1
