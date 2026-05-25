class Solution:
    def checkElements(self, start, end, arr):
        for i in range(start, end + 1):
            if i not in arr:
                return False
                
        return True
        
