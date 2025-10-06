class Solution:
    def knightTour(self, n):
        board = [[-1 for _ in range(n)] for _ in range(n)]
        mx = [2, 1, -1, -2, -2, -1, 1, 2]
        my = [1, 2, 2, 1, -1, -2, -2, -1]

        board[0][0] = 0

        def is_safe(x, y):
            return 0 <= x < n and 0 <= y < n and board[x][y] == -1

        def solve(x, y, step):
            if step == n * n:
                return True
            for i in range(8):
                nx, ny = x + mx[i], y + my[i]
                if is_safe(nx, ny):
                    board[nx][ny] = step
                    if solve(nx, ny, step + 1):
                        return True
                    board[nx][ny] = -1
            return False

        if solve(0, 0, 1):
            return board
        else:
            return []