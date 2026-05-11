from math import lcm

class Solution:
    def RangeLCMQuery(self, arr, queries):
        n = len(arr)
        seg = [1] * (4 * n)

        def build(i, l, r):
            if l == r:
                seg[i] = arr[l]
                return

            m = (l + r) // 2

            build(i * 2, l, m)
            build(i * 2 + 1, m + 1, r)

            seg[i] = lcm(seg[i * 2], seg[i * 2 + 1])

        def update(i, l, r, p, v):
            if l == r:
                seg[i] = v
                return

            m = (l + r) // 2

            if p <= m:
                update(i * 2, l, m, p, v)
            else:
                update(i * 2 + 1, m + 1, r, p, v)

            seg[i] = lcm(seg[i * 2], seg[i * 2 + 1])

        def query(i, l, r, ql, qr):
            if qr < l or ql > r:
                return 1

            if ql <= l and r <= qr:
                return seg[i]

            m = (l + r) // 2

            return lcm(query(i * 2, l, m, ql, qr), query(i * 2 + 1, m + 1, r, ql, qr))

        build(1, 0, n - 1)

        ans = []

        for q in queries:
            if q[0] == 1:
                update(1, 0, n - 1, q[1], q[2])
            else:
                ans.append(query(1, 0, n - 1, q[1], q[2]))

        return ans
