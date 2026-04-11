class Solution:
    def countIncreasing(self, arr):
        n = len(arr)
        i, j, ans = 1, 0, 0

        while(i < n):
            if arr[i] > arr[i - 1]:
                if i > j:
                    ans += (i - j)
            else:
                j = i
            i += 1
            
        return ans
