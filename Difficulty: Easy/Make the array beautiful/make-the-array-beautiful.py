class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        stack = []

        for num in arr:
            if stack and (stack[-1] or 1) * (num or 1) < 0:
                stack.pop()
            else:
                stack.append(num)

        return stack
