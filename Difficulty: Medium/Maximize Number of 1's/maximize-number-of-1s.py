class Solution:
    def maxOnes(self, arr, k):
        left = 0
        count0, maxlen = 0, 0

        for right in range(len(arr)):
            if arr[right] == 0:
                count0 += 1

            while count0 > k:
                if arr[left] == 0:
                    count0 -= 1
                left += 1

            maxlen = max(maxlen, right - left + 1)

        return maxlen