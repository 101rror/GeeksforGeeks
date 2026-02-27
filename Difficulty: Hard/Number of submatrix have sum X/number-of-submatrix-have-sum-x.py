class Solution:
    def countSquare(self, mat, x):
        n  = len(mat)
        m = len(mat[0])
        pre = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(m):
                pre[i + 1][j + 1] = mat[i][j]
                pre[i + 1][j + 1] += pre[i + 1][j]
                pre[i + 1][j + 1] += pre[i][j + 1]
                pre[i + 1][j + 1] -= pre[i][j]
                
        count = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for ln in range(1, min(i,j) + 1):
                    curr = pre[i][j]
                    curr -= pre[i - ln][j]
                    curr -= pre[i][j - ln]
                    curr += pre[i - ln][j - ln]
                    
                    if curr == x:
                        count += 1
                    
        return count
        