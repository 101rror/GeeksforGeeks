class Solution:
    def longestPath(self, mat, xs, ys, xd, yd):
        m, n = len(mat), len(mat[0])

        def moves(x: int, y: int):
            if x > 0:
                yield (x - 1, y)
            if x < m - 1:
                yield (x + 1, y)
            if y > 0:
                yield (x, y - 1)
            if y < n - 1:
                yield (x, y + 1)

        def dfs(x: int, y: int, dist: int) -> int:
            if mat[x][y] == 0:
                return -1
            if x == xd and y == yd:
                return dist
                
            mat[x][y] = 0
            mx = max(dfs(x1, y1, dist + 1) for x1, y1 in moves(x, y))
            mat[x][y] = 1
            return mx

        return dfs(xs, ys, 0)
