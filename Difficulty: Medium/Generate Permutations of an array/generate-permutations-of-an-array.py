class Solution:
    def permuteDist(self, arr):
        n = len(arr)
        ans = []
        
        def solve(i):
            if i == n:
                ans.append(arr[:])
                return
                
            for j in range(i, n):
                arr[i], arr[j] = arr[j], arr[i]
                solve(i + 1)
                arr[i], arr[j] = arr[j], arr[i]
                
        solve(0)
        return ans
            
            
        