class Solution:
    def maxProduct(self, n):
        if n == 2:
            return 1
        if n == 3:
            return 2

        div = n // 3
        rem = n % 3

        if rem == 0:
            return pow(3, div)
        if rem == 1:
            return pow(3, div - 1) * 4

        return pow(3, div) * 2
