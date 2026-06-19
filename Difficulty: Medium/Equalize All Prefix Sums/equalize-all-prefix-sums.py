class Solution:
    def optimalArray(self, arr):
        ans = [0]

        for i in range(1, len(arr)):
            val = ans[-1] + (arr[i] - arr[i // 2])
            ans.append(val)

        return ans