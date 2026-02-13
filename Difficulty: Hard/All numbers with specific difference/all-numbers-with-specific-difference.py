class Solution:
    def digitSum(self, x):
        summ = 0
        while x > 0:
            summ += x % 10
            x //= 10
        return summ
    
    def getCount(self, n, d):
        left, right = 1, n
        start = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid - self.digitSum(mid) >= d:
                start = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if start == -1:
            return 0
        
        return n - start + 1
        