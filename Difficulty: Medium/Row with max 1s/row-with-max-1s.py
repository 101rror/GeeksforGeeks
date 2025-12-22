class Solution:
    def rowWithMax1s(self, arr):
        mx, ans = 0, -1
        
        for i, row in enumerate(arr):
            if (row.count(1) > mx):
                mx = row.count(1)
                ans = i
                
        return ans