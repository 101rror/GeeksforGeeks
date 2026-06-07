class Solution:
    def profession(self, level, pos):
        flips = bin(pos - 1).count('1')

        if flips % 2 == 0:
            return "Engineer"
        else:
            return "Doctor"
        