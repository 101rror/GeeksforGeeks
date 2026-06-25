class Solution:
    def increasingNumbers(self, n):
        ans = []
        
        if n == 1:
            return [i for i in range(10)]

        if n > 9:
            return ans

        def backtrack(start, length, num):
            if length == n:
                ans.append(num)
                return

            for digit in range(start, 10):
                backtrack(digit + 1, length + 1, num * 10 + digit)

        backtrack(1, 0, 0)
        
        return ans
        
