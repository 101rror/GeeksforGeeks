class Solution:
    def processQueries(self, arr, queries):
        n = len(arr)
        pref = [1] * n
        suff = [1] * n
        
        for i in range(1, n):
            if arr[i - 1] >= arr[i]:
                pref[i] += pref[i - 1]
                
                
        for i in range(n - 1, 0, -1):
            if arr[i - 1] <= arr[i]:
                suff[i-1] += suff[i]
                
        ans = []
        
        for l, r in queries:
            if suff[l] + pref[r] - 1 >= r - l + 1:
                ans.append(True)
            else:
                ans.append(False)
                
        return ans
        