from itertools import chain
class Solution:
    def diagView(self, mat): 
        ans = [[] for _ in range(2 * n - 1)]
        
        for i in range(n):
            for j in range(n):
                ans[i + j].append(mat[i][j])

        return list(chain.from_iterable(ans))
        