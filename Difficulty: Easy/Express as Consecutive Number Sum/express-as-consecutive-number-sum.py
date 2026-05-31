import math

class Solution:
    def isSumOfConsecutive(self, n: int) -> bool:
        if math.log2(n) == int(math.log2(n)):
            return False

        return True
