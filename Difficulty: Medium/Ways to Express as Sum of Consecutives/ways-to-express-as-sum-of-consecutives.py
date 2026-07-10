class Solution:
    def getCount(self, n):
        count = 0
        k = 2

        while k * (k + 1) // 2 <= n:
            x = n - k * (k - 1) // 2
            if x > 0 and x % k == 0:
                count += 1
            k += 1

        return count
