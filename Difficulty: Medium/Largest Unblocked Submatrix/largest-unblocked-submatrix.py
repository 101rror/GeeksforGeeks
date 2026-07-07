class Solution:
    def largestArea(self, n, m, arr):
        rows = sorted(r for r, c in arr)
        cols = sorted(c for r, c in arr)

        mxro = prev = 0

        for r in rows:
            mxro = max(mxro, r - prev - 1)
            prev = r
        mxro = max(mxro, n - prev)

        mxco = 0
        prev = 0
        for c in cols:
            mxco = max(mxco, c - prev - 1)
            prev = c
        mxco = max(mxco, m - prev)

        return mxro * mxco
