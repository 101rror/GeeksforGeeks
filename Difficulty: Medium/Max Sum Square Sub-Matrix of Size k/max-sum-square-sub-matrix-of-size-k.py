class Solution:
    def maximumSum(self, mat, k):
        m, n = len(mat), len(mat[0])
        pref = [[0] * (n + 1) for _ in range(m + 1)]

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                pref[i][j] = (mat[i][j] + pref[i + 1][j] + pref[i][j + 1] - pref[i + 1][j + 1])

        return max(pref[i][j] - pref[i + k][j] - pref[i][j + k] + pref[i + k][j + k] for i in range(m - k + 1) for j in range(n - k + 1))
