class Solution:
    def sortBySetBitCount(self, arr):
        def countSetBit(n):
            count = 0
            
            while n:
                n = n & (n - 1)
                count += 1
                
            return count
            
        ans = sorted(arr, reverse=True, key = lambda a:countSetBit(a))
        
        return ans
        