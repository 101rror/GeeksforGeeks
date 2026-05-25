class Solution:
    def minToggle(self, arr):
        n = len(arr)
        ones =  arr.count(1)
        ans = n
        changed = 0
        
        for i in reversed(range(n)):
            if arr[i] == 0:
                changed += 1
            else:
                ones -= 1
            
            ans = min(ans, ones + changed)

        
        return min(ans, arr.count(1))