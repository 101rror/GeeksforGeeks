class Solution:
    def maxSumSubarray(self, arr):
        pos = s = lst = 0
        mx = -sys.maxsize
        flag = False
        
        for i in arr:
            if i < 0:
                lst = min(i, lst)
                if flag and pos > s - lst + i:
                    s = pos
                    lst = i
                flag = True
            s += i
            pos += i
            mx = max(mx, s - lst)
            
            if pos < 0:
                pos = 0
                
        return max(arr) if mx == 0 else mx
        