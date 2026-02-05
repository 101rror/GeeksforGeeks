class Solution:
    def maxOnes(self, arr, k):
        n = len(arr)
        left = zero = mx = 0

        for right in range(n):
            if arr[right] == 0:
                zero += 1

            while zero > k:
                if arr[left] == 0:
                    zero -= 1
                left += 1

            mx = max(mx, right - left + 1)

        return mx