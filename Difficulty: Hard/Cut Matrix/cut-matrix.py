class Solution:
    def findWays(self, matrix, k):
        MOD = 10**9 + 7
        R, C = len(matrix), len(matrix[0])

        suff = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                suff[r][c] = matrix[r][c] + suff[r+1][c] + suff[r][c+1] - suff[r+1][c+1]

        next_r = [[R] * C for _ in range(R)]
        next_c = [[C] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                for nr in range(r + 1, R):
                    if suff[r][c] > suff[nr][c]:
                        next_r[r][c] = nr
                        break
                for nc in range(c + 1, C):
                    if suff[r][c] > suff[r][nc]:
                        next_c[r][c] = nc
                        break

        dp = [[1 if suff[r][c] > 0 else 0 for c in range(C)] for r in range(R)]

        for _ in range(2, k + 1):
            new_dp = [[0] * C for _ in range(R)]
            row_sum = [[0] * C for _ in range(R + 1)]
            col_sum = [[0] * (C + 1) for _ in range(R)]
            
            for r in range(R - 1, -1, -1):
                for c in range(C - 1, -1, -1):
                    row_sum[r][c] = (row_sum[r+1][c] + dp[r][c]) % MOD
                    col_sum[r][c] = (col_sum[r][c+1] + dp[r][c]) % MOD

            for r in range(R):
                for c in range(C):
                    if suff[r][c] > 0:
                        nr, nc = next_r[r][c], next_c[r][c]
                        val = 0
                        if nr < R: val = (val + row_sum[nr][c]) % MOD
                        if nc < C: val = (val + col_sum[r][nc]) % MOD
                        new_dp[r][c] = val
            dp = new_dp

        return dp[0][0]
        
