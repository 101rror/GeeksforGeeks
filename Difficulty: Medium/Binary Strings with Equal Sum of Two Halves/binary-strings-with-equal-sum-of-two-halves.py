import math

class Solution:
    def computeValue(self, n):
        MOD = 10**9 + 7
        fact = math.factorial(n)

		return int((math.factorial(2*n) // fact // fact) % (MOD))
