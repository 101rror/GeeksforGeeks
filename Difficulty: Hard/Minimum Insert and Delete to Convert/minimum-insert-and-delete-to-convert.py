import bisect as bi

class Solution:
    def minInsAndDel(self, a, b):
        db = {b[i]: i for i in range(len(b))}
        ar = [db[i] for i in a if i in db]
        ans = []
        
        for val in ar:
            i = bi.bisect_left(ans, val)
            if i == len(ans):
                ans.append(val)
            else:
                ans[i] = val
                
        return len(a) + len(b) - 2 * len(ans)
        