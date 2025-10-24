class Solution:
    def isPossible(self, arr, k):
        brr = []
        
        for num in arr:
            flag = 1
            for subs in brr[::-1]:
                if subs[-1] == num - 1:
                    subs.extend([num])
                    flag = 0
                    break
            if(flag):
                brr.append([num])
            
        mn = float('inf')
        for subs in brr:
            mn = min(mn, len(subs))
            
        if mn >= k:
            return True
            
        return False