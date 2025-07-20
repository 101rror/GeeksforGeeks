class Solution:
    def countValid(self, n, arr):
        arr = set(arr)
        ln = len(arr)
        
        if n == 1:
            return ln - 1 if 0 in arr else ln
            
        total = 9 * 10 ** (n - 1) - (10 - ln) ** n
        
        if 0 not in arr:
            total += (10 - ln) ** (n - 1)
            
        return total