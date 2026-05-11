from math import lcm

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [1] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)
        

    def build(self, arr, idx, l, r):
        if l == r:
            self.tree[idx] = arr[l]
            return

        mid = (l + r) // 2

        self.build(arr, idx * 2, l, mid)
        self.build(arr, idx * 2 + 1, mid + 1, r)

        self.tree[idx] = lcm(self.tree[idx * 2], self.tree[idx * 2 + 1])
        

    def update(self, idx, l, r, pos, val):
        if l == r:
            self.tree[idx] = val
            return

        mid = (l + r) // 2

        if pos <= mid:
            self.update(idx * 2, l, mid, pos, val)
        else:
            self.update(idx * 2 + 1, mid + 1, r, pos, val)

        self.tree[idx] = lcm(self.tree[idx * 2], self.tree[idx * 2 + 1])
        

    def query(self, idx, l, r, ql, qr):
        if qr < l or r < ql:
            return 1

        if ql <= l and r <= qr:
            return self.tree[idx]

        mid = (l + r) // 2

        return lcm(self.query(idx * 2, l, mid, ql, qr), self.query(idx * 2 + 1, mid + 1, r, ql, qr))


class Solution:
    def RangeLCMQuery(self, arr, queries):
        st = SegmentTree(arr)
        ans = []

        for q in queries:
            if q[0] == 1:
                st.update(1, 0, st.n - 1, q[1], q[2])
            else:
                ans.append(st.query(1, 0, st.n - 1, q[1], q[2]))

        return ans
