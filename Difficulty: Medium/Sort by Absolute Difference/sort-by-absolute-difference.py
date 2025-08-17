class Solution:
    def rearrange(self, arr, x):
        arr.sort(key=lambda item:abs(item - x))
        
        return arr
        
        