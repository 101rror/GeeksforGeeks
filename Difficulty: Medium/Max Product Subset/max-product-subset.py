class Solution:
    def findMaxProduct(self, arr):
        arr.sort()
        x, mx = 1, 1

        flag = True
        
        for i in arr:
            t = x * i
            x = mx * i 
            mx = max(i, i if flag else mx, x, t)
            flag = False

        return mx % (10**9 + 7) if mx > 0 else mx
        