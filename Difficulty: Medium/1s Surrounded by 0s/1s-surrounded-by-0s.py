from itertools import chain, product

class Solution:
    def cntOnes(self, grid):
        DXDY = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        
        if m == 1 or n == 1:
            return 0
            
        s = []
        
        for x, y in chain(product(range(m), [0, n - 1]), product([0, m - 1], range(1, n - 1))):
            if grid[x][y]:
                s.append((x, y))
                grid[x][y] = 2
                
        while s:
            x, y = s.pop()
            for dx, dy in DXDY:
                x1, y1 = x + dx, y + dy
                if not (0 <= x1 < m and 0 <= y1 < n and grid[x1][y1] == 1):
                    continue
                
                grid[x1][y1] = 2
                s.append((x1, y1))
                
        return sum(grid[x][y] == 1 for x in range(m) for y in range(n))
        