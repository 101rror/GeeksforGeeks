from math import gcd

class Solution:
    def minOperations(self, b):
        mod = 10**9 + 7
        n = len(b)

        visited = [False] * n
        lcm = 1

        for i in range(n):
            if not visited[i]:
                curr = i
                length = 0

                while not visited[curr]:
                    visited[curr] = True
                    curr = b[curr] - 1
                    length += 1

                lcm = (lcm // gcd(lcm, length)) * length

        return lcm % mod
