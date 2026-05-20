class Solution:
    def isProduct(self, arr, target):
        for num in arr:
            if num == 0:
                continue
            
            rem = target % num
            div = target // num
            
            
            if rem == 0 and div in arr and div != num:
                return True
            elif rem == 0 and div == num and arr.count(num) > 1:
                return True
                
        return False