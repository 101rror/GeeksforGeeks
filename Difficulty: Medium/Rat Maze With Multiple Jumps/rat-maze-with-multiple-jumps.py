class Solution:
	def shortestDist(self, mat):
        n = len(mat)

        if n == 1:
            return [[1]]

        ans = [[0] * n for _ in range(n)]
        bad = [[False] * n for _ in range(n)]

        def dfs(i, j):
            if i == n - 1 and j == n - 1:
                ans[i][j] = 1
                return True

            if bad[i][j]:
                return False
                
            if mat[i][j] == 0:
                return False

            ans[i][j] = 1

            for jump in range(1, mat[i][j] + 1):
                nj = j + jump
                if nj < n and ans[i][nj] == 0:
                    if dfs(i, nj):
                        return True

                ni = i + jump
                if ni < n and ans[ni][j] == 0:
                    if dfs(ni, j):
                        return True

            ans[i][j] = 0
            bad[i][j] = True
            return False

        return ans if dfs(0, 0) else [[-1]]
