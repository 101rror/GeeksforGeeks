from bisect import bisect_left

class Solution:
    def minDeletions(self, arr):
        ans = []

        for num in arr:
            idx = bisect_left(ans, num)

            if idx == len(ans):
                ans.append(num)
            else:
                ans[idx] = num

        return len(arr) - len(ans)
