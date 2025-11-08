from functools import lru_cache

class Solution:
    def numberOfPath(self, mat, k):
        m, n = len(mat), len(mat[0])
        
        @lru_cache(None)
        def move(r, c, k):
            nonlocal m, n
            if r >= m or c >= n or k - mat[r][c] < 0:
                return 0
            k -= mat[r][c]
            if (r, c) == (m - 1, n - 1) and k == 0:
                return 1
                
            return move(r + 1, c, k) + move(r, c + 1, k)
        
        return move(0, 0, k)