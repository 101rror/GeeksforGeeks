class Solution:
    def countCoordinates(self, mat):
        n = len(mat)
        m = len(mat[0])

        p = deque([])
        q = deque([])

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    p.append((i, j))
                if i == n - 1 or j == m - 1:
                    q.append((i, j))

        def bfs(b, v):
            while b:
                i, j = b.popleft()
                if (i, j) in v:
                    continue

                v.add((i, j))

                for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    a, c = x + i, y + j

                    if 0 <= a < n and 0 <= c < m and mat[i][j] <= mat[a][c]:
                        b.append((a, c))

        k, h = set(), set()

        bfs(p, k)
        bfs(q, h)

        return len(k & h)
