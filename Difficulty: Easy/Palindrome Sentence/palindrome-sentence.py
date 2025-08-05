import re

class Solution:
	def isPalinSent(self, s):
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        n=len(s)
        for i in range(n//2):
            if s[i] != s[n-i-1]:
                return False
                
        return True