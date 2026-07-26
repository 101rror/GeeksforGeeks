class Solution:
    def levelSort(self, arr):
        n = len(arr)
        ans = []
        q = [1]

        while q:
            ans.append(sorted([arr[x - 1] for x in q]))
            nq = []
            for cur in q:
                if cur * 2 <= n:
                    nq.append(cur * 2)
                if cur * 2 + 1 <= n:
                    nq.append(cur * 2 + 1)
            q = nq

        return ans
