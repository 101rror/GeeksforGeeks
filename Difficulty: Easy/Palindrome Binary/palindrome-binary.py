class Solution:
    def isBinaryPalindrome(self, n):
        binary = bin(n)[2:]
            
        return True if binary == binary[::-1] else False