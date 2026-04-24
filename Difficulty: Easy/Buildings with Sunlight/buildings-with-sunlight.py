class Solution:
    def visibleBuildings(self, arr):
        n = len(arr)
        mx = arr[0]
        ans = 1
        
        for i in range(1, n):
            if arr[i] >= mx:
                ans += 1
                mx = arr[i]
                
        return ans
        